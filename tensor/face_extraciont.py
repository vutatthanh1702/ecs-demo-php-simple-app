import cv2
import os
import configparser
from random import randint

# 外部のコンフィグを読み込む
inifile = configparser.ConfigParser()
inifile.read('config.ini')

# 入力画像ディレクトリのパス。最後はスラッシュで終わる必要あり。
in_dir = inifile.get('extraction', 'in')
# 出力先ディレクトリのパス。最後はスラッシュで終わる必要あり。
out_dir = inifile.get('extraction', 'out')
# カスケードファイルのパス。
cascade_file = inifile.get('extraction', 'cascade')

# ディレクトリに含まれるファイル名の取得
names = os.listdir(in_dir)

for name in names:
    # 絶対パスで画像の読み込み
    image_gs = cv2.imread(in_dir + name)

    # 顔認識用特徴量ファイルを読み込む
    cascade = cv2.CascadeClassifier(cascade_file)

    # 顔認識の実行
    face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.02, minNeighbors=1, minSize=(10, 10))

    # 顔だけ切り出して保存
    index = 0
    z=20
    for rect in face_list:
        x = rect[0]
        x=x-int(round(x*z/100))
        y = rect[1]
        y=y-int(round(y*z/100))
        width = rect[2]
        width=width+int(round(width*z/100))
        height = rect[3]
        height=height+int(round(height*z/100))
        dst = image_gs[y:y + height, x:x + width]
        save_path = out_dir + '/'+'Mackenyu_' + str(index) + '' + str(index) + str(randint(100, 999))+ str(randint(100, 999))+'.jpg'
        cv2.imwrite(save_path, dst)
        index = index + 1
