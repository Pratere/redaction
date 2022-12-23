FROM python:3.10-buster

RUN apt update && apt upgrade -y

RUN apt-get install tesseract-ocr python3-opencv -y

COPY redacting/ /code

WORKDIR /code

RUN pip3 install -r requirements.txt

RUN mkdir /data

WORKDIR /data

ENTRYPOINT ["python3", "/code/redact.py"]
