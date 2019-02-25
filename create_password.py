#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'huangbinghe@gmail.com'

import sublime
import sublime_plugin
import random
import string


class CreatePasswordCommand(sublime_plugin.TextCommand):

    def run(self, edit, safe_level=1):
        setting = sublime.load_settings("HBH-PasswordCreater.sublime-settings")
        print('safe_level:', safe_level)
        if safe_level == 1:
            chars = string.digits
        elif safe_level == 2:
            chars = string.ascii_letters + string.digits
        elif safe_level == 3:
            chars = string.ascii_letters + string.digits + \
                '!"#$%&/()*+,-./:;<=>?@[//]^_`{|}~'
        else:
            chars = string.ascii_letters + string.digits

        pwd_length = setting.get('password_length', 6)

        pwd = ''.join([random.choice(chars) for i in range(int(pwd_length))])

        sublime.set_clipboard(pwd)

        self.view.replace(edit,
                          self.view.sel()[0], 'New Password:'+pwd)
