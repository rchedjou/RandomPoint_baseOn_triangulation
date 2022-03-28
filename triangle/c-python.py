#!/usr/bin/python3.8
#export XDG_RUNTIME_DIR=/tmp/runtime-root
# -*-coding:Utf-8 -*
# from tripy.tripy import * 
from os import getcwd, chdir, mkdir
from panda3d.core import Triangulator as Tri
import csv
import numpy.random as nr
from pylab import * 
import math

from subprocess import call
call(["./triangle", "pq A", "to", "triangle"])