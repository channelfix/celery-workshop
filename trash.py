import requests

from celery import Celery
from celery.schedules import crontab


app = Celery('trash', backend='rpc://', broker='pyamqp://guest@localhost//')
app.conf.timezone = 'Asia/Manila'


@app.task
def print_something(*args, **kwargs):
    print args
    print 'something'


@app.task
def check_op_chapter(chapter):
    url = 'https://mangafox.me/manga/one_piece/vTBD/c{}/1.html'.format(chapter)
    response = requests.get(url)
    is_live = response.content.find('<div class="read_img">') > -1

    if is_live:
        print 'chapter {} is live'.format(chapter)
    else:
        print 'chapter {} is not yet live :('.format(chapter)


# http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
@app.on_after_configure.connect
def setup_periodic_tasks(sender, *args, **kwargs):
    # http://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.add_periodic_task
    sender.add_periodic_task(
        schedule=30.0, sig=print_something, args=('hahaha',))

    # http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#crontab-schedules
    sender.add_periodic_task(
        schedule=crontab(minute='*'), sig=print_something, args=('hahaha',))


if __name__ == '__main__':
    check_op_chapter.delay(chapter=800)
    # http://docs.celeryproject.org/en/latest/reference/celery.app.task.html#celery.app.task.Task.apply_async
    check_op_chapter.apply_async(kwargs={'chapter': 801}, countdown=10)
