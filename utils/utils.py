#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


def unix_now():
    return int(datetime.now().timestamp())


def unix_start_of_today():
    return int(datetime.now().replace(hour=0, minute=0, second=0).timestamp())


def rfc_now():
    return datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
