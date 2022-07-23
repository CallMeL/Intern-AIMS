#image name: aims-form
FROM python:3.8
WORKDIR /aims-app
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install python-docx 
RUN pip install requests
# COPY ./app.py ./app.py
COPY ./upload.py ./app.py
COPY ./parse.py ./parse.py
# COPY ./templates ./templates
COPY ./container ./container
#EXPOSE 5000

CMD [ "python", "./app.py" ]
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]