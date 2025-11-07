import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import Counter
import math
from itertools import combinations
import itertools

# #####
# Fanny Widya Cahyani (24083010045)
# Izzati Kamila Putri (24083010059)
# Adrian Veda Darmawan (24083010090)

G = nx.Graph()

mahasiswa = [
"Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
"Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
"Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
"Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
"Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
"Kiky", "Sofia", "Varid", "Gaitsa"]
G.add_nodes_from(mahasiswa)

sekelompok= [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]
relasi = sekelompok.copy()
G.add_edges_from(relasi, color='red')

def tambah_relasi_dari_array(array):
  for i in range(len(array)):
    for j in range(len(array)-i-1):
      relasi.append((array[i], array[j+i+1]))

akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia",
          "Indra", "Madina", "Maulida", "Kiky", "Varid"]
jabodetabek = ["Sofia", "Maria", "Gaitsa", "Aisyah"]
tambah_relasi_dari_array(jabodetabek)
platP= ["Angel", "Yuniar"]; tambah_relasi_dari_array(platP)
platS= ["Naia", "Izzati"]; tambah_relasi_dari_array(platS)
platM= ["Dany", "Alimun"]; tambah_relasi_dari_array(platM)
platN= ["Amelia", "Alfani"]; tambah_relasi_dari_array(platN)
platAx= ["Adrian", "Raveena", "Selvy", "Fanny"]; tambah_relasi_dari_array(platAx)
sekos= ["Aisyah", "Naia"]; tambah_relasi_dari_array(sekos)
himasada= ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia",
           "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]
tambah_relasi_dari_array(himasada)
BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]; tambah_relasi_dari_array(BEMfakultas)
warkopbening = ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]; tambah_relasi_dari_array(warkopbening)
skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]; tambah_relasi_dari_array(skincaredanmakeup)
kacamata = ["Adrian", "Fanny", "Izzati", "Hizkia", "Maria", "Naia", "Madina", "Maulida", "Via", "Varid", "Aquina", "Alimun", "Indra"]; tambah_relasi_dari_array(kacamata)
luarpulaujawa = ["Febriani", "Ophyng", "Laudya"]; tambah_relasi_dari_array(luarpulaujawa)

G1 = G.copy()

# Nama Kelompok : imupp
# 24083010001 - Madina Hedy A
# 24083010044 - Via Amanda
# 24083010048 - Alfani Nur Azizah
# 24083010057 - Maulida Aprilia P

G = nx.Graph()
mahasiswa = [
"Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
"Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
"Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
"Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
"Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
"Kiky", "Sofia", "Varid", "Gaitsa"]
G.add_nodes_from(mahasiswa)

sekos = ["Aisyah", "Naia"]
himasada = ["Dany", "Esthi", "Via", "Madina", "Alfani", "Maulida", "Febriani", "Angel"]
BEMfakultas = ["Hafiyyan", "Varid", "Carissa"]
warkopbening = ["Yuniar", "Wildan", "Dany", "Izzati"]
skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia", "Naia", "Carissa"]
makanbareng = ["Via", "Alfani", "Maulida", "Madina", "Gendis", "Diah", "Aquina", "Maya"]
kupukupu = ["Maria", "Adinda", "Alimun", "Aisyah", "Amelia", "Naia", "Kenzy", "Erik", "Maya", "Wildan", "Naufal", "Laudya", "Adrian", "Selvy", "Indra", "Gaitsa"]
kurakura = ["Alfani", "Via", "Maulida", "Madina", "Gendis", "Raveena", "Ophyng", "Febriani", "Angel", "Auliya", "Carissa", "Dany", "Esthi", "Hafiyyan", "Yuniar", "Varid"]
danusan = ["Maria", "Auliya", "Ophyng", "Fanny", "Izzati", "Kiky", "Varid"]

# Gabungkan semua ke dictionary agar mudah di-loop
clusters = {
    "sekos": sekos,
    "himasada": himasada,
    "BEMfakultas": BEMfakultas,
    "warkopbening": warkopbening,
    "skincaredanmakeup": skincaredanmakeup,
    "makanbareng": makanbareng,
    "kupukupu": kupukupu,
    "kurakura": kurakura,
    "danusan": danusan
}

# Warna edge berbeda untuk tiap klaster
colors = [
    "red", "blue", "green", "orange", "purple", "cyan",
    "magenta", "gold", "brown"
]
cluster_colors = dict(zip(clusters.keys(), colors))

# Tambahkan koneksi pertemanan dalam tiap klaster
for cluster_name, members in clusters.items():
    for a, b in itertools.combinations(members, 2):
        G.add_edge(a, b, group=cluster_name, color=cluster_colors[cluster_name])
        
G2 = G.copy()

#######
# MARIA DWI KURNIASIH 24083010003
# HIZKIA SAMHAN REZAYOSHI 24083010019
# NAJWA SOFIA 24083010115

# --- Fungsi untuk menambahkan klaster dengan warna berbeda ---
def add_cluster_edges(graph, cluster, color):
    """Tambahkan edges antar anggota cluster dengan warna tertentu"""
    for i in range(len(cluster)):
        for j in range(i+1, len(cluster)):
            graph.add_edge(cluster[i], cluster[j], color=color)

# --- Buat graph dan nodes ---
G = nx.Graph()

mahasiswa = [
"Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
"Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
"Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
"Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
"Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
"Kiky", "Sofia", "Varid", "Gaitsa"]
G.add_nodes_from(mahasiswa)

# --- Klaster pertemanan ---
# Misal beberapa klaster
akamsi = ["Via", "Esthi", "Indra", "Madina", "Maulida", "Kiky", "Diva"]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah", "Hizkia"]
platP = ["Angel", "Selvy", "Amelia"]
platS = ["Naia", "Izzati", "Varid", "Kiky"]
platM = ["Dany", "Alimun", "Kenzy", "Erik"]
platN = ["Alfani", "Diah", "Naufal"]
platAx = ["Adrian", "Selvy", "Fanny", "Gaitsa"]
sekos = ["Aisyah", "Naia", "Maria", "Angel", "Laudya", "Adrian", "Ophyng"]
himasada = ["Dany", "Esthi", "Naia", "Via", "Madina", "Alfani", "Maulida", "Febriani"]
BEMfakultas = ["Hafiyyan", "Varid", "Carissa", "Raveena", "Wildan"]
warkopbening = ["Wildan", "Dany", "Izzati", "Erik", "Hafiyyan", "Diah", "Kenzy"]
skincaredanmakeup = ["Hizkia", "Kiky", "Sofia", "Maria", "Yuniar"]
makanbareng = ["Ophyng", "Varid", "Gaitsa", "Carissa", "Diva", "Aquina", "Sofia"]
nontonfilm = ["Febriani", "Laudya", "Naufal", "Adinda", "Auliya", "Gendis", "Maya", "Adrian"]
UKM = ["Maria", "Ophyng"]
kerja = ["Varid", "Wildan"]
Panitia = ["Ophyng", "Maria", "Hizkia", "Sofia", "Via", "Esthi", "Carissa", "Madina", "Varid", "Maulida", "Naufal",
           "Selvy", "Dany", "Gaitsa", "Fanny", "Izzati", "Naia"]

# Warna klaster
clusters = [
    (akamsi, "red"),
    (jabodetabek, "blue"),
    (platP, "green"),
    (platS, "purple"),
    (platM, "orange"),
    (platN, "brown"),
    (platAx, "pink"),
    (sekos, "cyan"),
    (himasada, "magenta"),
    (BEMfakultas, "yellow"),
    (warkopbening, "grey"),
    (skincaredanmakeup, "black"),
    (makanbareng, "lightgreen"),
    (nontonfilm, "darkblue"),
    (UKM, "maroon"),
    (kerja, "teal"),
    (Panitia, "lightgrey")
]

