#!/usr/bin/env python

import pybgsched
from pybgsched import getComputeHardware
pybgsched.init("/bgsys/local/etc//bg.properties")
h = getComputeHardware()
m = h.getMidplane('R00-M0')
m.getState()
m.getInUse()
str(m)
nb = m.getNodeBoard(3)
str(nb)
nb.getQuadrant()
nbv = pybgsched.getNodeBoards('R00-M0')


print(nbv)
