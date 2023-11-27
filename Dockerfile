FROM python:3.11-slim-buster

WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5002

CMD [ "python3", "app.py" ]