FROM        python:3.11-slim

ENV         PROJECTPATH /app
ENV         USER app
ENV         mode ${APP_MODE}

RUN         set -x \
            && apt-get -qq update \
            && apt-get install -y --no-install-recommends \
               libpq-dev git gettext binutils libproj-dev curl \
            && apt-get purge -y --auto-remove \
            && rm -rf /var/lib/apt/lists/*

RUN         ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime

ADD         https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait ${PROJECTPATH}/wait
RUN         chmod +x ${PROJECTPATH}/wait

RUN         curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3.11 - \
            && cd /usr/local/bin  \
            && ln -s /opt/poetry/bin/poetry \
            && poetry config virtualenvs.create false

WORKDIR      ${PROJECTPATH}

RUN         useradd -m -d /home/${USER} ${USER} \
            && mkdir -p /home/${USER}/logs/ \
            && chown -R ${USER} ${PROJECTPATH}

COPY        poetry.lock pyproject.toml ${PROJECTPATH}

RUN         poetry install --no-root
COPY        --chown=${USER} ./src ${PROJECTPATH}




