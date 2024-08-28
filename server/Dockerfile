FROM python:3-alpine
WORKDIR /server
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8765
CMD ["python", "server.py"]
