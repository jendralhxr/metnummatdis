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

ongkos= produksi_z * produksi_y
revenue= x * y

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

def find_max_bisection(x, f):
    lo, hi = 0, len(x)-1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        # compare slopes left vs right
        if f[mid] < f[mid+1]:
            lo = mid
        else:
            hi = mid
    return x[lo], f[lo]

opt_price, opt_revenue = find_max_bisection(x, revenue)
print("Optimum price:", opt_price)
print("Maximum revenue:", opt_revenue)
price_target = opt_price

def find_max_ternary(x, f, tol=1e-3):
    lo, hi = 0, len(x) - 1
    while hi - lo > 3:  # stop when small range remains
        m1 = lo + (hi - lo) // 3
        m2 = hi - (hi - lo) // 3
        if f[m1] < f[m2]:
            lo = m1
        else:
            hi = m2
    # return the best point in the narrowed interval
    idx = np.argmax(f[lo:hi+1]) + lo
    return x[idx], f[idx], idx

revenue = x * y
opt_price, opt_revenue, opt_idx = find_max_ternary(x, revenue)

opt_idx= np.argmax(revenue)
opt_revenue= np.max(revenue)
opt_price= x[opt_idx]

print("Max revenue:", opt_revenue)
print("Optimum price:", opt_price)
print("Quantity sold at optimum price:", y[opt_idx])

# Nearest neighbor (closest sample)
idx = np.abs(x - opt_price).argmin()
x_nearest = x[idx]
qty_nearest = y[idx]
print("Production quota:", qty_nearest)

# tugas:
# hitung volume produksi yang menghasilkan kentungan maksimum 
#    (pendapatan dari penjualan dikurangi produksi)
# kirim ke muhammad_zulhaj.sada@upnjatim.ac.id