# Tambahkan edges sesuai klaster
for cluster, color in clusters:
    add_cluster_edges(G, cluster, color)
    
G3= G.copy()

##
# Raveena Ayu Desember Suryoputri (24083010028)
# Amelia Rizqyna Putri (24083010042)
# Yuniar Rachmawati (24083010106)
G = nx.Graph()

def buat_koneksi_klaster(graph, anggota_list, warna_edge):
    """
    Fungsi untuk membuat koneksi pertemanan secara iteratif untuk anggota klaster
    Semua anggota dalam klaster akan saling terhubung (complete graph)

    Parameters:
    - graph: Graf NetworkX
    - anggota_list: List nama anggota dalam klaster
    - warna_edge: Warna edge untuk klaster ini

    Returns:
    - Jumlah koneksi yang ditambahkan
    """
    koneksi_baru = 0

    # Iterasi untuk membuat semua pasangan dalam klaster
    for i in range(len(anggota_list)):
        for j in range(i + 1, len(anggota_list)):
            person1 = anggota_list[i]
            person2 = anggota_list[j]

            # Tambahkan edge dengan warna tertentu
            graph.add_edge(person1, person2, color=warna_edge)
            koneksi_baru += 1

    return koneksi_baru

# ============================================================================
# FUNGSI UNTUK MEMBUAT KONEKSI PERTEMANAN SECARA ITERATIF
# ============================================================================
def buat_koneksi_klaster(graph, anggota_list, warna_edge):
    """
    Fungsi untuk membuat koneksi pertemanan secara iteratif untuk anggota klaster
    Semua anggota dalam klaster akan saling terhubung (complete graph)

    Parameters:
    - graph: Graf NetworkX
    - anggota_list: List nama anggota dalam klaster
    - warna_edge: Warna edge untuk klaster ini

    Returns:
    - Jumlah koneksi yang ditambahkan
    """
    koneksi_baru = 0

    # Iterasi untuk membuat semua pasangan dalam klaster
    for i in range(len(anggota_list)):
        for j in range(i + 1, len(anggota_list)):
            person1 = anggota_list[i]
            person2 = anggota_list[j]

            # Tambahkan edge dengan warna tertentu
            graph.add_edge(person1, person2, color=warna_edge)
            koneksi_baru += 1

    return koneksi_baru


# ============================================================================
# DATA MAHASISWA
# ============================================================================
mahasiswa = [
    "Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
    "Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
    "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
    "Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
    "Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
    "Kiky", "Sofia", "Varid", "Gaitsa"
]
G.add_nodes_from(mahasiswa)


# ============================================================================
# KONEKSI KELOMPOK AWAL (SEKELOMPOK)
# ============================================================================
sekelompok = [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]
G.add_edges_from(sekelompok, color='red')


# ============================================================================
# LENGKAPI DAN TAMBAHKAN KLASTER PERTEMANAN
# ============================================================================
klaster = {
    "akamsi": (["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia",
                "Indra", "Madina", "Maulida", "Kiky"], "purple"),

    "jabodetabek": (["Sofia", "Maria", "Gaitsa", "Aisyah"], "pink"),

    "platP": (["Angel"], "red"),

    "platS": (["Naia", "Izzati"], "orange"),

    "platM": (["Dany", "Alimun"], "green"),

    "platN": (["Amelia", "Alfani"], "cyan"),

    "platAx": (["Adrian", "Raveena", "Selvy", "Fanny"], "yellow"),

    "sekos": (["Aisyah", "Naia"], "brown"),

    "himasada": (["Dany", "Kiky", "Esthi", "Via", "Madina", "Alfani", "Maulida"], "blue"),

    "BEMfakultas": (["Hafiyyan", "Varid", "Carissa"], "lime"),

    "warkopbening": (["Wildan", "Dany", "Maulida", "Izzati"], "orange"),

    "skincaredanmakeup": (["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"], "magenta"),

    "makanbareng": (["Raveena", "Amelia", "Alimun", "Wildan", "Kenzy", "Yuniar", "Indra"], "red"),

    "transportkeUPN_motor": (["Madina", "Adinda", "Aquina", "Alimun", "Raveena", "Amelia", "Via", "Fanny",
                              "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya", "Carissa",
                              "Diva", "Erik", "Maya", "Dany", "Wildan", "Esthi", "Naufal", "Adrian", "Selvy",
                              "Hafiyyan", "Indra", "Yuniar", "Kiky", "Sofia", "Varid", "Gaitsa"], "gray")
}


# ============================================================================
# GUNAKAN WARNA EDGE YANG BERBEDA UNTUK TIAP JENIS KLASTER PERTEMANAN
# ============================================================================
for nama_klaster, (anggota, warna) in klaster.items():
    if len(anggota) > 1:  # Hanya proses jika lebih dari 1 anggota
        jumlah_koneksi = buat_koneksi_klaster(G, anggota, warna)
        print(f"{nama_klaster:30s} | Anggota: {len(anggota):2d} | Koneksi: {jumlah_koneksi:4d} | Warna: {warna}")
    else:
        print(f"{nama_klaster:30s} | Anggota: {len(anggota):2d} | Koneksi:    0 | Warna: {warna} (hanya 1 orang)")

G4 = G.copy()

# #####
# Esthi Nurani Sri Handayani - 24083010081
# Selvy Dwi Yulita Sari - 24083010095
# Kiky Maudry Natasya - 24083010110

def buat_klaster(G, anggota, warna_edge, nama_klaster):
    """
    Membuat koneksi antar semua anggota klaster (complete subgraph)
    dan memberi warna edge sesuai klaster.
    """
    kombinasi = list(itertools.combinations(anggota, 2))
    for u, v in kombinasi:
        G.add_edge(u, v, color=warna_edge, cluster=nama_klaster)
    return kombinasi

#  DATA MAHASISWA
mahasiswa = [
    "Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
    "Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
    "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
    "Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
    "Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
    "Kiky", "Sofia", "Varid", "Gaitsa"
]
G = nx.Graph()
G.add_nodes_from(mahasiswa)

#  DEFINISI KLASTER & WARNA

