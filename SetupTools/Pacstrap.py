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

import subprocess
from SetupTools.Software import Software

class Pacstrap:
    def __init__(self):
        pass

    def run(self, setupconfig):
        p = subprocess.Popen(["pacstrap", "/mnt", "base", "base-devel"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in p.stdout:
            yield line.decode("utf-8")
        software = Software()

        for x in software.installPackages(setupconfig.software):
            yield x
