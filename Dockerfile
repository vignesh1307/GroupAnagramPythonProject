FROM python:3

WORKDIR /app

COPY . .

CMD [ "python", "./GroupAnagram.py" ]