klaster_pertemanan = {
    "Sekelompok Tugas": {
        "anggota": [
            ["Raveena", "Amelia", "Yuniar"],
            ["Hizkia", "Maria", "Sofia"],
            ["Naufal", "Laudya", "Febriani"],
            ["Kenzy", "Wildan", "Hafiyyan"],
            ["Alimun", "Dany", "Indra"],
            ["Esthi", "Kiky", "Selvy"],
            ["Adrian", "Izzati", "Fanny"],
            ["Aquina", "Diva", "Maya"],
            ["Diah", "Gendis", "Angel"],
            ["Ophyng", "Aisyah", "Naia"],
            ["Adinda", "Varid", "Gaitsa"],
            ["Auliya", "Carissa", "Erik"],
            ["Madina", "Via", "Maulida", "Alfani"]
        ],
        "warna": "red"
    },
    "Akamsi (Satu Daerah)": {
        "anggota": [["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia", "Indra", "Madina", "Maulida", "Kiky"]],
        "warna": "green"
    },
    "Jabodetabek": {
        "anggota": [["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]],
        "warna": "blue"
    },
    "Sekosan": {
        "anggota": [["Aisyah", "Naia"]],
        "warna": "purple"
    },
    "HIMASADA": {
        "anggota": [["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia", "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]],
        "warna": "orange"
    },
    "BEM Fakultas": {
        "anggota": [["Indra", "Hafiyyan", "Varid", "Carissa", "Ophyng"]],
        "warna": "yellow"
    },
    "Warkop Bening": {
        "anggota": [["Erik", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]],
        "warna": "brown"
    },
    "Skincare & Makeup": {
        "anggota": [["Hizkia", "Kiky", "Selvy", "Auliya", "Sofia", "Gaitsa"]],
        "warna": "pink"
    },
    "Team Ngoding": {
        "anggota": [["Adrian", "Indra", "Dany", "Wildan", "Kenzy"]],
        "warna": "cyan"
    },
    "Team Futsal": {
        "anggota": [["Varid", "Wildan", "Hafiyyan", "Dany", "Adrian"]],
        "warna": "lime"
    },
    "Team Nugas Malam": {
        "anggota": [["Adrian", "Amelia", "Via", "Madina", "Naia", "Aisyah"]],
        "warna": "magenta"
    },
    "Anak Cafe": {
        "anggota": [["Laudya", "Naufal", "Maulida", "Wildan", "Izzati", "Diva", "Amelia"]],
        "warna": "deepskyblue"
    },
    "Pecinta Drama Korea": {
        "anggota": [["Aisyah", "Naia", "Selvy", "Sofia", "Fanny", "Maria"]],
        "warna": "lightcoral"
    },
    "Pecinta Kucing": {
        "anggota": [["Gaitsa", "Adinda", "Naia", "Gendis", "Madina"]],
        "warna": "plum"
    },
    "Geng Pendaki": {
        "anggota": [["Kenzy", "Indra", "Wildan", "Varid", "Hafiyyan", "Dany"]],
        "warna": "darkgreen"
    }
}

for nama_klaster, data in klaster_pertemanan.items():
    warna = data["warna"]
    for grup in data["anggota"]:
        buat_klaster(G, grup, warna, nama_klaster)

G5 = G.copy()
        
######


# Yohanes Olvin Jun Sole [2408301029]
# Aisyah Amalia Hamid [24083010034]
# Siti Naia Hesti Rachmawati [24083010047]

G = nx.Graph()
# Data mahasiswa
mahasiswa = [
    "Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
    "Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
    "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
    "Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
    "Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
    "Kiky", "Sofia", "Varid", "Gaitsa"
]

G.add_nodes_from(mahasiswa)
# Data kelompok awal
sekelompok = [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]

G.add_edges_from(sekelompok, color='red')
# Data asal daerah
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia",
          "Indra", "Madina", "Maulida", "Kiky"]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP = ["Angel", "Yuniar"]
platS = ["Naia", "Izzati"]
platM = ["Dany", "Alimun"]
platN = ["Amelia", "Alfani"]
platAx = ["Adrian", "Raveena", "Selvy", "Fanny"]

# Data organisasi dan lainnya
himasada = ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia",
           "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]
BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]
warkopbening = ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]
skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]

def buat_klaster_pertemanan(graph, anggota_klaster, warna, label):
    """
    Fungsi untuk membuat koneksi pertemanan secara iteratif dalam sebuah klaster
    """
    edges_ditambahkan = 0
    for i in range(len(anggota_klaster)):
        for j in range(i + 1, len(anggota_klaster)):
            # Cek apakah edge sudah ada
            if not graph.has_edge(anggota_klaster[i], anggota_klaster[j]):
                graph.add_edge(anggota_klaster[i], anggota_klaster[j], color=warna, label=label)
                edges_ditambahkan += 1
    return edges_ditambahkan

# Warna-warna untuk klaster yang berbeda
warna_klaster = {
    'sekelompok': 'red',
    'asal_daerah': 'blue',
    'hobi': 'green',
    'akademik': 'purple',
    'sosial_media': 'orange',
    'tempat_tinggal': 'brown',
    'organisasi': 'pink',
    'lainnya': 'gray'
}

# Klaster tambahan
# 1. Klaster hobi dan minat
olahraga = ["Wildan", "Hafiyyan", "Naufal", "Dany", "Indra", "Varid"]
musik = ["Auliya", "Carissa", "Erik", "Diva", "Maya", "Gaitsa"]
membaca = ["Madina", "Alfani", "Via", "Maulida", "Adinda"]
kuliner = ["Yuniar", "Raveena", "Amelia", "Kiky", "Esthi"]

# 2. Klaster akademik
kelas_pagi = ["Maria", "Hizkia", "Sofia", "Adinda", "Varid", "Gaitsa"]
kelas_siang = ["Madina", "Via", "Alfani", "Maulida", "Auliya", "Carissa"]
matkul_favorit = ["Amelia", "Yuniar", "Raveena", "Wildan", "Dany"]

# 3. Klaster sosial media
group_wa_1 = ["Raveena", "Amelia", "Yuniar", "Wildan", "Dany", "Maulida"]
group_wa_2 = ["Hizkia", "Maria", "Sofia", "Adinda", "Varid"]
instagram_close_friends = ["Aisyah", "Naia", "Ophyng", "Febriani", "Laudya"]

# 4. Klaster tempat tinggal
kos_putri = ["Madina", "Via", "Alfani", "Maulida", "Aisyah", "Naia"]
kos_putra = ["Wildan", "Hafiyyan", "Naufal", "Dany", "Alimun"]
asrama = ["Yuniar", "Raveena", "Amelia", "Kiky", "Esthi"]

klaster_tambahan = [
    (akamsi, warna_klaster['asal_daerah'], "Asal Daerah - AKAMSI"),
    (jabodetabek, warna_klaster['asal_daerah'], "Asal Daerah - Jabodetabek"),
    (platP, warna_klaster['asal_daerah'], "Asal Daerah - Plat P"),
    (platS, warna_klaster['asal_daerah'], "Asal Daerah - Plat S"),
    (platM, warna_klaster['asal_daerah'], "Asal Daerah - Plat M"),
    (platN, warna_klaster['asal_daerah'], "Asal Daerah - Plat N"),
    (platAx, warna_klaster['asal_daerah'], "Asal Daerah - Plat Ax"),

    (olahraga, warna_klaster['hobi'], "Hobi - Olahraga"),
    (musik, warna_klaster['hobi'], "Hobi - Musik"),
    (membaca, warna_klaster['hobi'], "Hobi - Membaca"),
    (kuliner, warna_klaster['hobi'], "Hobi - Kuliner"),

    (kelas_pagi, warna_klaster['akademik'], "Akademik - Kelas Pagi"),
    (kelas_siang, warna_klaster['akademik'], "Akademik - Kelas Siang"),
    (matkul_favorit, warna_klaster['akademik'], "Akademik - Matkul Favorit"),

    (group_wa_1, warna_klaster['sosial_media'], "Sosial Media - Group WA 1"),
    (group_wa_2, warna_klaster['sosial_media'], "Sosial Media - Group WA 2"),
    (instagram_close_friends, warna_klaster['sosial_media'], "Sosial Media - Instagram Close Friends"),

    (kos_putri, warna_klaster['tempat_tinggal'], "Tempat Tinggal - Kos Putri"),
    (kos_putra, warna_klaster['tempat_tinggal'], "Tempat Tinggal - Kos Putra"),
    (asrama, warna_klaster['tempat_tinggal'], "Tempat Tinggal - Asrama"),

    (himasada, warna_klaster['organisasi'], "Organisasi - Himasada"),
    (BEMfakultas, warna_klaster['organisasi'], "Organisasi - BEM Fakultas"),
    (warkopbening, warna_klaster['sosial_media'], "Tempat Nongkrong - Warkop Bening"),
    (skincaredanmakeup, warna_klaster['hobi'], "Hobi - Skincare & Makeup")
]

print("Menambahkan klaster pertemanan...")
total_edges_ditambahkan = 0
for klaster, warna, label in klaster_tambahan:
    edges_ditambahkan = buat_klaster_pertemanan(G, klaster, warna, label)
    total_edges_ditambahkan += edges_ditambahkan
    print(f"Klaster {label}: {edges_ditambahkan} edge ditambahkan")
    
G6= G.copy()


