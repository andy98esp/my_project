ARG PYTHON_VERSION=3.11.4

FROM python:${PYTHON_VERSION} as develop
ARG APP_HOME=/sites/app
ENV APP_HOME=${APP_HOME} \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="${PYTHONPATH}:${APP_HOME}" \
    PATH="/root/.local/bin:${APP_HOME}/infrastructure/bin:${PATH}"

WORKDIR ${APP_HOME}

COPY application ${APP_HOME}/application
COPY infrastructure ${APP_HOME}/infrastructure

RUN pip3 install --upgrade sentry-sdk
RUN python3.11 -m pip install --user --no-cache-dir -r ${APP_HOME}/infrastructure/requirements/requirements.txt

RUN chmod +x ${APP_HOME}/infrastructure/bin/*

ENTRYPOINT ["docker-entrypoint.sh"]
