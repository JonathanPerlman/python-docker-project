FROM python:3.9-slim

WORKDIR /app

# מעתיקים את הקליינט פנימה
COPY app.py .

# הלקוח רק שולח בקשה ומסיים, הוא לא צריך לפתוח פורט (EXPOSE)
CMD ["python", "app.py"]