####
# Aquina Syabita (24083010006): Menambah Klaster beserta node & edge dengan warna berbeda untuk Visualisasi Graph Jaringan Pertemanan Mahasiswa dan Analisis 1 (3 Orang dengan Koneksi Terbanyak) beserta visualisasi dan interpretasi hasil output.
# Diva Anggraeni (24083010065): Analisis 3a dan 3b (bridge person nx.betweenness_centrality(6) dan bridge person dengan koneksi paling sedikit) beserta visualisasi dan hasil output.
# Maya Purnama Sari (24083010074): Analisis 2 (Pasangan-pasangan yang paling jauh koneksinya) beserta visualisasi dan hasil output.
    
G = nx.Graph()
# Data Mahasiswa
mahasiswa = [
    "Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
    "Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
    "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
    "Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
    "Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
    "Kiky", "Sofia", "Varid", "Gaitsa"
]
G.add_nodes_from(mahasiswa)

# Klaster Awal
sekelompok = [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]
G.add_edges_from(sekelompok, color="red")

# Fungsi Tambah Klaster
def tambah_klaster(anggota, warna):
    for i in range(len(anggota)):
        for j in range(i + 1, len(anggota)):
            G.add_edge(anggota[i], anggota[j], color=warna)

# Klaster Tambahan
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia",
          "Indra", "Madina", "Maulida", "Kiky", "Wildan"]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP = ["Angel", "Yuniar"]
platS = ["Naia", "Izzati"]
platM = ["Dany", "Alimun"]
platN = ["Amelia", "Alfani"]
platAx = ["Adrian", "Raveena", "Selvy", "Fanny"]
sekos = ["Aisyah", "Naia", "Diah", "Fanny"]

himasada = ["Dany", "Yuniar", "Kiky", "Esthi", "Raveena",
            "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]
BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]
warkopbening = ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]
skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]

drakor_lovers = ["Naia", "Aisyah", "Sofia", "Maria", "Gendis", "Aquina", "Maya", "Yuniar"]
gaming_team = ["Wildan", "Ophyng", "Indra", "Erik", "Kenzy", "Diah", "Aquina"]
pecinta_kopi = ["Raveena", "Yuniar", "Madina", "Maulida", "Dany", "Maya", "Gendis"]
tugas_bareng = ["Adinda", "Varid", "Gaitsa", "Carissa", "Auliya", "Raveena", "Wildan", "Angel", "Diva"]

# Warna Klaster
klaster_dan_warna = [
    (akamsi, "orange"), (jabodetabek, "lightblue"), (platP, "violet"),
    (platS, "gray"), (platM, "green"), (platN, "yellow"),
    (platAx, "red"), (sekos, "lightgreen"),
    (himasada, "gold"), (BEMfakultas, "purple"),
    (warkopbening, "lightcoral"), (skincaredanmakeup, "pink"),
    (drakor_lovers, "cyan"), (gaming_team, "blue"),
    (pecinta_kopi, "brown"), (tugas_bareng, "black")
]

for klaster, warna in klaster_dan_warna:
    tambah_klaster(klaster, warna)

# Legend Warna Klaster
legend_colors = {
    "Akamsi": "orange",
    "Jabodetabek": "lightblue",
    "Plat P": "violet",
    "Plat S": "gray",
    "Plat M": "green",
    "Plat N": "yellow",
    "Plat Ax": "red",
    "Sekos": "lightgreen",
    "Himasada": "gold",
    "BEM Fakultas": "purple",
    "Warkop Bening": "lightcoral",
    "Skincare & Makeup": "pink",
    "Drakor Lovers": "cyan",
    "Gaming Team": "blue",
    "Pecinta Kopi": "brown",
    "Tugas Bareng": "black"
}

# Warna Node
degrees = dict(G.degree())
max_deg = max(degrees.values())

for node, deg in degrees.items():
    if deg >= 0.75 * max_deg:
        color = "lightgreen"      # sangat populer
    elif deg >= 0.5 * max_deg:
        color = "gold"            # sedang
    else:
        color = "lightcoral"      # sedikit koneksi
    G.nodes[node]["color"] = color


G7 = G.copy()

###
# 24083010054 ~ Ahmad Kenzy Farzaq
# Membuat visualisasi data
# Mengerjakan analisis nomor 3 dan tambahan
# Menambahkan analisis tambahan 1
# 24083010079 ~ Muhammad Wildan Sultansyah
# Mengerjakan analisis nomor 2
# Menambahkan analisis tambahan 2
# Membuat heatmap jarak antar node
# 24083010099 ~ Rizki Faza Hafiyyan Nusantara
# Mengerjakan analisis nomor 1 dan tambahan
# Menghitung degree per node

mahasiswa = [
    "Adinda", "Adrian", "Aisyah", "Alfani", "Alimun", "Amelia", "Angel",
    "Aquina", "Auliya", "Carissa", "Dany", "Diah", "Diva", "Erik", "Esthi",
    "Fanny", "Febriani", "Gaitsa", "Gendis", "Hafiyyan", "Hizkia", "Indra",
    "Izzati", "Kenzy", "Kiky", "Laudya", "Madina", "Maria", "Maulida",
    "Maya", "Naia", "Naufal", "Ophyng", "Raveena", "Selvy", "Sofia",
    "Varid", "Via", "Wildan", "Yuniar"
    ]

G = nx.Graph()
G.add_nodes_from(mahasiswa)

