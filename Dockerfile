FROM python:3.11.6-alpine3.18

WORKDIR /

COPY . .

RUN pip install --extra-index-url=https://gergely.imreh.net/wheels/ pymongo

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASKAPP flasky

CMD ["flask", "run", "--debug", "--host=0.0.0.0", "--port=5000"]
