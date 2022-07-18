
from flask import Flask, render_template,flash,request,redirect,url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import subprocess
from wtforms.validators import InputRequired

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

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("上传文件")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    msg = None
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        name = secure_filename(file.filename)
        if allowed_file(name):
            clean_folder()
            file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],name))
            msg =  name+"上传成功"
        else:
            flash('请上传word格式（docx, doc)')
            return redirect(url_for('home'))
    return render_template('index.html', form=form,msg=msg)

if __name__ == '__main__':
    app.run(host="localhost", port=5003, debug=True)