sekelompok = [
    ("Amelia", "Raveena"), ("Amelia", "Yuniar"), ("Yuniar", "Raveena"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Maria", "Sofia"),
    ("Febriani", "Laudya"), ("Febriani", "Naufal"), ("Laudya", "Naufal"),
    ("Hafiyyan", "Kenzy"), ("Hafiyyan", "Wildan"), ("Kenzy", "Wildan"),
    ("Alimun", "Dany"), ("Alimun", "Indra"), ("Dany", "Indra"),
    ("Esthi", "Kiky"), ("Esthi", "Selvy"), ("Kiky", "Selvy"),
    ("Adrian", "Fanny"), ("Adrian", "Izzati"), ("Fanny", "Izzati"),
    ("Aquina", "Diva"), ("Aquina", "Maya"), ("Diva", "Maya"),
    ("Angel", "Diah"), ("Angel", "Gendis"), ("Diah", "Gendis"),
    ("Aisyah", "Naia"), ("Aisyah", "Ophyng"), ("Naia", "Ophyng"),
    ("Adinda", "Gaitsa"), ("Adinda", "Varid"), ("Gaitsa", "Varid"),
    ("Auliya", "Carissa"), ("Auliya", "Erik"), ("Carissa", "Erik"),
    ("Alfani", "Madina"), ("Alfani", "Maulida"), ("Alfani", "Via"),
    ("Madina", "Maulida"), ("Madina", "Via"), ("Maulida", "Via")
    ]

G.add_edges_from(sekelompok, color='red')

# Klaster asal daerah
akamsi = ["Amelia", "Esthi", "Indra", "Kenzy", "Kiky", "Madina",
          "Maulida", "Via", "Yuniar"]
jabodetabek = ["Aisyah", "Fanny", "Gaitsa", "Maria", "Sofia"]
platP = ["Angel", "Yuniar"]
platS = ["Izzati", "Naia"]
platM = ["Alimun", "Dany"]
platAx = ["Adrian", "Fanny", "Raveena", "Selvy"]

# Klaster lainnya
sekos = ["Aisyah", "Naia"]
himasada = ["Alfani", "Amelia", "Dany", "Esthi", "Kiky", "Madina", "Maulida",
            "Naia", "Raveena", "Selvy", "Via", "Yuniar"]
BEMfakultas = ["Carissa", "Hafiyyan", "Indra", "Raveena", "Varid"]
warkopbening = ["Dany", "Izzati", "Maulida", "Raveena", "Wildan", "Yuniar"]
skincaredanmakeup = ["Amelia", "Hizkia", "Kiky", "Raveena", "Sofia", "Yuniar"]
datangawal = ["Alimun", "Angel", "Aquina", "Dany", "Indra", "Madina"]
datangmepet = ["Carissa", "Erik", "Hafiyyan", "Kenzy", "Varid", "Wildan"]
dudukdepan = ["Adrian", "Alfani", "Madina", "Maulida", "Via"]
dudukbelakang = ["Alimun", "Dany", "Hafiyyan", "Indra", "Kenzy", "Naufal", "Wildan"]

# Definisi klaster
klaster_info = {
    # Klaster asal daerah
    'akamsi': {
        'members': ["Amelia", "Esthi", "Indra", "Kenzy", "Kiky", "Madina",
                   "Maulida", "Via", "Yuniar"],
        'color': 'blue',
        'label': 'AKAMSI'
    },
    'jabodetabek': {
        'members': ["Aisyah", "Fanny", "Gaitsa", "Maria", "Sofia"],
        'color': 'green',
        'label': 'Jabodetabek'
    },
    'platP': {
        'members': ["Angel", "Yuniar"],
        'color': 'steelblue',
        'label': 'Plat P'
    },
    'platS': {
        'members': ["Izzati", "Naia"],
        'color': 'darkgreen',
        'label': 'Plat S'
    },
    'platM': {
        'members': ["Alimun", "Dany"],
        'color': 'darkblue',
        'label': 'Plat M'
    },
    'platAx': {
        'members': ["Adrian", "Fanny", "Raveena", "Selvy"],
        'color': 'mediumblue',
        'label': 'Plat AX'
    },
    # Klaster lainnya
    'sekos': {
        'members': ["Aisyah", "Naia"],
        'color': 'cyan',
        'label': 'Sekos'
    },
    'himasada': {
        'members': ["Alfani", "Amelia", "Dany", "Esthi", "Kiky", "Madina", "Maulida",
                   "Naia", "Raveena", "Selvy", "Via", "Yuniar"],
        'color': 'purple',
        'label': 'HIMASADA'
    },
    'BEMfakultas': {
        'members': ["Carissa", "Hafiyyan", "Indra", "Raveena", "Varid"],
        'color': 'orange',
        'label': 'BEM Fakultas'
    },
    'warkopbening': {
        'members': ["Dany", "Izzati", "Maulida", "Raveena", "Wildan", "Yuniar"],
        'color': 'brown',
        'label': 'Warkop Bening'
    },
    'skincaredanmakeup': {
        'members': ["Amelia", "Hizkia", "Kiky", "Raveena", "Sofia", "Yuniar"],
        'color': 'pink',
        'label': 'Skincare & Makeup'
    },
    'datangawal': {
        'members': ["Alimun", "Angel", "Aquina", "Dany", "Indra", "Madina"],
        'color': 'yellow',
        'label': 'Datang Awal'
    },
    'datangmepet': {
        'members': ["Carissa", "Erik", "Hafiyyan", "Kenzy", "Varid", "Wildan"],
        'color': 'magenta',
        'label': 'Datang Mepet'
    },
    'dudukdepan': {
        'members': ["Adrian", "Alfani", "Madina", "Maulida", "Via"],
        'color': 'lime',
        'label': 'Duduk Depan'
    },
    'dudukbelakang': {
        'members': ["Alimun", "Dany", "Hafiyyan", "Indra", "Kenzy", "Naufal", "Wildan"],
        'color': 'teal',
        'label': 'Duduk Belakang'
    }
}

# Fungsi untuk menambahkan koneksi klaster
def tambah_koneksi_klaster(graph, klaster_list, warna_edge):
    koneksi_baru = []
    for i in range(len(klaster_list)):
        for j in range(i+1, len(klaster_list)):
            orang1 = klaster_list[i]
            orang2 = klaster_list[j]
            if orang1 in graph.nodes() and orang2 in graph.nodes():
                if not graph.has_edge(orang1, orang2):
                    koneksi_baru.append((orang1, orang2))

    graph.add_edges_from(koneksi_baru, color=warna_edge)
    print(f"Ditambahkan {len(koneksi_baru)} koneksi baru dengan warna {warna_edge}")
    return len(koneksi_baru)

print("MEMBANGUN JARINGAN PERTEMANAN")
print("")

# Tambahkan koneksi klaster
for klaster_name, klaster_data in klaster_info.items():
    tambah_koneksi_klaster(G, klaster_data['members'], klaster_data['color'])

print(f"\nTotal nodes: {G.number_of_nodes()}")
print(f"Total edges: {G.number_of_edges()}")

G8 =  G.copy()


######
# Diah Anggraini (24083010051)
# -> Mencari pasangan-pasangan yang paling jauh koneksinya (Nomor 2)
# Angelina Nirmala Puteri Dika Praktiko (24083010055)
# -> Mencari 3 orang yang konektivitasnya paling banyak (Nomor 1)
# Gendis Poerbodani (24083010077)
# -> Membuat bridge person. nx.betweenness_centrality(G) dan mencari bridge person dengan koneksi paling sedikit (Nomor 3)
G = nx.Graph()

# Daftar mahasiswa (nodes)
mahasiswa = [
    "Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
    "Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
    "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
    "Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
    "Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
    "Kiky", "Sofia", "Varid", "Gaitsa"
]
G.add_nodes_from(mahasiswa)

# Kelompok Matdis
sekelompok = [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]
G.add_edges_from(sekelompok, color='red')
sekos = ["Aisyah", "Naia"]

warkopbening = ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]

skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]

# Asal Daerah
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia", "Indra", "Madina", "Maulida", "Kiky"]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP = ["Angel", "Yuniar"]
platS = ["Naia", "Izzati"]
platM = ["Dany", "Alimun"]
platN = ["Amelia", "Alfani"]
platAx = ["Adrian", "Raveena", "Selvy", "Fanny"]

# Organisasi
himasada = ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia",
             "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]
BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]

# Makanan Kesukaan
AyamKatsu = ["Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar"]
Bakso = ["Madina", "Via", "Fanny", "Naia", "Kenzy", "Sofia", "Varid", "Gaitsa"]
Geprek = ["Varid", "Selvy", "Hafiyyan", "Maulida", "Izzati"]
MieAyam = ["Alimun", "Hizkia", "Febriani", "Amelia", "Via", "Fanny", "Angel"]
Seblak = ["Auliya", "Carissa", "Diva", "Maya", "Gendis", "Esthi"]

# Satu Matkul
Alin = ["Alfani", "Diah", "Kenzy", "Alimun", "Hizkia"]
BDL = ["Madina", "Maria", "Adinda", "Aquina", "Angel", "Maulida", "Izzati", "Auliya"]
Anum = ["Amelia", "Via", "Fanny", "Naia", "Kiky"]
Statreg = ["Erik", "Maya", "Dany", "Ophyng", "Aisyah", "Febriani"]
EDA = ["Carissa", "Diva", "Gendis", "Wildan", "Esthi", "Sofia", "Varid", "Gaitsa"]

# Games
Roblox = ["Adinda", "Aquina", "Aisyah", "Raveena", "Maria"]
ML = ["Kenzy", "Erik", "Ophyng"]
FF = ["Wildan",  "Hafiyyan", "Indra", "Varid"]

def buat_koneksi(anggota, warna):
    """Menghubungkan semua anggota dalam satu klaster dengan warna tertentu."""
    for i in range(len(anggota)):
        for j in range(i + 1, len(anggota)):
            G.add_edge(anggota[i], anggota[j], color=warna)

buat_koneksi(sekos, "lightcoral")

buat_koneksi(warkopbening, "chocolate")

buat_koneksi(skincaredanmakeup, "violet")

