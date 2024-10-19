FROM python:3.9.16

WORKDIR /project

COPY . .

RUN pip install -r requeriment.txt

CMD ["python","server.py"]