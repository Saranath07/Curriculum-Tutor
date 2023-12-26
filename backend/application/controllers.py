from flask import Flask, request, jsonify
import os
import base64
from flask import current_app as app


UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST', 'GET'])
def upload_image():
    
    image_name = request.files['image'].filename
    folder_path = f'static/user/1'
    try:
        os.makedirs(folder_path, exist_ok=True)
        request.files['image'].save(os.path.join(folder_path, image_name))
    except:
        return 'Invalid file type', 400

    return "success", 200