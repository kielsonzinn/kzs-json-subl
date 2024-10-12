import sublime
import sublime_plugin
import json


class KzsjsonsublCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selected_regions = self.view.sel()

        if not any(not region.empty() for region in selected_regions):
            entire_content = self.view.substr(sublime.Region(0, self.view.size()))
            selected_text = entire_content
        else:
            selected_text = ''.join(self.view.substr(region) for region in selected_regions)

        character_start_obj = "{"
        character_start_array = "["

        if character_start_obj not in selected_text and character_start_array not in selected_text:
            sublime.message_dialog("JSON incorrect")
            return False

        character_end = None
        character_start = None

        if character_start_array in selected_text:
            pos_obj = None
            pos_array = selected_text.index(character_start_array)

            if character_start_obj in selected_text:
                pos_obj = selected_text.index(character_start_obj)

            if pos_obj is None or pos_array < pos_obj:
                character_end = ']'
                character_start = character_start_array

        if character_end is None or character_start is None:
            character_end = '}'
            character_start = character_start_obj

        pos = selected_text.index(character_start)
        selected_text = selected_text[pos:]
        pos = selected_text.rindex(character_end)
        selected_text = selected_text[0:pos + 1]
        selected_text = selected_text.replace('\\"\\"', '""')
        selected_text = selected_text.replace('\\"', '"')
        selected_text = selected_text.replace('\\n', '')

        try:
            formatted_json = json.dumps(json.loads(selected_text), indent=4, ensure_ascii=False)

            if not any(not region.empty() for region in selected_regions):
                self.view.replace(edit, sublime.Region(0, self.view.size()), formatted_json)
            else:
                for region in selected_regions:
                    self.view.replace(edit, region, formatted_json)
        except json.JSONDecodeError:
            sublime.message_dialog("JSON incorrect")
