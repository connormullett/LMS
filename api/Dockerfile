FROM python:3

WORKDIR /var/lms/api

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

copy . .

RUN python manage.py db init

RUN python manage.py db migrate
RUN python manage.py db upgrade

CMD [ "python", "manage.py run" ]

