#!/bin/bash

python manage.py collectstatic --no-input && \
gunicorn -c "./gunicorn_config.py" baseProjectRename.wsgi