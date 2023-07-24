FROM python:3.8-slim-buster
WORKDIR /app
RUN pip3 install --upgrade pip 
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "main.py"]