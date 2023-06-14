FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# RUN python -m venv venv
# RUN pip install django 
# RUN django-admin startproject config .

COPY . .


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]

