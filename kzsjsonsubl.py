import sublime
import sublime_plugin
import json


class KzsJsonSublCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selected_regions = self.view.sel()

        if not any(not region.empty() for region in selected_regions):
            entire_content = self.view.substr(sublime.Region(0, self.view.size()))
            selected_text = entire_content
        else:
            selected_text = ''.join(self.view.substr(region) for region in selected_regions)

        pos = selected_text.index('{')
        selected_text = selected_text[pos:]
        pos = selected_text.rindex('}')
        selected_text = selected_text[0:pos + 1]
        selected_text = selected_text.replace('\\"\\"', '""')
        selected_text = selected_text.replace('\\"', '"')
        selected_text = selected_text.replace('\\n', '')

        try:
            formatted_json = json.dumps(json.loads(selected_text), indent=4)
            if not sublime.ok_cancel_dialog(f"{formatted_json}", "Confirmar"):
                return

            if not any(not region.empty() for region in selected_regions):
                self.view.replace(edit, sublime.Region(0, self.view.size()), formatted_json)
            else:
                for region in selected_regions:
                    self.view.replace(edit, region, formatted_json)
        except json.JSONDecodeError:
            sublime.message_dialog("Texto não é um JSON válido.")
