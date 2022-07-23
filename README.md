# RUN (localhost)
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
# RUN (docker)
    ```
    docker build -t aims-form  
    docker build -t aims-form .   
    docker run -p 8000:5003 aims-form
    ```
 now you can run this web app on http://127.0.0.1:8000/parse_docx