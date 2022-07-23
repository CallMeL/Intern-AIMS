#image name: aims-form
FROM python:3.8
WORKDIR /aims-app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app.py ./app.py
COPY ./parse.py ./parse.py
COPY ./templates ./templates
CMD [ "python", "./app.py" ]
