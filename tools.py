# -*- coding: utf-8 -*-
# Module: default
# Author: cache-sk
# Created on: 26.02.2021
# License: AGPL v.3 https://www.gnu.org/licenses/agpl-3.0.html

import sys, os, io, math
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import traceback
import shutil

try:
    from xbmc import translatePath
except ImportError:
    from xbmcvfs import translatePath

#_userdata_path = translatePath('special://userdata/')
#_database_path = translatePath('special://userdata/Database')
#_addon_data = translatePath('special://userdata/addon_data')
_thumbnail_path = translatePath('special://userdata/Thumbnails')
#_cache_path = os.path.join(translatePath('special://home'), 'cache')
#_temp_path = os.path.join(translatePath('special://home'), 'temp')
#_addons_path = os.path.join(translatePath('special://home'), 'addons')
_packages_path = os.path.join(translatePath('special://home/addons'), 'packages') 

def removeFolderContent(translated_path, remove_folders = True):
    for root, dirs, files in os.walk(translated_path):
        for f in files:
            try:
                os.unlink(os.path.join(root, f))
            except:
                pass
        if remove_folders:
            for d in dirs:
                shutil.rmtree(os.path.join(root, d),ignore_errors=True, onerror=None)

def getFolderSize(translated_path):
    total_size = 0
    for root, dirs, files in os.walk(translated_path):
        for f in files:
            fp = os.path.join(root, f)
            if os.path.isfile(fp):
                total_size += os.path.getsize(fp)
    return total_size

def getHumanReadableFolderSize(translated_path):
    unit = 'B'
    size = float(getFolderSize(translated_path))
    if size > 1024:
        size = size / 1024
        unit = 'KiB'
    if size > 1024:
        size = size / 1024
        unit = 'MiB'
    if size > 1024:
        size = size / 1024
        unit = 'GiB'
    if size > 1024:
        size = size / 1024
        unit = 'TiB'
    return str(int(math.ceil(size))) + ' ' + unit 