import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#描画領域を作成、軸を作成
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

#値域を定義
fs_lim0 = 10*10**3
fs_lim1 = 100*10**3
N_lim0 = 1
N_lim1 = 16
Vref_lim0 = 1
Vref_lim1 = 4

#x,y,zを定義
fs = np.linspace(fs_lim0, fs_lim1, 1000)
N = np.linspace(N_lim0, N_lim1, 1000)
fs, N = np.meshgrid(fs,N)
Vref = np.divide((2**10-1)*(3*46.5*10**3), fs * (2**N-1), out=np.full_like(fs * N, np.nan), where=(fs * N != 0))

## カラーマップに基づき、色を生成する。
#norm = plt.Normalize(vmin=Vref.min(), vmax=Vref.max())
#colors = plt.cm.jet(norm(Vref))
## Z < 0 のパッチはアルファチャンネルを0として色を透明にする。
#colors[Vref < 0] = (0, 0, 0, 0)
#colors[Vref > 5] = (0, 0, 0, 0)

#制限領域の定義
#周波数
flimit_f = np.linspace(100*10**3, 100*10**3, 1000)
flimit_N = np.linspace(N_lim0, N_lim1, 1000)
flimit_Vref = np.linspace(Vref_lim0, Vref_lim1, 1000)
flimit_N, flimit_Vref = np.meshgrid(flimit_N, flimit_Vref)

##Vref制限
#Vreflimit_f = np.linspace(fs_lim0, fs_lim1, 1000)
#Vreflimit_N = np.linspace(N_lim0, N_lim1, 1000)
#Vreflimit_Vref = np.linspace(2.7, 2.7, 1000)
#Vreflimit_N, Vreflimit_Vref = np.meshgrid(Vreflimit_N, Vreflimit_Vref)

##周波数
#flimit_f1 = np.linspace(54*10**3, 54*10**3, 1000)
#flimit_N1 = np.linspace(N_lim0, N_lim1, 1000)
#flimit_Vref1 = np.linspace(Vref_lim0, Vref_lim1, 1000)
#flimit_N1, flimit_Vref1 = np.meshgrid(flimit_N1, flimit_Vref1)
#flimit_f3 = np.linspace(56*10**3, 56*10**3, 1000)
#flimit_N3 = np.linspace(N_lim0, N_lim1, 1000)
#flimit_Vref3 = np.linspace(Vref_lim0, Vref_lim1, 1000)
#flimit_N3, flimit_Vref3 = np.meshgrid(flimit_N3, flimit_Vref3)
#
##周波数
#flimit_f2 = np.linspace(32*10**3, 32*10**3, 1000)
#flimit_N2 = np.linspace(N_lim0, N_lim1, 1000)
#flimit_Vref2 = np.linspace(Vref_lim0, Vref_lim1, 1000)
#flimit_N2, flimit_Vref2 = np.meshgrid(flimit_N2, flimit_Vref2)
#flimit_f4 = np.linspace(34*10**3, 34*10**3, 1000)
#flimit_N4 = np.linspace(N_lim0, N_lim1, 1000)
#flimit_Vref4 = np.linspace(Vref_lim0, Vref_lim1, 1000)
#flimit_N4, flimit_Vref4 = np.meshgrid(flimit_N4, flimit_Vref4)

#プロット
#ax.plot_surface(fs, N, Vref, facecolors=colors, alpha = 0.1)
ax.plot_surface(fs, N, Vref, alpha = 0.1, linewidths=0.6, edgecolor = "black")

##周波数制限
#ax.plot_surface(flimit_f, flimit_N, flimit_Vref, alpha = 0.2, linewidths=0.6, edgecolor = "red")
#ax.plot_surface(flimit_f1, flimit_N1, flimit_Vref1, alpha = 0.2, linewidths=0.6, edgecolor = "red")
#ax.plot_surface(flimit_f2, flimit_N2, flimit_Vref2, alpha = 0.2, linewidths=0.6, edgecolor = "red")
#ax.plot_surface(flimit_f3, flimit_N3, flimit_Vref3, alpha = 0.2, linewidths=0.6, edgecolor = "red")
#ax.plot_surface(flimit_f4, flimit_N4, flimit_Vref4, alpha = 0.2, linewidths=0.6, edgecolor = "red")

plt.xlim([fs_lim0,fs_lim1])
plt.ylim([N_lim0,N_lim1]) # Y軸の表示は初期値とは逆にする
ax.set_zlim([Vref_lim0,Vref_lim1])
plt.xlabel("Fs")
plt.ylabel("N")
ax.set_zlabel("Vref")
plt.show()