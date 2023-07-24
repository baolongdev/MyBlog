FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]