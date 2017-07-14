#!/usr/bin/python
#
# This is a small stub that is intended to be built into an executable with a
# setup.py file using "python setup.py py2exe".  This results in an executable
# called py.exe.  This can be used to run an arbitrary python script on Windows
# (XP and later) via py.exe (name of script).
#
# Changes:
#  2.7.4.1:
#   * initial release
#  2.7.4.2:
#   * fixed an issue with __file__ and __name__
#  2.7.4.3:
#   * Added the program path to sys.path when running a program, and "" to
# sys.path when running direct or interpretted.
#  2.7.5.4:
#   * Upgraded to python 2.7.5
#  2.7.5.5:
#   * Imported submodules, such as logging.handlers, since they weren't
# included implicitly.
#  2.7.8.6:
#   * Added support for multiprocessing forking
#   * Added support for non-ttty direct usage (input and output pipes, for
# instance)
#   * Added support for -i option and PYTHONINSPECT environment variable.
#   * Turned off "frozen" flag in py.exe
#   * Upgraded pywin32 to build 219 (was 218).
#   * Upgraded to python 2.7.8
#   * Added import site to interactive prompts to get help and other commands
# added to the builtins.
#   * Added support for unbuffered -u option and PYTHONUNBUFFERED environment
# variable.
#  2.7.8.7:
#   * Added support for -E, -x, and --version options.
#   * Changed how the globals / locals dictionaries are used for greater
# consistency in different execution modes.
#   * Accept multiple single letter command line options grouped together.
#  2.7.8.8:
#   * Fixed a bug I introduced in the last version when renaming the variable
# "loc".
#  2.7.8.9:
#   * My change to make globals dictionaries more consistent broke
# multiprocessing forking.  I've reverted some of the changes.
#  2.7.9.10:
#   * Upgraded to python 2.7.9
#   * Added psutil 2.1.3 win32
#   * Added support for the -m option.
#   * Turned off the optimization flag when building py.exe.  Having it on
# interferes with some modules (such as sympy) which rely on docstring
# manipulation.

AllModules = False

import os
import sys

if len(sys.argv)==1 and not hasattr(sys, "frozen"):
   AllModules = True
if not AllModules and sys.argv[:2][-1]!="--all":
   pass
