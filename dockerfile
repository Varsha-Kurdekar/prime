FROM python:3.12-slim
WORKDIR /prime
COPY . .
CMD ["python", "prime.py"]