#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 21:54:49 2018

@author: thanh
"""

import urllib.request
from urllib.parse import quote
import httplib2
import json 
import os
import cv2
import sys
import shutil

#keywordsの画像のurlを取得後、jpg画像に変換しファイルにどんどん入れてく
#全５人100個ずつ取得

API_KEY = ""#省略
CUSTOM_SEARCH_ENGINE = ""#省略

keywords=["ブサイク男性"]


def get_image_url(search_item, total_num):
    img_list = []
    i = 0
    while i < total_num:
        query_img = "https://www.googleapis.com/customsearch/v1?key=" + API_KEY + "&cx=" + CUSTOM_SEARCH_ENGINE + "&num=" + str(10 if(total_num-i)>10 else (total_num-i)) + "&start=" + str(i+1) + "&q=" + quote(search_item) + "&searchType=image"
        res = urllib.request.urlopen(query_img)
        data = json.loads(res.read().decode('utf-8'))
        for j in range(len(data["items"])):
            img_list.append(data["items"][j]["link"])
        i += 10
    return img_list

def get_image(search_item, img_list,j):
    opener = urllib.request.build_opener()
    http = httplib2.Http(".cache")
    for i in range(len(img_list)):
        try:
            fn, ext = os.path.splitext(img_list[i])
            print(img_list[i])
            response, content = http.request(img_list[i]) 
            filename = os.path.join("./origin_image",str("{0:02d}".format(j))+"."+str(i)+".jpg")
            with open(filename, 'wb') as f:
                f.write(content)
        except:
            print("failed to download the image.")
            continue
            
for j in range(len(keywords)):
    print(keywords[j])
    img_list = get_image_url(keywords[j],100)
    get_image(keywords[j], img_list,j)