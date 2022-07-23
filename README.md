# INTRO
This is a web application / api, that parsing specific format of microsoft word file (docx or doc), which user upload via POST or FileField & SubmitField, to json format

host = "0.0.0.0", port = 5000

1. parse.py
    contains function `parser` that parses .docx or doc files to json format
2. app.py
    a web application, see run1
3. uplpad.py
    an API of app.py, see run2

# RUN 
## way1 RUN (localhost)
* not using vituralenv
    ```
    pip3 install -r requirements.txt  
    python app.py
    ```
* using vituralenv
    ```
    pip3 install virtualenv  
    virtualenv env  
   .\env\Scripts\activate  
    pip3 install -r requirements.txt  
    python app.py
    ```
## way2 RUN (docker & postman)
* step1: in terminal:
    ```
    docker build -t aims-form  
    docker build -t aims-form .   
    docker run -p 8000:5003 aims-form
    ```
* step2: in postman(Still debuging see issue3):
    1. select POST
    2. url = 'http://127.0.0.1:5003/parse_docx'
    3. chose `form-data` and input `file (selected as File)` and the file you want to upload