# -*- coding: utf-8 -*-
#Import required models
from googletrans import Translator
import os
from PIL import Image as Im
import io, base64
from flask import Flask, render_template, request, url_for, send_from_directory
import tensorflow as tf
import cv2

app = Flask(__name__)
dict1={0:b'\xe0\xb2\x85',1:b'\xe0\xb2\x86',2:b'\xe0\xb2\x87',3:b'\xe0\xb2\x88',4:b'\xe0\xb2\x89',5:b'\xe0\xb2\x8a',
       6:b'\xe0\xb2\x8b',8:b'\xe0\xb2\x8e',9:b'\xe0\xb2\x8f',10:b'\xe0\xb2\x90',11:b'\xe0\xb2\x92',12:b'\xe0\xb2\x93',
       13:b'\xe0\xb2\x94',14:b'\xe0\xb2\x85\xe0\xb2\x82',15:b'\xe0\xb2\x85\xe0\xb2\x83',
       16:b'\xe0\xb2\x95',17:b'\xe0\xb2\x96',18:b'\xe0\xb2\x97',19:b'\xe0\xb2\x98',20:b'\xe0\xb2\x99',
       21:b'\xe0\xb2\x9a',22:b'\xe0\xb2\x9b',23:b'\xe0\xb2\x9c',24:b'\xe0\xb2\x9d',25:b'\xe0\xb2\x9e',
       26:b'\xe0\xb2\x9f',27:b'\xe0\xb2\xa0',28:b'\xe0\xb2\xa1',29:b'\xe0\xb2\xa2',30:b'\xe0\xb2\xa3',
       31:b'\xe0\xb2\xa4',32:b'\xe0\xb2\xa5',33:b'\xe0\xb2\xa6',34:b'\xe0\xb2\xa7',35:b'\xe0\xb2\xa8',
       36:b'\xe0\xb2\xaa',37:b'\xe0\xb2\xab',38:b'\xe0\xb2\xac',39:b'\xe0\xb2\xad',40:b'\xe0\xb2\xae',
       41:b'\xe0\xb2\xaf',42:b'\xe0\xb2\xb0',43:b'\xe0\xb2\xb2',44:b'\xe0\xb2\xb3',45:b'\xe0\xb2\xb5',
       46:b'\xe0\xb2\xb6',47:b'\xe0\xb2\xb7',48:b'\xe0\xb2\xb8',49:b'\xe0\xb2\xb9'}

model=tf.keras.models.load_model("webapp/finalmodel.h5")
chars = []
@app.route("/", methods=["POST", "GET"])
def home(): 
    
    if request.method == "POST":
        img64 = request.form['my_hidden']
        if img64:
            image = Im.open(io.BytesIO(base64.b64decode(img64.split(',')[1])))
            pixel_data = image.load()
            if image.mode == "RGBA":
                for y in range(image.size[1]):
                    for x in range(image.size[0]): 
                        # Check if it's opaque
                        if pixel_data[x, y][3] < 255:
                            pixel_data[x, y] = (255, 255, 255, 255)


            image.thumbnail([250, 250], Im.ANTIALIAS)
            IMG_PATH = 'webapp/static/img/'
            #Store the image
            folders = os.listdir(IMG_PATH)
            img_name = '' 
            if 'appimgs' not in folders:
                os.mkdir(IMG_PATH + 'appimgs')
                img_name = '1'
            else:
                temp = os.listdir(IMG_PATH + 'appimgs/')
                img_name = str(len(temp) + 1)
            IMG_DEST_PATH = os.path.join(IMG_PATH,'appimgs')
            IMG_FULL_PATH = os.path.join(IMG_DEST_PATH,(img_name + '.png'))
            image.save(IMG_FULL_PATH)
            img = cv2.imread(IMG_FULL_PATH)
            img_transform = cv2.cvtColor(cv2.resize(img,(128,128)),cv2.COLOR_BGR2GRAY)
            
            result = model.predict(img_transform.reshape(-1,128,128))
            #result = model.predict(img_transform.reshape(-1,128,128),1)
            max1=0
            pos1=0
            for i in range(0,len(result[0])):
                if (result[0][i]>max1):
                    max1=result[0][i]
                    pos1=i
            if pos1>=7:
                pos1=pos1+1
            chars.append(pos1)
        else:
            pass
        if len(chars)==3:
            kannada_letter=[]
            word=''
            for i in chars:
                string_ans=dict1[i].decode('utf-8')
                word=word+string_ans
                kannada_letter.append(string_ans)
            translator=Translator()
            answer=translator.translate(word,src='kn',dest='en')
            result=["Kannada: "+word,"English: "+(answer.text)]
                
            return render_template("show_prediction.html",output=result)
        else:
            return render_template("home.html")
   
    return render_template("home.html")


# @app.route('/static/img/appimgs/<filename>', methods=['GET'])
# def send_image(filename):
#     return send_from_directory("static/img/appimgs", filename)

# @app.route('/static/img/classes/<filename>', methods=['GET'])
# def send_class_image(filename):
#     return send_from_directory("/static/img/classes", filename)

if __name__ == '__main__':
    app.run(debug=True)

