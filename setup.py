"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Arbitor.py']
DATA_FILES = ['']
OPTIONS = {'argv_emulation': True, 'iconfile': '/Users/Rahul/Kaggle/Arbitor/icon.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    description="Mac app to download subtitles for a given movie.",
    url="https://github.com/RahulShivkumar/Arbitor/",
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
