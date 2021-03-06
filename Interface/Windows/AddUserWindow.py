#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of ArchSetup.
#
# ArchSetup is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ArchSetup is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ArchSetup.  If not, see <http://www.gnu.org/license

from Interface.Windows.SetupWindow import SetupWindow
from Interface.Widgets.SpacerWidget import SpacerWidget
from Interface.Widgets.TextWidget import TextWidget
from Interface.Widgets.EntryWidget import EntryWidget
from Interface.Widgets.PasswordWidget import PasswordWidget
from Interface.Widgets.ProgressWidget import ProgressWidget

import gettext

class AddUserWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()
        self.callback = callback

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        #tmp var
        self.cur_usr_name = ""

        self.setupconfig = setupconfig
        self.addwidget(TextWidget(1, 1, _('Now you have to create a user:'),  40))
        self.addwidget(TextWidget(2, 1, _('Username:'), 40))
        self.username = self.addwidget(EntryWidget(3, 1, "", 40, self.event, 40))
        self.addwidget(TextWidget(4, 1, _('Home directory:'), 40))
        self.homedir  = self.addwidget(EntryWidget(5, 1, "", 40, self.event, 40))
        self.addwidget(TextWidget(6, 1, _("Real name:"), 40))
        self.fullname = self.addwidget(EntryWidget(7, 1, "", 40, self.event, 40))
        self.addwidget(TextWidget(8, 1, _("Password:"), 40))
        self.password = self.addwidget(PasswordWidget(9, 1, "", 40, self.event, 40, '*'))
        self.addwidget(TextWidget(10,1, _("Please confirm:"), 40))
        self.confirm  = self.addwidget(PasswordWidget(11, 1, "", 40, self.event, 40, '*'))
        self.addwidget(TextWidget(12,1, _("Password safety:"), 40))
        self.pro      = self.addwidget(ProgressWidget(13, 1, 0, 40))
        self.matcherr = self.addwidget(TextWidget(15, 1, _('Passwords do not match!'),  40))
        self.matcherr.setvisibility(False)
        self.next = self.setnextcallback(callback, '')
        self.setprevcallback(callback, 'prev')

    def event(self, event, opt=''):
        if event == 'refresh':
            if self.cur_usr_name != self.username.gettext():
                self.cur_usr_name = self.username.gettext()
                self.homedir.settext("/home/" + self.cur_usr_name)
            if len(self.username.gettext()) > 0 and len(self.homedir.gettext()) > 0 and len(self.fullname.gettext()) > 0 and len(self.password.gettext()) > 0 and self.password.gettext() == self.confirm.gettext():
                self.next.setcallback(self.callback, 'next')
                self.matcherr.setvisibility(False)
                self.setupconfig.setuserdata(self.username.gettext(), self.homedir.gettext(), self.fullname.gettext(), self.password.gettext())
            else:
                self.matcherr.setvisibility(True)
                self.next.setcallback(self.callback, '')
            self.pro.setvalue(int(100 / 20 * len(self.password.gettext())))
            self.refresh()
        else:
            super().event(event)