else:
   # I think this is the complete list of modules in the Python 2.7
   # installation on Windows XP.  This was the default 2.7 installation without
   # any options, plus pywin32-219, psutil 2.1.3, setuptools, and py2exe.  I
   # generated the list of modules with help("modules").  I then commented out
   # anything that wouldn't import.  Further, there are some submodules that
   # don't automatically import with the base module.  help("modules .") lists
   # these.  Any module that isn't present with its base but can be imported
   # was then added.
   try:
      import xlwings
   except:
      pass

   try:
      import __future__
   except:
      pass

   try:
      import _ast
   except:
      pass

   try:
      import _bisect
   except:
      pass

   try:
      import _bootlocale
   except:
      pass

   try:
      import _bz2
   except:
      pass

   try:
      import _codecs
   except:
      pass

   try:
      import _codecs_cn
   except:
      pass

   try:
      import _codecs_hk
   except:
      pass

   try:
      import _codecs_iso2022
   except:
      pass

   try:
      import _codecs_jp
   except:
      pass

   try:
      import _codecs_kr
   except:
      pass

   try:
      import _codecs_tw
   except:
      pass

   try:
      import _collections
   except:
      pass

   try:
      import _collections_abc
   except:
      pass

   try:
      import _compat_pickle
   except:
      pass

   try:
      import _compression
   except:
      pass

   try:
      import _csv
   except:
      pass

   try:
      import _ctypes
   except:
      pass

   try:
      import _ctypes_test
   except:
      pass

   try:
      import _datetime
   except:
      pass

   try:
      import _decimal
   except:
      pass

   try:
      import _dummy_thread
   except:
      pass

   try:
      import _elementtree
   except:
      pass

   try:
      import _functools
   except:
      pass

   try:
      import _hashlib
   except:
      pass

   try:
      import _heapq
   except:
      pass

   try:
      import _imp
   except:
      pass

   try:
      import _io
   except:
      pass

   try:
      import _json
   except:
      pass

   try:
      import _locale
   except:
      pass

   try:
      import _lsprof
   except:
      pass

   try:
      import _lzma
   except:
      pass

   try:
      import _markupbase
   except:
      pass

   try:
      import _md5
   except:
      pass

   try:
      import _msi
   except:
      pass

   try:
      import _multibytecodec
   except:
      pass

   try:
      import _multiprocessing
   except:
      pass

   try:
      import _opcode
   except:
      pass

   try:
      import _operator
   except:
      pass

   try:
      import _osx_support
   except:
      pass

   try:
      import _overlapped
   except:
      pass

   try:
      import _pickle
   except:
      pass

   try:
      import _pydecimal
   except:
      pass

   try:
      import _pyio
   except:
      pass

   try:
      import _random
   except:
      pass

   try:
      import _sha1
   except:
      pass

   try:
      import _sha256
   except:
      pass

   try:
      import _sha512
   except:
      pass

   try:
      import _signal
   except:
      pass

   try:
      import _sitebuiltins
   except:
      pass

   try:
      import _socket
   except:
      pass

   try:
      import _sqlite3
   except:
      pass

   try:
      import _sre
   except:
      pass

   try:
      import _ssl
   except:
      pass

   try:
      import _stat
   except:
      pass

   try:
      import _string
   except:
      pass

   try:
      import _strptime
   except:
      pass

   try:
      import _struct
   except:
      pass

   try:
      import _symtable
   except:
      pass

   try:
      import _testbuffer
   except:
      pass

   try:
      import _testcapi
   except:
      pass

   try:
      import _testimportmultiple
   except:
      pass

   try:
      import _testmultiphase
   except:
      pass

   try:
      import _thread
   except:
      pass

   try:
      import _threading_local
   except:
      pass

   try:
      import _tracemalloc
   except:
      pass

   try:
      import _warnings
   except:
      pass

   try:
      import _weakref
   except:
      pass

   try:
      import _weakrefset
   except:
      pass

   try:
      import _win32sysloader
   except:
      pass

   try:
      import _winapi
   except:
      pass

   try:
      import _winxptheme
   except:
      pass

   try:
      import abc
   except:
      pass

   try:
      import adodbapi
   except:
      pass

   try:
      import afxres
   except:
      pass

   try:
      import aifc
   except:
      pass

   try:
      import antigravity
   except:
      pass

   try:
      import argparse
   except:
      pass

   try:
      import array
   except:
      pass

   try:
      import ast
   except:
      pass

   try:
      import asynchat
   except:
      pass

   try:
      import asyncio
   except:
      pass

   try:
      import asyncore
   except:
      pass

   try:
      import atexit
   except:
      pass

   try:
      import audioop
   except:
      pass

   try:
      import base64
   except:
      pass

   try:
      import bdb
   except:
      pass

   try:
      import binascii
   except:
      pass

   try:
      import binhex
   except:
      pass

   try:
      import bisect
   except:
      pass

   try:
      import builtins
   except:
      pass

   try:
      import bz2
   except:
      pass

   try:
      import cProfile
   except:
      pass

   try:
      import calendar
   except:
      pass

   try:
      import cgi
   except:
      pass

   try:
      import cgitb
   except:
      pass

   try:
      import chunk
   except:
      pass

   try:
      import cmath
   except:
      pass

   try:
      import cmd
   except:
      pass

   try:
      import code
   except:
      pass

   try:
      import codecs
   except:
      pass

   try:
      import codeop
   except:
      pass

   try:
      import collections
   except:
      pass

   try:
      import colorsys
   except:
      pass

   try:
      import commctrl
   except:
      pass

   try:
      import compileall
   except:
      pass

   try:
      import concurrent
   except:
      pass

   try:
      import configparser
   except:
      pass

   try:
      import contextlib
   except:
      pass

   try:
      import copy
   except:
      pass

   try:
      import copyreg
   except:
      pass

   try:
      import crypt
   except:
      pass

   try:
      import csv
   except:
      pass

   try:
      import ctypes
   except:
      pass

   try:
      import curses
   except:
      pass

   try:
      import datetime
   except:
      pass

   try:
      import dbi
   except:
      pass

   try:
      import dbm
   except:
      pass

   try:
      import dde
   except:
      pass

   try:
      import decimal
   except:
      pass

   try:
      import difflib
   except:
      pass

   try:
      import dis
   except:
      pass

   try:
      import distutils
   except:
      pass

   try:
      import doctest
   except:
      pass

   try:
      import dummy_threading
   except:
      pass

   try:
      import easy_install
   except:
      pass

   try:
      import email
   except:
      pass

   try:
      import encodings
   except:
      pass

   try:
      import ensurepip
   except:
      pass

   try:
      import enum
   except:
      pass

   try:
      import errno
   except:
      pass

   try:
      import faulthandler
   except:
      pass

   try:
      import fibonacci
   except:
      pass

   try:
      import filecmp
   except:
      pass

   try:
      import fileinput
   except:
      pass

   try:
      import fnmatch
   except:
      pass

   try:
      import formatter
   except:
      pass

   try:
      import fractions
   except:
      pass

   try:
      import ftplib
   except:
      pass

   try:
      import functools
   except:
      pass

   try:
      import future
   except:
      pass

   try:
      import gc
   except:
      pass

   try:
      import genericpath
   except:
      pass

   try:
      import getopt
   except:
      pass

   try:
      import getpass
   except:
      pass

   try:
      import gettext
   except:
      pass

   try:
      import glob
   except:
      pass

   try:
      import gzip
   except:
      pass

   try:
      import hashlib
   except:
      pass

   try:
      import heapq
   except:
      pass

   try:
      import hmac
   except:
      pass

   try:
      import html
   except:
      pass

   try:
      import http
   except:
      pass

   try:
      import idlelib
   except:
      pass

   try:
      import imaplib
   except:
      pass

   try:
      import imghdr
   except:
      pass

   try:
      import imp
   except:
      pass

   try:
      import importlib
   except:
      pass

   try:
      import inspect
   except:
      pass

   try:
      import io
   except:
      pass

   try:
      import ipaddress
   except:
      pass

   try:
      import isapi
   except:
      pass

   try:
      import itertools
   except:
      pass

   try:
      import json
   except:
      pass

   try:
      import keyword
   except:
      pass

   try:
      import libfuturize
   except:
      pass

   try:
      import libpasteurize
   except:
      pass

   try:
      import linecache
   except:
      pass

   try:
      import locale
   except:
      pass

   try:
      import logging
   except:
      pass

   try:
      import lzma
   except:
      pass

   try:
      import macpath
   except:
      pass

   try:
      import macurl2path
   except:
      pass

   try:
      import mailbox
   except:
      pass

   try:
      import mailcap
   except:
      pass

   try:
      import marshal
   except:
      pass

   try:
      import math
   except:
      pass

   try:
      import mimetypes
   except:
      pass

   try:
      import mmap
   except:
      pass

   try:
      import mmapfile
   except:
      pass

   try:
      import mmsystem
   except:
      pass

   try:
      import modulefinder
   except:
      pass

   try:
      import msilib
   except:
      pass

   try:
      import msvcrt
   except:
      pass

   try:
      import multiprocessing
   except:
      pass

   try:
      import netbios
   except:
      pass

   try:
      import netrc
   except:
      pass

   try:
      import nntplib
   except:
      pass

   try:
      import nt
   except:
      pass

   try:
      import ntpath
   except:
      pass

   try:
      import ntsecuritycon
   except:
      pass

   try:
      import nturl2path
   except:
      pass

   try:
      import numbers
   except:
      pass

   try:
      import odbc
   except:
      pass

   try:
      import opcode
   except:
      pass

   try:
      import operator
   except:
      pass

   try:
      import optparse
   except:
      pass

   try:
      import os
   except:
      pass

   try:
      import parser
   except:
      pass

   try:
      import past
   except:
      pass

   try:
      import pathlib
   except:
      pass

   try:
      import pdb
   except:
      pass

   try:
      import perfmon
   except:
      pass

   try:
      import pickle
   except:
      pass

   try:
      import pickletools
   except:
      pass

   try:
      import pip
   except:
      pass

   try:
      import pipes
   except:
      pass

   try:
      import pkg_resources
   except:
      pass

   try:
      import pkgutil
   except:
      pass

   try:
      import platform
   except:
      pass

   try:
      import plistlib
   except:
      pass

   try:
      import poplib
   except:
      pass

   try:
      import posixpath
   except:
      pass

   try:
      import pprint
   except:
      pass

   try:
      import profile
   except:
      pass

   try:
      import pstats
   except:
      pass

   try:
      import pty
   except:
      pass

   try:
      import py_compile
   except:
      pass

   try:
      import py_version
   except:
      pass

   try:
      import pyclbr
   except:
      pass

   try:
      import pydoc
   except:
      pass

   try:
      import pydoc_data
   except:
      pass

   try:
      import pyexpat
   except:
      pass

   try:
      import pythoncom
   except:
      pass

   try:
      import pywin
   except:
      pass

   try:
      import pywin32_testutil
   except:
      pass

   try:
      import pywintypes
   except:
      pass

   try:
      import queue
   except:
      pass

   try:
      import quopri
   except:
      pass

   try:
      import random
   except:
      pass

   try:
      import rasutil
   except:
      pass

   try:
      import re
   except:
      pass

   try:
      import regcheck
   except:
      pass

   try:
      import regutil
   except:
      pass

   try:
      import reprlib
   except:
      pass

   try:
      import rlcompleter
   except:
      pass

   try:
      import runpy
   except:
      pass

   try:
      import sched
   except:
      pass

   try:
      import select
   except:
      pass

   try:
      import selectors
   except:
      pass

   try:
      import servicemanager
   except:
      pass

   try:
      import setup
   except:
      pass

   try:
      import setuptools
   except:
      pass

   try:
      import shelve
   except:
      pass

   try:
      import shlex
   except:
      pass

   try:
      import shutil
   except:
      pass

   try:
      import signal
   except:
      pass

   try:
      import site
   except:
      pass

   try:
      import smtpd
   except:
      pass

   try:
      import smtplib
   except:
      pass

   try:
      import sndhdr
   except:
      pass

   try:
      import socket
   except:
      pass

   try:
      import socketserver
   except:
      pass

   try:
      import sqlite3
   except:
      pass

   try:
      import sre_compile
   except:
      pass

   try:
      import sre_constants
   except:
      pass

   try:
      import sre_parse
   except:
      pass

   try:
      import ssl
   except:
      pass

   try:
      import sspi
   except:
      pass

   try:
      import sspicon
   except:
      pass

   try:
      import stat
   except:
      pass

   try:
      import statistics
   except:
      pass

   try:
      import string
   except:
      pass

   try:
      import stringprep
   except:
      pass

   try:
      import struct
   except:
      pass

   try:
      import subprocess
   except:
      pass

   try:
      import sunau
   except:
      pass

   try:
      import symbol
   except:
      pass

   try:
      import symtable
   except:
      pass

   try:
      import sys
   except:
      pass

   try:
      import sysconfig
   except:
      pass

   try:
      import tabnanny
   except:
      pass

   try:
      import tarfile
   except:
      pass

   try:
      import telnetlib
   except:
      pass

   try:
      import tempfile
   except:
      pass

   try:
      import test
   except:
      pass

   try:
      import textwrap
   except:
      pass

   try:
      import this
   except:
      pass

   try:
      import threading
   except:
      pass

   try:
      import time
   except:
      pass

   try:
      import timeit
   except:
      pass

   try:
      import timer
   except:
      pass

   try:
      import token
   except:
      pass

   try:
      import tokenize
   except:
      pass

   try:
      import trace
   except:
      pass

   try:
      import traceback
   except:
      pass

   try:
      import tracemalloc
   except:
      pass

   try:
      import tty
   except:
      pass

   try:
      import turtle
   except:
      pass

   try:
      import turtledemo
   except:
      pass

   try:
      import types
   except:
      pass

   try:
      import typing
   except:
      pass

   try:
      import udf
   except:
      pass

   try:
      import unicodedata
   except:
      pass

   try:
      import unittest
   except:
      pass

   try:
      import urllib
   except:
      pass

   try:
      import uu
   except:
      pass

   try:
      import uuid
   except:
      pass

   try:
      import venv
   except:
      pass

   try:
      import warnings
   except:
      pass

   try:
      import wave
   except:
      pass

   try:
      import weakref
   except:
      pass

   try:
      import webbrowser
   except:
      pass

   try:
      import wheel
   except:
      pass

   try:
      import win2kras
   except:
      pass

   try:
      import win32api
   except:
      pass

   try:
      import win32clipboard
   except:
      pass

   try:
      import win32com
   except:
      pass

   try:
      import win32con
   except:
      pass

   try:
      import win32console
   except:
      pass

   try:
      import win32cred
   except:
      pass

   try:
      import win32crypt
   except:
      pass

   try:
      import win32cryptcon
   except:
      pass

   try:
      import win32event
   except:
      pass

   try:
      import win32evtlog
   except:
      pass

   try:
      import win32evtlogutil
   except:
      pass

   try:
      import win32file
   except:
      pass

   try:
      import win32gui
   except:
      pass

   try:
      import win32gui_struct
   except:
      pass

   try:
      import win32help
   except:
      pass

   try:
      import win32inet
   except:
      pass

   try:
      import win32inetcon
   except:
      pass

   try:
      import win32job
   except:
      pass

   try:
      import win32lz
   except:
      pass

   try:
      import win32net
   except:
      pass

   try:
      import win32netcon
   except:
      pass

   try:
      import win32pdh
   except:
      pass

   try:
      import win32pdhquery
   except:
      pass

   try:
      import win32pdhutil
   except:
      pass

   try:
      import win32pipe
   except:
      pass

   try:
      import win32print
   except:
      pass

   try:
      import win32process
   except:
      pass

   try:
      import win32profile
   except:
      pass

   try:
      import win32ras
   except:
      pass

   try:
      import win32rcparser
   except:
      pass

   try:
      import win32security
   except:
      pass

   try:
      import win32service
   except:
      pass

   try:
      import win32serviceutil
   except:
      pass

   try:
      import win32timezone
   except:
      pass

   try:
      import win32trace
   except:
      pass

   try:
      import win32traceutil
   except:
      pass

   try:
      import win32transaction
   except:
      pass

   try:
      import win32ts
   except:
      pass

   try:
      import win32ui
   except:
      pass

   try:
      import win32uiole
   except:
      pass

   try:
      import win32verstamp
   except:
      pass

   try:
      import win32wnet
   except:
      pass

   try:
      import winerror
   except:
      pass

   try:
      import winioctlcon
   except:
      pass

   try:
      import winnt
   except:
      pass

   try:
      import winperf
   except:
      pass

   try:
      import winreg
   except:
      pass

   try:
      import winsound
   except:
      pass

   try:
      import winxpgui
   except:
      pass

   try:
      import winxptheme
   except:
      pass

   try:
      import wsgiref
   except:
      pass

   try:
      import xdrlib
   except:
      pass

   try:
      import xml
   except:
      pass

   try:
      import xmlrpc
   except:
      pass

   try:
      import xxsubtype
   except:
      pass

   try:
      import zipapp
   except:
      pass

   try:
      import zipfile
   except:
      pass

   try:
      import zipimport
   except:
      pass

   try:
      import zlib
   except:
      pass

   try:
      import numpy
   except:
      pass


