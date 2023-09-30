FROM python:3.10

WORKDIR /

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASKAPP flasky
# ENV FLASK_HOST 0.0.0.0
# ENV FLASK_PORT 5000

CMD ["flask", "run", "--debug", "--host=0.0.0.0", "--port=5000"]