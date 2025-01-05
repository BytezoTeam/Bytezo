FROM python:3.11-alpine AS build

WORKDIR /app

COPY bytezo_website/ bytezo_website/
COPY tailwind.config.js ./
# Build CSS Styles
RUN pip install --no-cache-dir pytailwindcss-extra && \
    tailwindcss-extra && \
    tailwindcss-extra -i ./bytezo_website/static/css/input.css -o .//bytezo_website/static/css/output.css

FROM python:3.11-alpine AS RUN

WORKDIR /app

RUN addgroup nonroot && \
    adduser --system -G nonroot --disabled-password nonroot && \
    apk add --no-cache gosu --repository https://dl-cdn.alpinelinux.org/alpine/edge/testing/

# Install and setup dependencies
COPY requirements.lock ./
RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -r requirements.lock

# Copy project files
COPY --from=build /app/bytezo_website/ bytezo_website/
COPY docker-entrypoint.sh ./
RUN chmod +x docker-entrypoint.sh

EXPOSE 8000

VOLUME [ "/app/database/" ]

ENTRYPOINT ["./docker-entrypoint.sh"]

HEALTHCHECK CMD wget --spider -q http://127.0.0.1:8000 || exit 1
