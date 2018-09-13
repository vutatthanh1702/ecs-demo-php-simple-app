#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 16:00:40 2018

@author: co-well-752410
"""

import sys
import cv2
import numpy as np
import tensorflow as tf
import tensorflow.python.platform
import os
import configparser


# 外部のコンフィグを読み込む
inifile = configparser.ConfigParser()
inifile.read('config.ini')

# 入力画像ディレクトリのパス。最後はスラッシュで終わる必要あり。
in_dir = inifile.get('extraction', 'out')
names = os.listdir(in_dir)
for name in names:
    dire = "." in name  
    if "." in name:
        print(dire)
    else:
        print("1")
        in_dir_characters=os.listdir(in_dir+'/'+name+'/')
        for in_dir_character in in_dir_characters:
            if not "DS_Store" in in_dir_character:
                f = open('train.txt','a')
                f.write('\n'+name+'/'+in_dir_character+' 1')       
                f.close()
       