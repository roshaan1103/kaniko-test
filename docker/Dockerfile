FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt first and install dependencies
#COPY requirements.txt .

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#RUN pip install fastapi uvicorn requests pydantic

# Copy the rest of the app
COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

