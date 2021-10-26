#!/usr/bin/env python3

from tasks import long_running_task


def launch_tasks():
    """Launch a celery worker with 5 concurrent processes.
    :param: none.
    :return: void.
    """

    for i in range(1, 5):
        print(f'Launching task number {i}')
        long_running_task.delay(i)
