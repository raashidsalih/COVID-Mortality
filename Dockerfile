FROM python:3.9

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python3" , "/app/app_local.py" ]
