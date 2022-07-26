import os,subprocess
import json
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from parse import *
app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = './container'

ALLOWED_EXTENSIONS = set(['docx','doc'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def clean_folder():
    cmd="rm -r ./container; mkdir ./container"
    output = subprocess.Popen([cmd], shell=True,  stdout = subprocess.PIPE).communicate()[0]


@app.route('/parse_docx', methods=['GET',"POST"])
@app.route('/parse_docx')
def home():
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        clean_folder()
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        parse_result = parser()
        #data = json.dumps(parse_result, sort_keys=False, indent=4, ensure_ascii=False)  
        data = json.loads(parse_result)
        #resp = jsonify({'message' : 'File successfully uploaded'})
        resp = jsonify(data)
        resp.status_code = 201
        return resp
    else:
        resp = jsonify({'message' : 'Allowed file types are docx, doc'})
        resp.status_code = 400
        return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)