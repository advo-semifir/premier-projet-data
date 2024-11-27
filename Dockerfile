FROM Python:3.14.0a2-slim-bookworm

RUN apt update && apt upgrade

COPY . /dist

....
