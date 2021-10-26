#!/usr/bin/env python3

from __future__ import absolute_import

from celery import Celery


celery_app = Celery('celery_app', #name of project package
             broker='amqp://guest:guest@rabbitmq3:5672', # RabbitMQ connection
             backend='rpc://', # storing task results, rpc means sending results back as AMQP msgs
             include=['tasks'])
             