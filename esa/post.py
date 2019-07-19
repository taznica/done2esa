#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Post:
    def __init__(self, name, *,
                 body_md: str = None,
                 tags: [str] = None,
                 category: str = None,
                 wip: bool = True,
                 message: str = None,
                 user: str = None,
                 template_post_id: int = None):

        self.name = name
        self.body_md = body_md
        self.tags = tags
        self.category = category
        self.wip = wip
        self.message = message
        self.user = user
        self.template_post_id = template_post_id

    def data(self):
        data = {
            'post': {
                'name': self.name,
                'body_md': self.body_md,
                'tags': self.tags,
                'category': self.category,
                'wip': self.wip,
                'message': self.wip,
                'user': self.user,
                'template_post_id': self.template_post_id
            }
        }
        return data
