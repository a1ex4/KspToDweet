import cx_Freeze
import sys
import pyksp
import dweepy
from requests import *
import requests.certs
import requests.packages

# base = None

# if sys.platform == 'win32':
#     base =  "Win32GUI"
    
executables = [cx_Freeze.Executable("ksp_dweet.py")]

cx_Freeze.setup(
    name ="ksp_dweet",
    options = {"build_exe":{"packages":["pyksp","dweepy", "requests"],"include_files":["cacert.pem"] }},
    executables = executables
    )   