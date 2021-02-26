# -*- coding: utf-8 -*-
# Module: default
# Author: cache-sk
# Created on: 26.02.2021
# License: AGPL v.3 https://www.gnu.org/licenses/agpl-3.0.html

import sys, os, io
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import traceback
import tools

_addon = xbmcaddon.Addon()

def packages():
    if xbmcgui.Dialog().yesno(_addon.getAddonInfo('name'), "Delete all packages?"):
        tools.removeFolderContent(tools._packages_path)
        xbmcgui.Dialog().ok(_addon.getAddonInfo('name'), "Packages (hopefully) removed. Please restart Kodi.")

def thumbnails():
    if xbmcgui.Dialog().yesno(_addon.getAddonInfo('name'), "Delete all thumbnails?"):
        tools.removeFolderContent(tools._thumbnail_path)
        xbmcgui.Dialog().ok(_addon.getAddonInfo('name'), "Thumbnails (hopefully) removed. Please restart Kodi.")

def menu():
    xbmcplugin.addDirectoryItem(_handle, get_url(action='packages'), xbmcgui.ListItem(label='Clean packages'), False)
    xbmcplugin.addDirectoryItem(_handle, get_url(action='thumbnails'), xbmcgui.ListItem(label='Clean thumbnails'), False)
    xbmcplugin.endOfDirectory(_handle)

def main():
    try:
        selected = xbmcgui.Dialog().select(_addon.getAddonInfo('name'), ['Clean packages','Clean thumbnails'])
        if selected == 0:
            packages()
        elif selected == 1:
            thumbnails()

    except Exception as e:
        xbmcgui.Dialog().ok(_addon.getAddonInfo('name'), str(e))
        traceback.print_exc()

if __name__ == '__main__':
    main()
