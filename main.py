#!/usr/bin/env python
# -*- coding: utf-8 -*-

from esa.esa import Esa
from swarm.swarm import Swarm
from gcalendar.gcalendar import Calendar
from utils import consts, dates
from esa.post import Post
from message import Message


def main():
    events = get_events()
    checkins = get_checkins()
    message = Message(events, checkins)

    esa = Esa(access_token=consts.ESA_ACCESS_TOKEN, current_team=consts.ESA_TEAM_NAME)

    post = Post(name='日報', body_md=message.format(), category='日報/' + dates.date_of_today())

    esa.new_post(consts.ESA_TEAM_NAME, post=post)


def get_checkins():
    swarm = Swarm(consts.SWARM_ACCESS_TOKEN, consts.SWARM_CLIENT_ID, consts.SWARM_CLIENT_SECRET)
    return swarm.get_checkins()


def get_events():
    calendar = Calendar()
    calendar.init_service()
    return calendar.get_events_today()


if __name__ == '__main__':
    main()
