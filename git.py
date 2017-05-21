#!/usr/bin/env python
# encoding: utf-8


import os
import sys, getopt

url = 'git@github.com:RedFalsh/python_packages.git'
name = 'RedFalsh.github.io'
def pull():
    os.system('git kk%s'%url)

def push(commit):
    os.system('git add ./')
    os.system('git commit -m %s'%commit)
    os.system('git push origin master')

def help():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hp", ["help","push","pull"])
    except getopt.GetoptError:
        print('error')
    print(opts)
    for o, a in opts:
        if o in ("-h", "--help"):
            print('\t%-20s%s'%('-h or --help','help information'))
            print('\t%-20s%s'%('--push','push the blog to Github'))
            print('\t%-20s%s'%('--pull','pull the the blog from Github'))
        if o in ('','--pull'):
            pull()
        if o in ('','-p'):
            push(args[0])

if __name__=="__main__":
    help()





