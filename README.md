## YamlToJson Sublime Text plugin

### Installation

- Package Control: Coming soon.
- Manual installation:

        cd <Data Directory>/Packages
        git clone https://github.com/ryandao/SublimeYamlToJson.git

The location of `Data Directory` can be found in this [document](http://sublimetext.info/docs/en/basic_concepts.html) or simply just go to `Preferences > Browse Packages`. 

### Usage

The default shortcuts are `["ctrl+y", "ctrl+j"]` (pressing `y` and then `j` while holding `ctrl`) for converting YAML to JSON and `["ctrl+j", "ctrl+y"]` for JSON to YAML. It's the same for OSX, Windows, and Linux. To customize, just add this configuration to your key bindings and change accordingly:

    {
        "keys": [
            "ctrl+y", "ctrl+j"
        ],
        "command": "yaml_to_json"
    },
    {
        "keys": [
            "ctrl+j", "ctrl+y"
        ],
        "command": "json_to_yaml"
    }

