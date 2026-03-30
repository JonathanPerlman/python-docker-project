FROM python:3.9-slim

WORKDIR /app

# 3. תעתיק את הקובץ מהמחשב שלי לתוך התיקייה /app בקונטיינר
COPY app.py .

# 4. תגיד לדוקר שהשרת הזה מקשיב בפורט 8000
EXPOSE 8000

# 5. מה הפקודה שמריצה את השרת?
CMD ["python", "app.py"]