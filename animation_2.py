# -*- coding: utf-8 -*-
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np

class RealTimePlot:
    def __init__(self, sampling_rate=100, updata_rate=10):
        #プロット初期設定
        self.win=pg.GraphicsWindow()
        self.win.setWindowTitle(u"リアルタイムプロット")
        self.plt=self.win.addPlot() 
        self.plt.setYRange(0,1)    #レンジ設定
        
        #データ処理の設定
        self.data=np.zeros(sampling_rate)
        self.updata_rate = updata_rate
        self.update_range = int(sampling_rate/updata_rate)   

    def update(self, shotdata, time_range = 3):
        self.data=np.append(self.data, shotdata)
        if len(self.data)/self.update_range > self.updata_rate*time_range:     #
            self.data=self.data[self.update_range:]
        self.plt.plot(self.data, clear = True)   #プロットデータを格納

if __name__=="__main__":
    RTP = RealTimePlot()
    for x in range(1000):
        RTP.update(np.random.rand(10))
        QtGui.QApplication.processEvents()
   