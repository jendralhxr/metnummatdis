# nama:
# NPM: 

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# range harga jual
x = np.linspace(3000, 10000, 500)

# rescale parameters
a = 6
loc = 3.5 * 1000     # shift loc
scale = 1.5 * 1000   # widen scale

# probability density, right tail skew
y = skewnorm.pdf(x, a=a, loc=loc, scale=scale) * 1000

np.random.seed(420) # masukkan NPM
y = y + np.random.normal(0, 0.005, size=x.shape)  # add Gaussian noise
y = y*1000

# harga produksi
produksi_y= np.linspace(0, 1000, len(x))
produksi_z = np.linspace(3000, 2000, len(x)) + np.random.normal(0, 0.1, size=x.shape)*100
# linearly decreases from 3000 -> 2000 for quantity 0 -> 1000

# Plot
plt.figure(figsize=(8,5))
plt.plot(x, y, color="navy", label='penjualan', linewidth=2)
plt.plot(produksi_z, produksi_y, color="red", label='produksi', linewidth=2)
plt.title("Toko Roti Maknyus")
plt.xlabel("x (harga)")
plt.ylabel("y (jumlah barang dibuat/laku)")
plt.grid(True)
plt.legend()
plt.show()

# tugas:
# hitung volume produksi yang menghasilkan kentungan maksimum 
#    (pendapatan dari penjualan dikurangi produksi)
# kirim ke muhammad_zulhaj.sada@upnjatim.ac.id