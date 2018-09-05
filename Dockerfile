FROM python:3

COPY src /usr/src/app

ENTRYPOINT ["/usr/local/bin/python", "/usr/src/app/data-faker.py"]
