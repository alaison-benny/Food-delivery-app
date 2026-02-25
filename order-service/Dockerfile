FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ഈ സർവീസ് 5002 പോർട്ടിലാണ് വർക്ക് ചെയ്യുന്നത്
EXPOSE 5002

CMD ["python", "app.py"]