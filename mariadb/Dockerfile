FROM mariadb

RUN apt-get update

ENV MARIADB_ROOT_PASSWORD=root \
    MARIADB_ALLOW_EMPTY_ROOT_PASSWORD=true



HEALTHCHECK --start-period=5m \
  CMD mariadb -e 'SELECT @@datadir;' || exit 1