def alternate_raw_input(prompt=None):
   """Write the prompt to stderr, then call raw_input without a prompt.
    This is to try to mimic better what the python executable does.
   Enter: prompt: prompt to print to stderr."""
   if prompt and len(prompt):
      sys.stderr.write(prompt)
      sys.stderr.flush()
   return input("")


if hasattr(sys, "frozen"):
   delattr(sys, "frozen")
Help = False
DirectCmd = None
ImportSite = True
Interactive = "check"
RunModule = False
ShowVersion = False
SkipFirstLine = False
Start = None
Unbuffered = False
UseEnvironment = True
skip = 0
for i in range(1, len(sys.argv)):
   if DirectCmd is not None:
      break
   if skip:
      skip -= 1
      continue
   arg = sys.argv[i]
   if arg.startswith("-") and arg[1:2]!="-":
      for let in arg[1:]:
         if let=="c":
            DirectCmd = " ".join(sys.argv[i+1+skip:])
            DirectCmd = sys.argv[i+1+skip:]
         elif let=="E":
            UseEnvironment = False
         elif let=="i":
            Interactive = True
         elif let=="m" and i+1<len(sys.argv):
            RunModule = sys.argv[i+1]
            skip = 1
         elif let=="S":
            ImportSite = False
         elif let=="u":
            Unbuffered = True
         elif let=="V":
            ShowVersion = True
         elif let=="x":
            SkipFirstLine = True
         elif let in ("E", "O"):
            # ignore these options
            pass
         else:
            Help = True
   elif arg=="--all":
      continue
   elif arg=="--help" or arg=="-h" or arg=="/?":
      Help = True
   elif arg=="--multiprocessing-fork":
      skip = 1
      import multiprocessing.forking
      multiprocessing.forking.freeze_support()
   elif arg=="--version":
      ShowVersion = True
   elif arg.startswith("-"):
      Help = True
   elif not Start:
      Start = i
      break
