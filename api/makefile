
.PHONY: clean python-packages install test run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

python-packages:
	pip install -r requirements.txt

install: python-packages

test:
	python manage.py test

run:
	python manage.py run

all: clean install test run
