FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "./testapp.py"]
