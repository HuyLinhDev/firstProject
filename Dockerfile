FROM python:3.10.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN groupadd -g 1000 app_group

RUN useradd -g app_group --uid 1000 app_user

RUN chown -R app_user:app_group /app

USER app_user

CMD ["/bin/sh", "-c", "unvicorn app.main:app -h 0.0.0.0"]