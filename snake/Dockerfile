FROM python:3.10-slim-buster
ENV LANG "en_US.UTF-8"
ENV LANGUAGE "en_US:en"
ENV LC_ALL "en_US.UTF-8"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get upgrade

WORKDIR /usr/src
COPY makefile .
COPY main.py .
COPY snake/ .
COPY requirements.txt .
RUN make venv

# La tu dois creer un user non root et chown susr ce user /code
RUN groupadd nobody
USER nobody:nobody
CMD ["make", "snake"]
