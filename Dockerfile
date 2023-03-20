FROM python:3.9-alpine AS builder
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY mysite /app/mysite
EXPOSE 8000
ENTRYPOINT ["python3"]
RUN ["mysite/manage.py", "migrate"]
CMD ["mysite/manage.py", "runserver", "0.0.0.0:8000"]