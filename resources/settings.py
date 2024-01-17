import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon(id='plugin.video.myvideolinks')

def get_setting(setting_id):
    return addon.getSetting(setting_id)

def set_setting(setting_id, value):
    addon.setSetting(setting_id, value)

# Example usage:
default_search_query = get_setting('search_query')
print(f"Default Search Query: {default_search_query}")

# Modify and save settings:
new_search_query = xbmcgui.Dialog().input('Enter new default search query:', default_search_query)
set_setting('search_query', new_search_query)
print("Settings updated.")

