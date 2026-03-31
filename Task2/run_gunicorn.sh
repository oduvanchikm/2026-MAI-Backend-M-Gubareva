#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

readonly WORKERS_CNT=4
readonly PORT=8000

function main()
{
  echo "Starting gunicorn on port ${PORT} with ${WORKERS_CNT} workers..."

  cd /Users/oduvanchik/Desktop/test/2026-MAI-Backend-M-Gubareva/Task2

  if ! gunicorn --workers ${WORKERS_CNT} \
                --bind 127.0.0.1:${PORT} \
                --access-logfile logs/gunicorn_access.log \
                --error-logfile logs/gunicorn_error.log \
                myapp:app ; then
    echo "Failed to run gunicorn..."
    return 1
  fi
}

# shellcheck disable=SC2068
main $@