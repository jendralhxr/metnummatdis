import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

x = np.linspace(3, 10, 500)
y = skewnorm.pdf(x, a=6, loc=3.5, scale=1.5) * 10
np.random.seed(420) # masukkan NRP
y = y + np.random.normal(0, 0.02, size=x.shape)  # add Gaussian noise


# Plot
plt.figure(figsize=(8,5))
plt.plot(x, y, color="navy", linewidth=2)
plt.title("Penjualan")
plt.xlabel("x (harga, ribuan)")
plt.ylabel("y (jumlah barang laku, ratusan)")
plt.grid(True)
plt.show()
