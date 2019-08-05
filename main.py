#!/usr/bin/env python
# -*- coding: utf-8 -*-

from esa.esa import Esa
from swarm.swarm import Swarm
from gcalendar.gcalendar import Calendar
from utils import consts


def main():
    esa = Esa(access_token=consts.ESA_ACCESS_TOKEN, current_team=consts.ESA_TEAM_NAME)
    print(esa.team(consts.ESA_TEAM_NAME))


def main_swarm():
    swarm = Swarm(consts.SWARM_ACCESS_TOKEN, consts.SWARM_CLIENT_ID, consts.SWARM_CLIENT_SECRET)
    print(swarm.get_checkins())


def main_calendar():
    calendar = Calendar()
    calendar.init_service()
    calendar.get_upcoming_10()


if __name__ == '__main__':
    main_calendar()
