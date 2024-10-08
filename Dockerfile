FROM python:3

WORKDIR /usr/src/bin

COPY . .

CMD [ "python", "./GroupAnagram.py" ]

