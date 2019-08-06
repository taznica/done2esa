#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


def unix_now():
    return int(datetime.now().timestamp())


def unix_start_of_today():
    return int(datetime.now().replace(hour=0, minute=0, second=0).timestamp())


def rfc_now():
    return datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time


def rfc_start_of_today():
    return datetime.utcnow().replace(hour=0, minute=0, second=0).isoformat() + 'Z'


def rfc_end_of_today():
    return datetime.utcnow().replace(hour=23, minute=59, second=59).isoformat() + 'Z'


def str_to_hm(string):
    return datetime.fromisoformat(string).time().strftime('%H:%M')
