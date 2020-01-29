
#!/usr/bin/python
# -*- coding: utf-8 -*-

from enum import Enum
import time

__author__= "Tomelin Michele,Luca Manini"

__email__ = "tomelinmichele@gmail.com"

__version__= "1.0"

__status__= "Beta"

__date__= "23/11/2019"

ip="192.168.7.2"
ip2="192.168.7.4"
ip3="192.168.7.5"
idx="3"

 import ftrobopy
 txt = ftrobopy.ftrobopy(host=ip,port=65000) 
 txt.play_sound(idx,1,100)
