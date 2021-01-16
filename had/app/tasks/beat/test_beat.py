

from datetime import datetime
from celery import task

# Infra
from modules.shared.infrastructure.log import get_logger

log = get_logger(file_path=__file__)


@task
def test_beat():
    print(f"Executed {datetime.now()}")
    log.info(f"Executed {datetime.now()}")

