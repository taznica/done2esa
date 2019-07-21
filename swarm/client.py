#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import json
import requests


class Client:
    def __init__(self, access_token, client_id, client_secret):
        self.access_token = access_token
        self.client_id = client_id
        self.client_secret = client_secret

    def check_api(self):
        url = 'https://api.foursquare.com/v2/venues/explore'
        params = dict(
            client_id=self.client_id,
            client_secret=self.client_secret,
            v='20180323',
            ll='40.7243,-74.0018',
            query='coffee',
            limit=1
        )
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        return data

    def get_checkins(self):
        url = 'https://api.foursquare.com/v2/users/self/checkins'
        params = dict(
            oauth_token=self.access_token,
            client_id=self.client_id,
            client_secret=self.client_secret,
            v='20190720',
            limit=30,
            sort='oldestfirst',
            afterTimestamp=self.start_of_today(),
            beforeTimestamp=int(datetime.now().timestamp())

        )
        resp = requests.get(url=url, params=params)
        data = json.loads(resp.text)
        return data

    def start_of_today(self):
        return int(datetime.now().replace(hour=0, minute=0, second=0).timestamp())

    def today(self):
        return int(datetime.now().timestamp())

    '''    
    def get_auth(self):
        # access 'https://foursquare.com/oauth2/authenticate?client_id=' + swarm_client_id + '&response_type=code&redirect_uri=' + redorect_uri)
        # -> access_code

        # requests.get('https://foursquare.com/oauth2/access_token?client_id=' + client_id + '&client_secret=' + client_secret + '&grant_type=authorization_code&redirect_uri=' + redirect_uri +  '&code=' + acccess_code)
        # -> access_token
    '''

