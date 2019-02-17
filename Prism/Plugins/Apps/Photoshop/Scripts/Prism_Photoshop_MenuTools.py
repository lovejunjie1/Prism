# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2019 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.



import os, sys, platform

prismRoot = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir, os.pardir, os.pardir, os.pardir))

sys.path.insert(0, os.path.join(prismRoot, "Scripts"))
sys.path.insert(0, os.path.join(prismRoot, "PythonLibs", "Python27", "PySide"))

try:
	from PySide2.QtCore import *
	from PySide2.QtGui import *
	from PySide2.QtWidgets import *
	psVersion = 2
except:
	from PySide.QtCore import *
	from PySide.QtGui import *
	psVersion = 1

qapp = QApplication.instance()
if qapp == None:
    qapp = QApplication(sys.argv)

import PrismCore
pcore = PrismCore.PrismCore(app="Photoshop")

curPrj = pcore.getConfig("globals", "current project")
pcore.changeProject(curPrj)

result = False
if sys.argv[1] == "Tools":
	result = pcore.appPlugin.openPhotoshopTools()
elif sys.argv[1] == "SaveVersion":
	pcore.saveScene()
elif sys.argv[1] == "SaveComment":
	pcore.saveWithComment()
elif sys.argv[1] == "Export":
	result = pcore.appPlugin.exportImage()
elif sys.argv[1] == "ProjectBrowser":
	result = pcore.projectBrowser()
elif sys.argv[1] == "Settings":
	result = pcore.prismSettings()

if result == True:
    qapp.exec_()