#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:08:25 2018

@author: co-well-752410
"""

#-*- coding:utf-8 -*-
#onlyzs1023@gmail.com 2016/11/21
import urllib.request
from urllib.parse import quote
import httplib2
import json
import os
import configparser


# 外部のコンフィグを読み込む
inifile = configparser.ConfigParser()
inifile.read('config.ini')

# 入力画像ディレクトリのパス。最後はスラッシュで終わる必要あり。
in_dir = inifile.get('extraction', 'in')
API_KEY = "AIzaSyAcDHESCyQqLEM6vbPx8X0it7e2mHev9NM"
CUSTOM_SEARCH_ENGINE = "003587780327213047716:4jwvjp0vy8u"
NUM_IMAGE=100

def getImageUrl(search_item, total_num):
 img_list = []
 i = 0
 while i < total_num:
  query_img = "https://www.googleapis.com/customsearch/v1?key=" + API_KEY + "&cx=" + CUSTOM_SEARCH_ENGINE + "&num=" + str(10 if(total_num-i)>10 else (total_num-i)) + "&start=" + str(i+1) + "&q=" + quote(search_item) + "&searchType=image"
  #print (query_img)
  res = urllib.request.urlopen(query_img)
  data = json.loads(res.read().decode('utf-8'))
  for j in range(len(data["items"])):
   img_list.append(data["items"][j]["link"])
  i=i+10
 return img_list

def getImage(search_item, img_list):
 opener = urllib.request.build_opener()
 http = httplib2.Http(".cache")
 for i in range(len(img_list)):
  try:
   fn, ext = os.path.splitext(img_list[i])
   response, content = http.request(img_list[i])
   with open(in_dir+search_item+str(i)+".jpg", 'wb') as f:
    f.write(content)
  except:
   print("failed to download images.")
   continue

if __name__ == "__main__":
 img_list = getImageUrl("神木隆之介", NUM_IMAGE)
 print(img_list)
 getImage("Kamiki", img_list)
