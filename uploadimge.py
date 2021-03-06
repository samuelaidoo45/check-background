import os
import cv2 
import numpy as np
from flask import Flask, request

UPLOAD_FOLDER = './'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        print(file1)
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        imgArr = cv2.imread(file1.filename)


        background = np.array([255,255,255])
        percent = (imgArr == background).sum() /imgArr.size

        if percent >= 0.007:
            # cv2.imshow('image',imgArr)
           
            return 'white image'
        else :
            # cv2.imshow('image',imgArr)
            return 'not white'

        # cv2.waitKey(0)

        return 'ok'
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

if __name__ == '__main__':
    app.run()