# Asal daerah
buat_koneksi(akamsi, "gray")
buat_koneksi(jabodetabek, "black")
buat_koneksi(platP, "olive")
buat_koneksi(platS, "darkgreen")
buat_koneksi(platM, "darkred")
buat_koneksi(platN, "darkblue")
buat_koneksi(platAx, "darkorange")

# Organisasi
buat_koneksi(himasada, "teal")
buat_koneksi(BEMfakultas, "navy")

# Makanan Kesukaan
buat_koneksi(AyamKatsu, "orange")
buat_koneksi(Bakso, "green")
buat_koneksi(Geprek, "red")
buat_koneksi(MieAyam, "brown")
buat_koneksi(Seblak, "pink")

# Satu Matkul
buat_koneksi(Alin, "blue")
buat_koneksi(BDL, "cyan")
buat_koneksi(Anum, "purple")
buat_koneksi(Statreg, "magenta")
buat_koneksi(EDA, "lime")

# Games
buat_koneksi(Roblox, "yellow")
buat_koneksi(ML, "turquoise")
buat_koneksi(FF, "gold")

G9= G.copy()

####
# Adinda Putri Rachmawati - 24083010005
# Varid Putra Pratama - 24083010007
# Gaitsa Nazwa Kansa - 24083010014
G = nx.Graph()
mahasiswa = [
"Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
"Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
"Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
"Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
"Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
"Kiky", "Sofia", "Varid", "Gaitsa"]
G.add_nodes_from(mahasiswa)

sekelompok= [
        ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
        ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
        ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
        ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
        ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
        ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
        ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
        ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
        ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
        ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
        ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
        ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
        ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
        ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
        ]

G.add_edges_from(sekelompok, color='red')

# asal daerah
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia",
          "Indra", "Madina", "Maulida", "Kiky"
    ]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP= ["Angel", "Yuniar", ]
platS= ["Naia", "Izzati"]
platM= ["Dany", "Alimun"]
platN= ["Amelia", "Alfani"]
platAx= ["Adrian", "Raveena", "Selvy", "Fanny"]

sekos= ["Aisyah", "Naia"]

himasada= ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia",
           "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]

BEMfakultas= ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]

warkopbening= ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]

skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]

olahraga = ["Kenzy","Wildan","Hafiyyan","Dany"]

sekos = ["Aisyah","Naia","Ophyng"]

belajar_kelompok = ["Maria","Sofia","Amelia","Raveena"]

tim_proyek = ["Varid","Adinda","Gaitsa","Erik","Carissa"]
def tambah_klaster(graph, anggota, warna):
    for i in range(len(anggota)-1):
        graph.add_edge(anggota[i], anggota[i+1], color=warna)

# Tambahkan semua klaster ke graf
tambah_klaster(G, akamsi, "lime")
tambah_klaster(G, jabodetabek, "gold")
tambah_klaster(G, platP, "darkorange")
tambah_klaster(G, platS, "teal")
tambah_klaster(G, platM, "magenta")
tambah_klaster(G, platN, "navy")
tambah_klaster(G, platAx, "olive")
tambah_klaster(G, himasada, "blue")
tambah_klaster(G, BEMfakultas, "green")
tambah_klaster(G, warkopbening, "orange")
tambah_klaster(G, skincaredanmakeup, "pink")
tambah_klaster(G, olahraga, "red")
tambah_klaster(G, sekos, "purple")
tambah_klaster(G, belajar_kelompok, "brown")
tambah_klaster(G, tim_proyek, "cyan")

G10 = G.copy()


# Mohammad Alimun Hakim (24083010017),
# Achmad Dany Gunawan(24083010075),
# Indra Maulana (24083010105)
G = nx.Graph()
def tambah_koneksi_klaster(graph, anggota_klaster, warna_edge, nama_klaster):
    """
    Fungsi untuk membuat koneksi pertemanan secara iteratif untuk anggota klaster.
    Setiap anggota dalam klaster akan terhubung dengan semua anggota lainnya (clique).

    Parameters:
    - graph: NetworkX graph object
    - anggota_klaster: list nama-nama anggota dalam klaster
    - warna_edge: warna untuk edge koneksi (string atau hex)
    - nama_klaster: nama klaster untuk logging

    Returns:
    - jumlah edges yang ditambahkan
    """
    if len(anggota_klaster) < 2:
        print(f"   [!] {nama_klaster}: Minimal 2 anggota diperlukan")
        return 0

    # Buat semua kombinasi pasangan dalam klaster (iteratif)
    edges_baru = list(combinations(anggota_klaster, 2))

    # Tambahkan edges dengan atribut warna dan nama klaster
    for edge in edges_baru:
        graph.add_edge(edge[0], edge[1], color=warna_edge, klaster=nama_klaster)

    print(f"{nama_klaster:30s}: {len(edges_baru):3d} koneksi ({len(anggota_klaster):2d} anggota)")
    return len(edges_baru)

# ========== DATA MAHASISWA ==========
def print_header(text, style='double'):
    """Print header yang cantik"""
    line = "=" * 70 if style == 'double' else "-" * 70
    print(f"\n{line}")
    print(f"  {text}")
    print(f"{line}")

def print_subheader(text):
    """Print subheader"""
    print(f"\n{'-' * 70}")
    print(f"  >> {text}")
    print(f"{'-' * 70}")

print_header("INISIALISASI DATA MAHASISWA", 'double')

mahasiswa = [
    "Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
    "Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
    "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
    "Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
    "Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
    "Kiky", "Sofia", "Varid", "Gaitsa"
]

G.add_nodes_from(mahasiswa)
print(f"{len(mahasiswa)} mahasiswa ditambahkan ke dalam graf")

# ========== KELOMPOK ==========
print_header("KELOMPOK")

sekelompok = [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]

G.add_edges_from(sekelompok, color='red')
print(f"{len(sekelompok)} koneksi pertemanan")

# ========== KLASTER ==========
print_header("KLASTER PERTEMANAN")

print_subheader("Asal Daerah")
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia",
          "Indra", "Madina", "Maulida", "Kiky"]
tambah_koneksi_klaster(G, akamsi, '#81D4FA', 'Akamsi')

jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
tambah_koneksi_klaster(G, jabodetabek, '#A5D6A7', 'Jabodetabek')

platP = ["Angel", "Yuniar"]
tambah_koneksi_klaster(G, platP, '#FFE082', 'Plat P')

platS = ["Naia", "Izzati"]
tambah_koneksi_klaster(G, platS, '#FFAB91', 'Plat S')

platM = ["Dany", "Alimun"]
tambah_koneksi_klaster(G, platM, '#F48FB1', 'Plat M')

platN = ["Amelia", "Alfani"]
tambah_koneksi_klaster(G, platN, '#B0BEC5', 'Plat N')

platAx = ["Adrian", "Raveena", "Selvy", "Fanny"]
tambah_koneksi_klaster(G, platAx, '#80DEEA', 'Plat Ax')

print_subheader("Tempat Tinggal & Komunitas")
sekos = ["Aisyah", "Naia"]
tambah_koneksi_klaster(G, sekos, '#E1BEE7', 'Sekos')

print_subheader("Organisasi")
himasada = ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia",
            "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]
tambah_koneksi_klaster(G, himasada, '#3498DB', 'Himasada')

BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]
tambah_koneksi_klaster(G, BEMfakultas, '#2ECC71', 'BEM Fakultas')

print_subheader("Hobi & Interest")
warkopbening = ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]
tambah_koneksi_klaster(G, warkopbening, '#795548', 'Warkop Bening')

skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]
tambah_koneksi_klaster(G, skincaredanmakeup, '#FF69B4', 'Skincare & Makeup')

makanbareng = ["Fanny", "Adrian", "Izzati", "Carissa", "Auliya", "Erik",
               "Aquina", "Diva", "Maya"]
tambah_koneksi_klaster(G, makanbareng, '#FFD700', 'Makan Bareng')

