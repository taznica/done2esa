#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


def now():
    return int(datetime.now().timestamp())


def start_of_today():
    return int(datetime.now().replace(hour=0, minute=0, second=0).timestamp())
