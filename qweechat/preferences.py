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

        sections = {}

        for section in self.config.sections():
            sections[section] = QtGui.QGroupBox(section)
            boxGrid = QtGui.QGridLayout()

            for item in self.config.items(section):
                boxGrid.addWidget(QtGui.QLabel(item[0]))

            sections[section].setLayout(boxGrid)
            grid.addWidget(sections[section])

        self.dialog_buttons = QtGui.QDialogButtonBox()
        self.dialog_buttons.setStandardButtons(
            QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        self.dialog_buttons.rejected.connect(self.close)

        grid.addWidget(self.dialog_buttons, 4, 0, 1, 2)
        self.setLayout(grid)
        self.show()