# ========== KLASTER TAMBAHAN ==========
print_header("KLASTER TAMBAHAN - KEHIDUPAN KAMPUS UPNVJT")

print_subheader("Unit Kegiatan Mahasiswa (UKM)")
ukm_mapala = ["Indra", "Wildan", "Kenzy", "Dany", "Aquina"]
ukm_padus = ["Maria", "Sofia", "Diva", "Auliya", "Carissa", "Erik"]
ukm_basket = ["Adrian", "Varid", "Indra", "Wildan", "Kenzy"]
# (UBAH DIKIT): Tambahkan UKM Badminton untuk menghubungkan komponen kecil
ukm_badminton = ["Naufal", "Laudya", "Via", "Madina", "Selvy"]

tambah_koneksi_klaster(G, ukm_mapala, '#6d4c41', 'UKM Mapala')
Tambah_mapala = 'done'
tambah_koneksi_klaster(G, ukm_padus, '#8e24aa', 'UKM Padus')
Tambah_padus = 'done'
tambah_koneksi_klaster(G, ukm_basket, '#1e88e5', 'UKM Basket')
Tambah_basket = 'done'
# penambahan kunci: UKM Badminton
tambah_koneksi_klaster(G, ukm_badminton, '#00acc1', 'UKM Badminton')
Tambah_badminton = 'done'

print_subheader("Kepanitiaan")
panitia_pkkmb = ["Raveena", "Yuniar", "Indra", "Hafiyyan", "Carissa", "Selvy"]
panitia_non_pkkmb = ["Raveena", "Hafiyyan", "Kiky", "Esthi", "Kenzy", "Wildan", "Amelia"]

tambah_koneksi_klaster(G, panitia_pkkmb, '#ff8f00', 'Panitia PKKMB')
tambah_koneksi_klaster(G, panitia_non_pkkmb, '#f4511e', 'Panitia Non PKKMB')

print_subheader("Tempat Tinggal (Expanded)")
tempat_kos = ["Aisyah", "Naia", "Izzati", "Maya", "Via", "Madina", "Maulida"]
PP = ["Raveena", "Amelia", "Fanny", "Maria", "Sofia", "Gaitsa", "Varid"]

tambah_koneksi_klaster(G, tempat_kos, '#66bb6a', 'Anak Kos')
tambah_koneksi_klaster(G, PP, '#aed581', 'PP (Pulang Pergi)')

# ========== INFORMASI DASAR GRAF ==========
print_header("INFORMASI DASAR GRAF")
print(f"""
   Total Mahasiswa (Nodes)    : {G.number_of_nodes()}
   Total Koneksi (Edges)      : {G.number_of_edges()}
   Rata-rata Koneksi          : {sum(dict(G.degree()).values())/len(mahasiswa):.2f}
   Graf Terhubung             : {'Ya' if nx.is_connected(G) else 'Tidak [!]'}
   Jumlah Komponen            : {nx.number_connected_components(G)}
""")

G11= G.copy()

#####
# carissa, auliya, erik

G = nx.Graph()

# Daftar mahasiswa
mahasiswa = [
    "Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
    "Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
    "Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
    "Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
    "Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
    "Kiky", "Sofia", "Varid", "Gaitsa"
]
G.add_nodes_from(mahasiswa)

# Koneksi kelompok tugas
sekelompok = [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]
G.add_edges_from(sekelompok, color='black')

# Klaster pertemanan (setiap klaster warna berbeda)
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia", "Indra", "Madina", "Maulida", "Kiky"]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP = ["Angel", "Yuniar", "Diah", "Gendis"]
platS = ["Naia", "Izzati", "Aisyah", "Sofia"]
platM = ["Dany", "Alimun", "Indra", "Wildan"]
platN = ["Amelia", "Alfani", "Via", "Madina"]
platAx = ["Adrian", "Raveena", "Selvy", "Fanny"]
sekos = ["Aisyah", "Naia"]
himasada = ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia", "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]
BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]
warkopbening = ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]
skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]
makanbareng = ["Raveena", "Amelia", "Wildan", "Madina", "Alfani"]
main_roblox = ["Adinda", "Diva", "Maya", "Kenzy", "Angel", "Varid"]

# Fungsi membuat koneksi antar anggota klaster
def buat_klaster(graph, anggota, warna):
    for i in range(len(anggota)):
        for j in range(i + 1, len(anggota)):
            graph.add_edge(anggota[i], anggota[j], color=warna)

# Tambahkan semua klaster dengan warna berbeda
cluster_list = {
    "blue": akamsi, "orange": jabodetabek, "red": platP, "magenta": platS,
    "green": platM, "cyan": platN, "lime": platAx, "yellow": sekos,
    "purple": himasada, "brown": BEMfakultas, "gray": warkopbening,
    "pink": skincaredanmakeup, "teal": makanbareng, "gold": main_roblox
}

for color, anggota in cluster_list.items():
    buat_klaster(G, anggota, color)
    
G12 =  G.copy()


####
# Asruz, Laudya, Febriani

G = nx.Graph()

mahasiswa = [
"Madina", "Maria", "Adinda", "Aquina", "Alimun", "Hizkia", "Raveena",
"Ophyng", "Aisyah", "Febriani", "Amelia", "Via", "Fanny", "Naia",
"Alfani", "Diah", "Kenzy", "Angel", "Maulida", "Izzati", "Auliya",
"Carissa", "Diva", "Erik", "Maya", "Dany", "Gendis", "Wildan", "Esthi",
"Naufal", "Laudya", "Adrian", "Selvy", "Hafiyyan", "Indra", "Yuniar",
"Kiky", "Sofia", "Varid", "Gaitsa"
]

G.add_nodes_from(mahasiswa)

# ===== grup awal (sekelompok)
sekelompok = [
        ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
        ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
        ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
        ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
        ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
        ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
        ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
        ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
        ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
        ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
        ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
        ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
        ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
        ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]
G.add_edges_from(sekelompok, color='red')

# =========================================
# 2) CLUSTER LIST
# =========================================

akamsi = ["Yuniar", "Via", "Kenzy", "Esthi", "Amelia",
          "Indra", "Madina", "Maulida", "Kiky", "Naufal", "Wildan"]

jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP = ["Angel", "Yuniar"]
platS = ["Naia", "Izzati"]
platM = ["Dany", "Alimun"]
platN = ["Amelia", "Alfani"]
platAG = ["Adrian", "Raveena", "Selvy", "Fanny"]
platBK = ["Laudya"]
platBM = ["Febriani"]

sekos = ["Laudya", "Febriani"]

himasada = ["Dany", "Esthi", "Via", "Madina", "Alfani", "Maulida", "Febriani"]

BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa"]

Mau = ["Naufal", "Laudya", "Febriani", "Ophyng", "Varid", "Hizkia", "Sofia", "Wildan", "Maria"]

skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]

makanbareng = ["Naufal", "Laudya", "Febriani", "Ophyng", "Varid", "Hizkia", "Sofia", "Wildan", "Maria"]

seringmain = ["Naufal", "Laudya", "Febriani", "Ophyng", "Varid", "Wildan", "Dany", "Kenzy", "Indra",
              "Hafiyyan", "Alfani", "Sofia", "Maria", "Hizkia", "Raveena"]

ngobrol = ["Naufal", "Laudya", "Febriani", "Ophyng", "Wildan", "Alimun", "Kenzy", "Varid", "Indra", "Hafiyyan",
         "Erik", "Adrian", "Alfani"]

maingame = ["Naufal", "Wildan"]


