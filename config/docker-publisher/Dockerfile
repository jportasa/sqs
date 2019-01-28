FROM python:3

ENV APP_DIR /app

WORKDIR /app

COPY requirements.txt $APP_DIR/
RUN pip install --no-cache-dir -r requirements.txt

COPY . $APP_DIR