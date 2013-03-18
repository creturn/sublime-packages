#!/usr/bin/env python
#coding: utf-8

"""""""""""""""""""""""""""""""""
File: weibo.py
Descript: this
Blog: www.creturn.com
Autor: Return
"""""""""""""""""""""""""""""""""

import sublime, sublime_plugin
import os
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')
def getWeiboList():
	weiboList = os.popen('weiboHome').readlines()
	weibo = ''.join(weiboList)
	return weibo 
class ShowhomeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		weibo = getWeiboList()
		self.view.insert(edit, 0, weibo)
