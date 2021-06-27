# coding: utf-8

from lib.library import *
from tkinter import *
import os



root = textEditor("root", "content")
root.create()
root.add_text()
root.add_menu()
root.generate()