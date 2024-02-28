FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=testapp.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
