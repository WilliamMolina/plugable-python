from yapsy.PluginManager import PluginManager
import json, sys

# Load the plugins from the plugin directory.
manager = PluginManager()
manager.setPluginPlaces(["plugins"])
manager.collectPlugins()

def main(file):    
    # Loop round the plugins and print their names.
    message = json.loads(open(file).read())
    plugin = manager.getPluginByName(message['type'])
    if plugin:
        plugin.plugin_object.print_name()
        plugin.plugin_object.retry(**message['target'], message = message.get('message'))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])    
    
