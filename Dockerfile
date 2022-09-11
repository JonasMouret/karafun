FROM tiangolo/uwsgi-nginx:python3.9

ENV APP_HOME=/app
RUN mkdir $APP_HOME/static
WORKDIR $APP_HOME
COPY . $APP_HOME

LABEL maintainer="jonas@mouret.org"
LABEL description="Developement image for Demo CMS"

ENV PYTHONDONTWRITEBYTECODE 1

ENV UWSGI_INI /app/deploy/uwsgi.ini
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN apt-get update -qq && apt-get install build-essential gettext libpq-dev postgresql-contrib postgresql-client gcc  -y -qq \
    && pip install --trusted-host pypi.python.org --upgrade pip \
    && pip install --trusted-host pypi.python.org -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove gcc

RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt


RUN mv ./deploy/nginx.conf /etc/nginx/conf.d/nginx2.conf \
    & mv /app/deploy/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD sleep 5 \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput \
    && /usr/bin/supervisord