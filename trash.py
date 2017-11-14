from celery import Celery


app = Celery('trash', backend='rpc://', broker='pyamqp://guest@localhost//')


@app.task
def print_something():
    print 'something'
