FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]