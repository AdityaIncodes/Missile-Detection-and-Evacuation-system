FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r ai-detection/requirements.txt

CMD ["python", "backend/app.py"]