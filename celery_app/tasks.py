#!/usr/bin/env python3

from __future__ import absolute_import
from celery_init import celery_app
from datetime import datetime
import time
import random


@celery_app.task
def long_running_task(i):
    """Simulates a long running task that takes a random execution time
    between 5 and 15 seconds
    """

    seconds_it_took = round(random.uniform(5, 15), 2)
    what_time = datetime.now().strftime("%H:%M:%S.%f")
    print(f'STARTED task {i} at {what_time}, it will run for {seconds_it_took} seconds')
    time.sleep(seconds_it_took)

    what_time = datetime.now().strftime("%H:%M:%S.%f")
    print(f'FINISHED task {i} at {what_time} after {seconds_it_took} seconds')
