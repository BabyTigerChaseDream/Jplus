#FROM python:3.8-slim-buster
# for mysql in comtainer,need to use 3.8 / slim-buster will not work
FROM python:3.8
#FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /django

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#COPY . .

#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]