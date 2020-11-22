
from celery.schedules import crontab

from had.app.tasks.beat import test_beat


tasks = {
    'test_beat': {
        'task': test_beat,
        'schedule': crontab(minute='*'),
        'args': tuple(),
    },
}
