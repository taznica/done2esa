#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from esa.client import Client

access_token = os.environ['ESA_ACCESS_TOKEN']
team_name = os.environ['ESA_TEAM_NAME']


def main():
    esa = Client(access_token=access_token, current_team=team_name)
    print(esa.team(team_name))


if __name__ == '__main__':
    main()
