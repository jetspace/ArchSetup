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
# along with ArchSetup.  If not, see <http://www.gnu.org/licenses/>.

from SetupTools.Timezone import Timezone
from Interface.SetupWindow import SetupWindow
from Interface.SpacerWidget import SpacerWidget
from Interface.TextWidget import TextWidget
from Interface.ScrollWidget import ScrollWidget
from Interface.RadioWidget import RadioWidget

import gettext

class TimesubzoneWindow(SetupWindow):
    def __init__(self, callback, setupconfig):
        super().__init__()

        # Init Translation
        trans = gettext.translation("archsetup", "locale", fallback=True)
        trans.install()

        # Init setup tools
        self.timezone = Timezone()
        self.setupconfig = setupconfig

        # Add widgets and setup callbacks...
        self.addwidget(TextWidget(1, 1, _('Please select a subzone...'),  40))
        self.radiowidget = RadioWidget(0, 0, 40, self.timezone.list_subzones(self.setupconfig.gettimezone()), self.event)
        self.addwidget(ScrollWidget(3, 1, 40, 20, self.radiowidget, self.event))
        self.addwidget(SpacerWidget(23, 1, 1))
        self.setnextcallback(callback, 'next')
        self.setprevcallback(callback, 'prev')

    def event(self, event, opt=''):
        if event == 'show':
            self.radiowidget.setlist(self.timezone.list_subzones(self.setupconfig.gettimezone()))
            self.refresh()
        elif event == 'refresh':
            self.refresh()
        elif event == 'selection':
            self.setupconfig.settimesubzone(opt)
        else:
            super().event(event)
