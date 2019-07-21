#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from esa.client import Client
from swarm.client import Client as Swarm

access_token = os.environ['ESA_ACCESS_TOKEN']
team_name = os.environ['ESA_TEAM_NAME']

swarm_client_id = os.environ['SWARM_CLIENT_ID']
swarm_client_secret = os.environ['SWARM_CLIENT_SECRET']
swarm_access_token = os.environ['SWARM_ACCESS_TOKEN']


def main():
    esa = Client(access_token=access_token, current_team=team_name)
    print(esa.team(team_name))


def main_swarm():
    swarm = Swarm(swarm_access_token, swarm_client_id, swarm_client_secret)
    print(swarm.get_checkins())


if __name__ == '__main__':
    main_swarm()
