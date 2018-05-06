# coding: utf-8

from fabkit import task
from fablib.vpp import Vpp


@task
def setup():
    vpp = Vpp()
    vpp.setup()
