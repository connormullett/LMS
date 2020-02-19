FROM python:3

WORKDIR /var/lms/api

ENV ENVIRONMENT=prod
ENV DATABASE_URI=postgresql://connor@localhost/lms
ENV SECRET_KEY=secret_key

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

copy . .

RUN rm -rf ./migrations
RUN python manage.py db init

RUN python manage.py db migrate
RUN python manage.py db upgrade

CMD [ "python", "manage.py run" ]
