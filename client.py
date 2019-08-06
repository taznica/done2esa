#!/usr/bin/env python
# -*- coding: utf-8 -*-

from esa.esa import Esa
from swarm.swarm import Swarm
from gcalendar.gcalendar import Calendar
from utils import consts, dates
from esa.post import Post
from message import Message


class Client:
    def __init__(self):
        self.esa = Esa(access_token=consts.ESA_ACCESS_TOKEN, current_team=consts.ESA_TEAM_NAME)
        self.calendar = Calendar()
        self.swarm = Swarm(consts.SWARM_ACCESS_TOKEN, consts.SWARM_CLIENT_ID, consts.SWARM_CLIENT_SECRET)

    def get_events(self):
        self.calendar.init_service()
        return self.calendar.get_events_today()

    def new_post(self):
        events = self.get_events()
        checkins = self.swarm.get_checkins()
        message = Message(events, checkins)
        post = Post(name='日報', body_md=message.format(), category='日報/' + dates.date_of_today())
        self.esa.new_post(consts.ESA_TEAM_NAME, post=post)

    def get_link_of_post(self):
        posts = self.esa.posts(consts.ESA_TEAM_NAME)
        return 'https://' + consts.ESA_TEAM_NAME + '.esa.io/posts/' + str(posts['posts'][0]['number'] + 1)

    def run(self):
        link = self.get_link_of_post()
        self.new_post()
        print(link)
