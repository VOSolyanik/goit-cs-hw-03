# Use a slim version of Python 3.11
FROM python:3.11-slim

# Install required system dependencies
ENV app /app

WORKDIR $app

COPY . .

RUN pip install -r requirements.txt

# Automatically run db_connect.py on container start
CMD ["python", "app.py"]