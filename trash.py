from celery import Celery


app = Celery('trash', broker='pyamqp://guest@localhost//')


@app.task
def print_something():
    print 'something'
