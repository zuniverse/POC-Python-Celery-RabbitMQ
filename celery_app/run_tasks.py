#!/usr/bin/env python3

from tasks import long_running_task


def launch_tasks():
    for i in range(1, 5):
        print(f'Launching task number {i}')
        result = long_running_task.delay(i)
