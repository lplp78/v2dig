#! -*- coding: utf-8 -*-

import tornado.web
from base import BaseHandler
from lib import PageMixin

class MemberPageHandler(BaseHandler, PageMixin):
    def get(self, username):
        member = self.get_member(username)
        topics = self.db.topic.find({'author': member['username']},
                                    sort=[('create_time', -1)]).limit(5)
        replies = self.db.reply.find({'author': member['username']},
                                    sort=[('create_time', -1)]).limit(5)
        ideas = self.db.Idea.find({'author': member['username']},
                                  sort=[('date',-1)]).limit(5)

        self.render('member.html', 
                    member=member, topics=topics, replies=replies, ideas=ideas)

class MemberPageReplyListModule(tornado.web.UIModule):
    def render(self, replies):
        return self.render_string("module/member_reply_list.html", 
                                  replies=replies)



handlers = [
    (r'/member/(\w+)', MemberPageHandler),
    ]

ui_modules = {
    'MemberPageReplyListModule':MemberPageReplyListModule,
    }
