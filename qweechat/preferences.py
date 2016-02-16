# -*- coding: utf-8 -*-
#
# preferences.py - preferences window
#
# Copyright (C) 2011-2014 Krzysztof Korościk <soltys@soltys.info>
#
# This file is part of QWeeChat, a Qt remote GUI for WeeChat.
#
# QWeeChat is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# QWeeChat is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with QWeeChat.  If not, see <http://www.gnu.org/licenses/>.
#

import qt_compat
QtGui = qt_compat.import_module('QtGui')


class PreferencesDialog(QtGui.QDialog):
    """Preferences window."""

    def __init__(self, cfg, *args):
        QtGui.QDialog.__init__(*(self,) + args)
        self.config = cfg
        self.setModal(True)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        self.show()
