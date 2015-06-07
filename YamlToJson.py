import sublime, sublime_plugin, platform, json

try:
  # For Sublime Test 3
  from . import yaml3 as yaml
except ValueError:
  # For Sublime Test 2
  import yaml2 as yaml

class BaseCommand(sublime_plugin.TextCommand):
  def get_selections(self):
    selections = []
    for region in self.view.sel():
      if not region.empty():
        selections.append(region)

    if len(selections) == 0:
      selections.append(sublime.Region(0, self.view.size()))

    return selections

class YamlToJsonCommand(BaseCommand):
  def run(self, edit):
    for selection in self.get_selections():
      try:
        result = yaml.load(self.view.substr(selection))
        json_str = json.dumps(
          result,
          indent=2,
          ensure_ascii=False,
          sort_keys=False,
        )

        self.view.replace(edit, selection, json_str)
      except Exception as e:
        sublime.status_message(str(e))

class JsonToYamlCommand(BaseCommand):
  def run(self, edit):
    for selection in self.get_selections():
      try:
        result = json.loads(self.view.substr(selection))
        yaml_str = yaml.safe_dump(
          result,
          indent=2,
          default_flow_style=False,
        )

        self.view.replace(edit, selection, yaml_str)
      except Exception as e:
        sublime.status_message(str(e))
