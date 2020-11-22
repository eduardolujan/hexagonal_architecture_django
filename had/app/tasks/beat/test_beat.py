
from datetime import datetime

from config.celery_app import app

# Infra
from modules.shared.infrastructure.log import get_logger

log = get_logger(file_path=__file__)


@app.task
def test_beat():
    log.info(f"Executed {datetime.now()}")

