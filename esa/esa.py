#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


class Esa:
    def __init__(self, access_token, current_team):
        self.access_token = access_token
        self.current_team = current_team

    def create_url(self, end_point):
        base_url = 'https://api.esa.io/v1/'
        token_url = '?access_token=' + self.access_token
        return base_url + end_point + token_url

    def send_get(self, end_point):
        url = self.create_url(end_point)
        r = requests.get(url)
        return json.loads(r.text)

    def send_post(self, end_point, data):
        url = self.create_url(end_point)
        headers = {'Content-Type': 'application/json'}
        json_data = json.dumps(data)
        r = requests.post(url=url, headers=headers, data=json_data)
        return json.loads(r.text)

    def teams(self):
        return self.send_get('teams')

    def team(self, team_name):
        return self.send_get('teams/' + team_name)

    def stats(self, team_name):
        return self.send_get('teams/' + team_name + '/stats')

    def members(self, team_name):
        return self.send_get('teams/' + team_name + '/members')

    # TODO: query, include, sort and order
    def posts(self, team_name):
        return self.send_get('teams/' + team_name + '/posts')

    def post(self, team_name, post_number):
        return self.send_get('teams/' + team_name + '/posts/' + str(post_number))

    def new_post(self, team_name, post):
        return self.send_post('teams/' + team_name + '/posts', post.data())
