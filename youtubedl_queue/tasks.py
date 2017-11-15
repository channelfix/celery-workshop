from celery.decorators import periodic_task
from celery import shared_task
from celery.schedules import crontab
from datetime import timedelta

from .utils import download
from .models import DownloadRequest


@periodic_task(run_every=timedelta(seconds=30))
def printing():
    print 'hahas'


@periodic_task(run_every=crontab(minute=20))
def lol():
    print 'lol'


@shared_task
def queue_download(dl_request_pk):
    dl_request = DownloadRequest.objects.get(pk=dl_request_pk)
    download(dl_request)
