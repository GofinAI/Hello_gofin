FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE $PORT

CMD ["waitress-serve", "--port=$PORT", "Hello_db:app"]