if Help:
   print("""Stand-Alone Python Interpreter

Syntax: py.exe [--all] [--help] [-c (cmd) | -m (module) | (python file) [arg]]
               [-i] [-S] [-u] [-V] [-x]
               [--multiprocessing-fork (handle)]

--all attempts to import all modules.
-c runs the remaining options as a program.
-E ignores environment variables.
-i forces a prompt even if stdin does not appear to be a terminal; also
  PYTHONINSPECT=x
--help, -h, or /? prints this message.
-m runs the specified python module.
--multiprocessing-fork supports the multiprocessing module.
-S supresses importing the site module
-u runs in unbuffered mode; also PYTHONUNBUFFERED=x
-V prints the version and exits (--version also works).
-x skips the first line of a source file.
If no file is specified and stdin is a terminal, the interactive interpreter is
  started.""")
   #print sys.argv, repr(sys.argv)
   sys.exit(0)
if ShowVersion:
   from py_version import Version, Description
   print("%s, Version %s"%(Description,Version))
   sys.exit(0)
if Interactive=="check" and UseEnvironment:
   if os.environ.get("PYTHONINSPECT"):
      Interactive = True
if Unbuffered is False and UseEnvironment:
   if os.environ.get("PYTHONUNBUFFERED"):
      Unbuffered = True
