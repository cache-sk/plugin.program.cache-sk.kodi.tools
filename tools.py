# -*- coding: utf-8 -*-
# Module: default
# Author: cache-sk
# Created on: 26.02.2021
# License: AGPL v.3 https://www.gnu.org/licenses/agpl-3.0.html

import sys, os, io, math
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import traceback
import shutil

#_userdata_path = xbmc.translatePath('special://userdata/')
#_database_path = xbmc.translatePath('special://userdata/Database')
#_addon_data = xbmc.translatePath('special://userdata/addon_data')
_thumbnail_path = xbmc.translatePath('special://userdata/Thumbnails')
#_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
#_temp_path = os.path.join(xbmc.translatePath('special://home'), 'temp')
#_addons_path = os.path.join(xbmc.translatePath('special://home'), 'addons')
_packages_path = os.path.join(xbmc.translatePath('special://home/addons'), 'packages') 

def removeFolderContent(translated_path):
    for root, dirs, files in os.walk(translated_path):
        for f in files:
            try:
                os.unlink(os.path.join(root, f))
            except:
                pass
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