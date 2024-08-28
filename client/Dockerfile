FROM python:3-alpine
WORKDIR /client
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
CMD ["python", "client.py"]
