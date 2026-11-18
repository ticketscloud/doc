
FROM mirror.gcr.io/library/python:3.9-slim AS build

WORKDIR /srv/src

COPY requirements.txt ./requirements.txt

RUN python -m pip install --no-cache-dir 'pip<26' \
 && python -m pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sphinx-build -b html \
    -d /tmp/sphinx-doctrees /srv/src /tmp/site \
 && test -s /tmp/site/index.html

FROM nginx:stable-alpine

WORKDIR /srv/src

COPY deploy/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /tmp/site/ /srv/src/ru/latest/

EXPOSE 8080
