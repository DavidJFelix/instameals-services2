FROM python:3.5-slim

WORKDIR /opt/instameals

RUN mkdir instameals

RUN apt-get update && apt-get install -y --no-install-recommends \
        libproj-dev \
        gdal-bin \
        libpq-dev \
        libtiff5-dev \
        libjpeg-dev \
        zlib1g-dev \
        libfreetype6-dev \
        liblcms2-dev \
        libwebp-dev \
        tcl8.6-dev \
        tk8.6-dev \
        python-tk \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
        gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove \
        gcc

# Diagnostic command for checking dependencies
RUN pip list --outdated

COPY ./ /opt/instameals
CMD python manage.py collectstatic && \
    python manage.py migrate && \
    gunicorn instameals_services.wsgi \
        -k gaiohttp \
        --log-file -