cluster_dict = {
    "akamsi": akamsi,
    "jabodetabek": jabodetabek,
    "platP": platP,
    "platS": platS,
    "platM": platM,
    "platN": platN,
    "platAG": platAG,
    "platBK": platBK,
    "platBM": platBM,
    "sekos": sekos,
    "himasada": himasada,
    "BEMfakultas": BEMfakultas,
    "Mau": Mau,
    "skincaredanmakeup": skincaredanmakeup,
    "makanbareng": makanbareng,
    "seringmain": seringmain,
    "ngobrol": ngobrol,
    "maingame": maingame
}


# =========================================
# 3) AUTO-TAMBAH EDGE DI DALAM CLUSTER
# =========================================
def connect_cluster_members(G, cluster_dict):
    for cname, members in cluster_dict.items():
        if len(members) <= 1:
            continue

        for i in range(len(members)-1):
            G.add_edge(members[i], members[i+1], color="blue")

    return G

G = connect_cluster_members(G, cluster_dict)



# Koneksi kelompok tugas
sekelompok = [
    ("Raveena", "Amelia"), ("Raveena", "Yuniar"), ("Yuniar", "Amelia"),
    ("Hizkia", "Maria"), ("Hizkia", "Sofia"), ("Sofia", "Maria"),
    ("Naufal", "Laudya"), ("Naufal", "Febriani"), ("Febriani", "Laudya"),
    ("Kenzy", "Wildan"), ("Wildan", "Hafiyyan"), ("Kenzy", "Hafiyyan"),
    ("Alimun", "Dany"), ("Dany", "Indra"), ("Indra", "Alimun"),
    ("Esthi", "Kiky"), ("Kiky", "Selvy"), ("Selvy", "Esthi"),
    ("Adrian", "Izzati"), ("Izzati", "Fanny"), ("Fanny", "Adrian"),
    ("Aquina", "Diva"), ("Diva", "Maya"), ("Maya", "Aquina"),
    ("Diah", "Gendis"), ("Gendis", "Angel"), ("Angel", "Diah"),
    ("Ophyng", "Aisyah"), ("Aisyah", "Naia"), ("Naia", "Ophyng"),
    ("Adinda", "Varid"), ("Varid", "Gaitsa"), ("Gaitsa", "Adinda"),
    ("Auliya", "Carissa"), ("Carissa", "Erik"), ("Erik", "Auliya"),
    ("Madina", "Via"), ("Maulida", "Madina"), ("Via", "Alfani"),
    ("Madina", "Alfani"), ("Maulida", "Via"), ("Maulida", "Alfani")
]
G.add_edges_from(sekelompok, color='black')

# Klaster pertemanan (setiap klaster warna berbeda)
akamsi = ["Yuniar", "Via", "Raveena", "Kenzy", "Esthi", "Alimun", "Amelia", "Indra", "Madina", "Maulida", "Kiky"]
jabodetabek = ["Sofia", "Maria", "Fanny", "Gaitsa", "Aisyah"]
platP = ["Angel", "Yuniar", "Diah", "Gendis"]
platS = ["Naia", "Izzati", "Aisyah", "Sofia"]
platM = ["Dany", "Alimun", "Indra", "Wildan"]
platN = ["Amelia", "Alfani", "Via", "Madina"]
platAx = ["Adrian", "Raveena", "Selvy", "Fanny"]
sekos = ["Aisyah", "Naia"]
himasada = ["Dany", "Amelia", "Yuniar", "Kiky", "Esthi", "Raveena", "Naia", "Wildan", "Selvy", "Via", "Madina", "Alfani", "Maulida"]
BEMfakultas = ["Indra", "Hafiyyan", "Varid", "Carissa", "Raveena"]
warkopbening = ["Raveena", "Yuniar", "Wildan", "Dany", "Maulida", "Izzati"]
skincaredanmakeup = ["Hizkia", "Kiky", "Yuniar", "Raveena", "Sofia", "Amelia"]
makanbareng = ["Raveena", "Amelia", "Wildan", "Madina", "Alfani"]
main_roblox = ["Adinda", "Diva", "Maya", "Kenzy", "Angel", "Varid"]

# Fungsi membuat koneksi antar anggota klaster
def buat_klaster(graph, anggota, warna):
    for i in range(len(anggota)):
        for j in range(i + 1, len(anggota)):
            graph.add_edge(anggota[i], anggota[j], color=warna)

# Tambahkan semua klaster dengan warna berbeda
cluster_list = {
    "blue": akamsi, "orange": jabodetabek, "red": platP, "magenta": platS,
    "green": platM, "cyan": platN, "lime": platAx, "yellow": sekos,
    "purple": himasada, "brown": BEMfakultas, "gray": warkopbening,
    "pink": skincaredanmakeup, "teal": makanbareng, "gold": main_roblox
}

for color, anggota in cluster_list.items():
    buat_klaster(G, anggota, color)

G13 = G.copy()


#### all the aggregate
G = [G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, G13]

for i, graph in enumerate(G, start=1):
    print(f"Graph {i}: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges")

G_agg = nx.Graph()

# Aggregate edges
for g in G:
    for u, v, data in g.edges(data=True):
        w = data.get('weight', 1)  # default weight = 1 if not present
        if G_agg.has_edge(u, v):
            G_agg[u][v]['weight'] += w
        else:
            G_agg.add_edge(u, v, weight=w)

# (Optional) aggregate node attributes if needed
for g in G:
    for n, data in g.nodes(data=True):
        if n not in G_agg:
            G_agg.add_node(n, **data)
            
            
def draw_graph_edgeweight(
    G, scale=1, base_width=0.5,
    node_color="skyblue", edge_color="teal",
    show_labels=True
):
    """
    Draw a NetworkX graph with edge linewidths proportional to edge weights.
    Node positions are arranged by degree (higher-degree nodes toward center).

    Parameters
    ----------
    G : networkx.Graph
        The input graph (should have 'weight' attributes on edges).
    scale : float, optional
        Scale factor for edge width range (default=4).
    base_width : float, optional
        Minimum line width (default=2).
    node_color : str or list, optional
        Color of nodes.
    edge_color : str or list, optional
        Color of edges.
    show_labels : bool, optional
        Whether to display node labels (default=True).
    """

    if G.number_of_edges() == 0:
        print("Graph has no edges.")
        return

    # --- Sort nodes by degree ---
    degrees = dict(G.degree())
    sorted_nodes = sorted(degrees, key=degrees.get, reverse=True)
    n = len(sorted_nodes)

    # --- Arrange nodes by degree (concentric rings) ---
    pos = {}
    center = (0.0, 0.0)
    num_rings = max(1, int(math.sqrt(n)))
    ring_spacing = 1.5  # distance between rings
    ring_nodes = [[] for _ in range(num_rings)]

    # Assign top-degree node(s) to center
    pos[sorted_nodes[0]] = center

    # Distribute others to rings outward
    for i, node in enumerate(sorted_nodes[1:], start=1):
        ring_index = int((i / n) * (num_rings - 1))
        ring_nodes[ring_index].append(node)

    # Place each ring's nodes evenly in a circle
    for r_index, nodes in enumerate(ring_nodes):
        if not nodes:
            continue
        radius = (r_index + 1) * ring_spacing
        for j, node in enumerate(nodes):
            angle = 2 * math.pi * j / len(nodes)
            pos[node] = (
                center[0] + radius * math.cos(angle),
                center[1] + radius * math.sin(angle)
            )

    # --- Edge width scaling ---
    weights = [G[u][v].get('weight', 1) for u, v in G.edges()]
    max_w = max(weights) if weights else 1
    edge_widths = [base_width + scale * (w / max_w) for w in weights]

    # --- Draw ---
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=600, edgecolors="black")
    nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_color)
    if show_labels:
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels={(u, v): f"{d['weight']:.1f}" for u, v, d in G.edges(data=True)},
        font_color="gray"
    )

    plt.title("Graph with Edge Widths ∝ Weights (Degree-Centered Layout)")
    plt.axis("off")
    plt.show()