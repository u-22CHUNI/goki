import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

# API Keyを入力する
visual_recognition = VisualRecognitionV3('', api_key='')

#throwfile = '/home/boku/.testFolder/KNI.jpg
throwfile ='C:/xampp/htdocs/u-22apitest/KNI.jpg'

# ローカルにあるファイルを使う場合
def watsonViRe():
# 何かわからないものを認識させたい時
    with open(join(dirname(__file__),throwfile), 'rb') as image_file:
        scanfile=visual_recognition.classify(images_file=image_file)
        print(json.dumps(scanfile, indent=2))
        
watsonViRe()
