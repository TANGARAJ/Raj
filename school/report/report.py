import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebkit import *


def fill_login_form(web,user,password):
    doc=web.page().mainFrame().documentElement()
    user=doc.findFrist('input[id=Email]') 