if Unbuffered:
   sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
   sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
   sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)
if ImportSite:
   import site
# Generate the globals/locals environment
globenv = {}
for key in list(globals().keys()):
   if key.startswith("_"): # or key=="AllModules":
      globenv[key] = globals()[key]
if Start:
   sys.argv = sys.argv[Start:]
   __name__ = "__main__"
   __file__ = sys.argv[0]
   sys.path[0:0] = [os.path.split(__file__)[0]]
   # If I try to use the simplified global dictionary, multiprocessing doesn't
   # work.
   if not SkipFirstLine:
      #execfile(sys.argv[0], globenv)
      exec(compile(open(sys.argv[0]).read(), sys.argv[0], 'exec'))
   else:
      fptr = open(sys.argv[0])
      discard = fptr.readline()
      src = fptr.read()
      fptr.close()
      #exec src in globenv
      #exec src
elif RunModule:
   import runpy
   runpy.run_module(RunModule, run_name='__main__')
elif DirectCmd:
   sys.path[0:0] = [""]
   sys.argv = DirectCmd
   exec(DirectCmd[0], globenv)
else:
   if Interactive=="check":
      Interactive = sys.stdin.isatty()
   sys.path[0:0] = [""]
   if Interactive:
      import code
      cons = code.InteractiveConsole(locals=globenv)
      if not sys.stdout.isatty():
         cons.raw_input = alternate_raw_input
         if not Unbuffered:
            sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
            sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)
      cons.interact()
   elif False:
      # This will run code as it comes it, rather than wait until it has parsed
      # it all; it doesn't seem to be what the main python interpreter ever
      # does, however.
      import code
      interp = code.InteractiveInterpreter(locals=globenv)
      src = []
      for line in sys.stdin:
         if not len(line.rstrip("\r\n")):
            continue
         if line.startswith("#"):
            continue
         if line.rstrip("\r\n")[0:1] not in (" ", "\t"):
            if len(src):
               interp.runsource("".join(src), "<stdin>")
               src = []
         src.append(line)
      if len(src):
         interp.runsource("".join(src))
   else:
      src = sys.stdin.read()
      # This doesn't work the way I expect for some reason
      #interp = code.InteractiveInterpreter(locals=globenv)
      #interp.runsource(src, "<stdin>")
      # But an exec works fine
      exec(src, globenv)
