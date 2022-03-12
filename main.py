# --------------------------------------------------------------------------------------
# This is the interactive scripting language "RPGScript" for Python 3
# CC-Celeste (Creative Commons 2022)
# Copyright 2022 © Celeste aka. 73chn0m4nc3r
# Sourcecode is available on GitHub https://www.github.com/celeste-42bit/allTheJazz
# --------------------------------------------------------------------------------------

from choiceeng import *
from fileops import display

# --------------------DEFINE START-POINT----------------------
# Just enter the filename of your first text file :)
# ------------------------------------------------------------
startpoint = "N_start.txt"
# ------------------------------------------------------------


# -----------------------START-SCRIPT-------------------------
# The script always starts with your start-point and can be continued freely from there on out!
# After making the first choice, the start-script is done and you have to continue all the different scripts in
# "scripts.py". Define a script like that: "def script_name(variables, used, by, the, script, player_name, age): "
# ------------------------------------------------------------
display(startpoint)
display("C_choice.txt")
mkch2("O_01.txt", "O_02.txt")
# ------------------------------------------------------------
