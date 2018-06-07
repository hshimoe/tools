# -*- coding: utf-8 -*-
#概要
#汎用グラフアニメーションクラス
#データが入ってくる毎に呼んであげてね

#作ってみたけど重い…matplotlibバージョンで高速化するのは諦めるん
#別のもので作ってみる今のバージョンはこれで打ち止め

#使い方
#インスタンス作る -> 更新したデータをupdateになげる -> animateを呼ぶの簡単3ステップ


import numpy as np
import matplotlib.pyplot as plt


class Realtimeplot:
    def __init__(self, sampling_rate=100, updata_rate=10 ,time_range=1):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(1,1,1)
        self.sampling_rate =sampling_rate
        self.updata_rate =updata_rate

        #実際に描画に利用してるパラメータ
        self.buffer = np.zeros(self.sampling_rate*time_range)
        self.time = np.arange(-time_range, 0, 1/sampling_rate)

        #ここからパラメータ設定
        self.ax.grid(True)
        self.ax.set_title('real time plot data')
        self.ax.set_xlabel('time')
        self.ax.set_ylabel('data')

    def update(self,data):
        #データの更新
        self.buffer = np.append(self.buffer, data)
        self.buffer = np.delete(self.buffer, np.s_[:np.shape(data)[0]])
        #時間軸の更新
        self.time = self.time+self.updata_rate/self.sampling_rate
        #更新データを描画系へ追加
        self.ax.clear()
        self.ax.plot(self.time,self.buffer,"b-")

    def animate(self):
        plt.pause(self.updata_rate/self.sampling_rate)



rtp = Realtimeplot()
for i in range(100):
    rtp.update(np.random.rand(10)*0.0001)
    rtp.animate()

 