# Notes

## What is Celery
[Celery](http://docs.celeryproject.org/en/latest/index.html) is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.

It’s a task queue with focus on real-time processing, while also supporting task scheduling.


## Part 1: Setup
* install django and celery
* install rabbitmq `brew install rabbitmq or sudo apt-get install rabbitmq-server`
* start rabbitmq service `brew service start rabbitmq or  service rabbitmq-server start`
* code dummy task
* run celery with dummy task `celery -A trash worker`


## Part 2: Basics
* create a function
* make it a celery task
* run the task
    * delay
    * apply_async
    * periodic tasks
[code](https://github.com/name3anad/celery-workshop/blob/part2/celery_tasks/trash.py)