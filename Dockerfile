FROM python:2-slim

RUN mkdir -p /app/youtube_exporter

RUN pip install prometheus_client

WORKDIR /app/youtube_exporter

COPY requirements.txt /app/youtube_exporter
RUN pip install --no-cache-dir -r requirements.txt

COPY youtube_exporter.py /app/youtube_exporter

EXPOSE 6969

ENTRYPOINT [ "python", "-u", "./youtube_exporter.py"]
