import os,sys

def init():
    if getattr(sys, 'frozen', False):
        nowdir = os.path.dirname(os.path.realpath(sys.executable))
    elif __file__:
        nowdir = os.path.dirname(__file__)
    return nowdir
