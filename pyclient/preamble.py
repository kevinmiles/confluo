#!/usr/bin/env python

import os
import sys
from thrift import Thrift
from dialog import dialog_client

dialog = None

def dialogConnect(host = 'localhost', port = 9090):
  global dialog
  dialog = dialog_client.dialog_client(host, port)  
  

try:
  dialogConnect()
  print "DiaLog Client is now available as dialog."
except Thrift.TException, tx:
  print '%s' % (tx.message)
  print 'Check your server status and retry connecting with dialogConnect(host, port)'

# Add auto-completion and a stored history file of commands to your Python
# interactive interpreter. Requires Python 2.0+, readline. Autocomplete is
# bound to the Esc key by default.
#
# Store the file in ~/.pystartup, and set an environment variable to point
# to it:  "export PYTHONSTARTUP=~/.pystartup" in bash.

import atexit
import readline
import rlcompleter

historyPath = os.path.expanduser("~/.pyhistory")

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)
readline.parse_and_bind('tab: complete')

del os, atexit, readline, rlcompleter, save_history, historyPath, sys