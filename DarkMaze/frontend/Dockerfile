FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and templates
COPY ./src ./src

# Set Python path
ENV PYTHONPATH=/app

# Expose the correct port
EXPOSE 8088

# Run the application with correct port
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8088", "--reload"]