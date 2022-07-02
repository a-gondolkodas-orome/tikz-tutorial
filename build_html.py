#!/usr/bin/python3

import os

def sh(x):
    """
    Shorter name for os.system
    """
    os.system(x)

def compile_very(name):
    sh("lwarpmk cleanall -p " + name) # when dobrogi took everything
    sh("lwarpmk cleanlimages -p " + name) # even the pictures of the geese
    sh("lualatex " + name + ".tex") # a young boy reinvented himself
    sh("lwarpmk html -p " + name) # he tricked the lord and took what was his
    sh("lwarpmk html -p " + name) # he tricked the lord and took it again
    sh("lwarpmk htmlindex -p " + name) # to the village he listed all his evil
    sh("lwarpmk limages -p " + name) # (he used pictures. villagers cant read)
    sh("lwarpmk html -p " + name) # and he tricked the lord for a third time

def main():
    os.chdir("pages")
    compile_very("mainpage")

main()
