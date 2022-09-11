#!/usr/bin/python3

import os
import time

def sh(x):
    """
    Shorter name for os.system
    """
    os.system(x)

def compile_very(pn):
    os.chdir("pages")
    sh("lwarpmk cleanall -p " + pn) # when dobrogi took everything
    sh("lwarpmk cleanlimages -p " + pn) # even the pictures of the geese
    sh("lwarpmk print -p " + pn) # a young boy reinvented himself
    sh("lwarpmk html -p " + pn) # he tricked the lord and took what was his
    sh("lwarpmk html -p " + pn) # he tricked the lord and took it again
    sh("lwarpmk htmlindex -p " + pn) # to the village he listed all his evil
    sh("lwarpmk limages -p " + pn) # (he used pictures. villagers cant read)
    sh("lwarpmk html -p " + pn) # and he tricked the lord for a third time
    sh("lwarpmk clean -p " + pn)
    os.chdir("..")

def copy_files(pn):
    time.sleep(3)
    sh("rm -rf docs")
    sh("mkdir docs")
    sh("cp -rvt docs pages/*.html")
    sh("cp -rvt docs pages/*.css")
    sh("cp -rvt docs pages/mainpage.pdf")
    sh("cp -rvt docs pages/" + pn + "-images")

def main():
    pn = "mainpage"
    compile_very(pn)
    copy_files(pn)

main()
