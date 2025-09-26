# 1. Use official Python base image
FROM python:3.13-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the application code
COPY . .

# 5. Expose port (FastAPI runs on 8000 by default)
EXPOSE 8000

# 6. Run FastAPI with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
