#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = '岳立强'

import time,uuid

from orm import Model,StringField,BooleanField,FloatField,TextField

def next_id():
	return '%015d%s000' % (int(time.time()*1000),uuid.uuid4().hex)

class User(Model):
	__table__='users'

	id=StringField(primary_key=True,default=next_id,dd1='varchar(50)')
	email=StringField(dd1='varchar(50)')
	passwd=StringField(dd1='varchar(50)')
	admin=BooleanField()
	name=StringField(dd1='varchar(50)')
	image=StringField(dd1='varchar(500)')
	create_at=FloatField(default=time.time)

class Blog(Model):
	__table__='blogs'

	id=StringField(primary_key=True,default==next_id,dd1='varchar(50)')
	user_id=StringField(dd1='varchar(50)')
	user_name=StringField(dd1='varchar(50)')
	user_image=StringField(dd1='varchar(500)')
	name=StringField(dd1='varchar')
	summary=StringField(dd1='varchar(50)')
	content=TextField()
	create_at=FloatField(default=time.time)

class Comment(Model):
	__table__='comments'

	id=StringField(primary_key=True,default=next_id,dd1='varchar(50)')
	blog_id=StringField(dd1='varchar(50)')
	user_id=StringField(dd1='varchar(50)')
	user_name=StringField(dd1='varchar(50)')
	user_image=StringField(dd1='varchar(500)')
	content=TextField()
	create_at=FloatField(default=time.time)

