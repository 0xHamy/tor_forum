FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY populate.py .
COPY templates/ templates/

EXPOSE 5000

# Run populate.py to initialize the database, then start Gunicorn
CMD ["sh", "-c", "python populate.py && gunicorn --bind 0.0.0.0:5000 --log-level debug app:app"]