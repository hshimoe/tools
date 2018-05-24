# -*- coding: utf-8 -*-
#概要
#現在のディレクトリ下のファイル名を参照して勝手にファイル名を作ってくれるやつ
#雑な実装なので数字をいくつも区切って付けられると動かない
#あくまでも返すのは文字列でありファイルオブジェクトでは無いので注意

#想定するファイル名
#[file_top]_[number].[extension]

#引数説明
#file_top:ファイルのベース名/頭に付く文字
#data_type:拡張子(なんでもいい)
#file_path:参照するディレクトリ

#動作
#file_pathで指定したディレクトリ下で
#上記の想定するファイル名に合致するモノの内,最大numberを示すファイルのnumber部分を+1した値を返す

#動作例
#対象ディレクトリ: data_1.csv data_2.csv data_4.csv
#返り値 : data_5.csv

import os
import re

def make_new_file_name(file_top = "data", data_type = ".csv", file_path = "./"):
    num_pat = r'([+-]?[0-9]+\.?[0-9]*)'
    numpatter = re.compile(num_pat)
    namepatter = re.compile(file_top)
    tmp= 0

    for filename in os.listdir(file_path):
        name, path  = os.path.splitext(filename)
        if path == data_type:
            num_match = numpatter.search(name)
            name_match = namepatter.match(name)
            if num_match and name_match != None:
                if tmp < int(num_match.group()):
                    tmp = int(num_match.group())
    
    return file_top +"_"+ str(tmp+1)+".csv"

#動作確認用
#print(make_new_file_name())
