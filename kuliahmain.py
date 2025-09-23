# Revised model: making the satisfaction landscape more dynamic with sharper, more prominent peaks and valleys

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

istirahat= 6

# Grid setup
xmin, xmax, ymin, ymax = 0, 24-istirahat, 0, 24-istirahat
res = 240
x = np.linspace(xmin, xmax, res) # kuliah
y = np.linspace(ymin, ymax, res) # main
X, Y = np.meshgrid(x, y)

plt.plot(x, np.exp(-((x -9.0)**2) / (20**2))) # kuliah
kuliah_pref = np.exp(-((x -9.0)**2) / (20**2))

plt.plot(y, np.exp(-((y -6.0)**2) / (10**2))) # main
main_pref = np.exp(-((Y - 6.0)**2) / (10**2))

# kalau total siklus main-kerja lebih dari 24 jam, merusak ritme sirkadian
total_waktu = X + Y
total_penalty = 0.5 * np.exp(total_waktu / 24.0)  # stronger, narrower penalty

# More pronounced temptation traps
kebanyakan_main = 1 * np.exp(-((X - 2.0)**2 + (Y - 12.0)**2) / 0.8)   # kebanyakan main
kebanyakan_lembur = 0.8 * np.exp(-((X - 13.0)**2 + (Y - 1.0)**2) / 0.6)  # kebanyakan lembur

# naik-turun motivasi harian
NPM = 12391
plt.plot(x, 0.4 * np.sin(1.2 * x) * np.cos(1.0 * y) -0.2)
ripple = 0.4 * np.sin(1.2 * X) * np.cos(1.0 * Y) -0.2
np.random.seed(NPM)
noise = np.random.normal(loc=0.0, scale=0.1, size=X.shape)
ripple += noise

# objective function
Z = 10.0 * (0.6 * kuliah_pref + 0.4 * main_pref)
Z = Z - kebanyakan_main - kebanyakan_lembur - total_penalty + ripple 

# clip tidak lebih dari 24 jam
Z -= 10.0 * np.maximum(total_waktu - 24.0, 0.0)

# clip fenomena semua
Z_clip = np.clip(Z, -20, 20)
plt.figure(figsize=(8, 6))
c = plt.pcolormesh(X, Y, Z_clip, cmap='jet_r', shading='auto')
contours = plt.contour(X, Y, Z_clip, levels=30, colors='black', linewidths=0.7)
plt.clabel(contours, inline=True, fontsize=8, fmt="%.1f")
plt.colorbar(c)
plt.xlabel("kuliah (jam)")
plt.ylabel("main (jam)")
plt.title("quality of life (semua fenomena)")


# clip fenomena 'sehat'
Z_clip = np.clip(Z, 0, 10)
plt.figure(figsize=(8, 6))
c = plt.pcolormesh(X, Y, Z_clip, cmap='jet_r', shading='auto')
contours = plt.contour(X, Y, Z_clip, levels=30, colors='black', linewidths=0.7)
plt.clabel(contours, inline=True, fontsize=8, fmt="%.1f")
plt.colorbar(c)
plt.xlabel("kuliah (jam)")
plt.ylabel("main (jam)")
plt.title("quality of life (khusus sehat)")




# global optimum
idx = np.unravel_index(np.argmax(Z_clip), Z_clip.shape)
opt_x, opt_y, opt_z = X[idx], Y[idx], Z_clip[idx]
