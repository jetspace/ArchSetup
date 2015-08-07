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

import os
import subprocess

class PreInstall:
    def __init__(self):
        pass

    # Tasks:
    #
    # generate fstab          [x]
    # Hostname                [x]
    # locale.conf             [ ]
    # create time link        [x]
    # generate locales        [ ]
    # mkinitcpio              [ ]
    # set root password       [ ]
    # save keybord layout     [x]
    # save font               [x]
    # Install GRUB2           [ ] (might chooseable in future?)
    # Installing basic deamons[ ]
    # Copy Mirrorlist list.txt[ ]
    # -----> Soon: Xorg + Configuration


    def run(setupconfig):

        yield "2,Generating fstab"
        os.system("genfstab -p /mnt >> /mnt/etc/fstab")

        yield "4,Setting Hostname"
        os.system("echo " +setupconfig.hostname + " >> /mnt/etc/hostname")

        yield "8,Setting Timezone"
        os.system("ln /usr/share/zoneinfo/" +setupconfig.timezone + "/" + setupconfig.timesubzone + " /etc/localtime")

        yield "15,Setting Keymap"
        os.system("echo KEYMAP=" + setupconfig.keybord + " > /etc/vconsole.conf")

        yield "16,Setting Font"
        os.system("echo FONT=" +setupconfig.font + " >> /etc/vconsole.conf")




        yield "100,done!"