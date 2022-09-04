#mysite/main/tasks.py

from __future__ import absolute_import
from celery import shared_task
import datetime


@shared_task
def test():
    return "test method is executing at "