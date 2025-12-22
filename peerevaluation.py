# peer evaluation filter

import pandas as pd
df = pd.read_csv('matdis-presentasi.csv')
df["Timestamp"] = pd.to_datetime(df["Timestamp"])
# 450 

# kolom kehadiran
df.iloc[:, 11] = df.iloc[:, 11].astype(str).str.extract(r"(\d+)").astype("Int64")


# yang menilai lebih dari sekali
df = df.sort_values("Timestamp").drop_duplicates(
    subset=["Kelompok yang dinilai:", "Email Address"],
    keep="last"
)
# 435

email_counts = df["Email Address"].value_counts()


# hapus nilai maksimum (jilatan)
df = df[
    ~(
        (df.iloc[:, 3]  == 10) &
        (df.iloc[:, 4]  == 10) &
        (df.iloc[:, 5]  == 5)  &
        (df.iloc[:, 6]  == 10) &
        (df.iloc[:, 7]  == 10) &
        (df.iloc[:, 8]  == 10) &
        (df.iloc[:, 9]  == 10) &
        (df.iloc[:,10]  == 10)
    )
]
# 285


stats_filtered = (
    df.assign(row_sum=df.iloc[:, 3:11].sum(axis=1))
      .groupby(df.iloc[:, 2])["row_sum"]
      .agg(
          max="max",
          mean="mean",
          q1=lambda x: x.quantile(0.25),
          median=lambda x: x.quantile(0.50),
          q3=lambda x: x.quantile(0.75),
      )
)
