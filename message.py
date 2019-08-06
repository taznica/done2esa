#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Message:
    def __init__(self, events, checkins):
        self.events = events
        self.checkins = checkins

    def format(self):
        msg = '# Events\n'
        for event in self.events:
            msg += ('- ' + event + '\n')

        msg += '# Checkins\n'
        for checkin in self.checkins:
            msg += ('- ' + checkin + '\n')

        return msg

