import sublime
import sublime_plugin


class InsertAtasciiCommand(sublime_plugin.TextCommand):
    """Insert an ATASCII Unicode character at the current cursor position."""

    def run(self, edit, character=""):
        for region in self.view.sel():
            self.view.insert(edit, region.begin(), character)


class InvertAtasciiCommand(sublime_plugin.TextCommand):
    """Invert the ATASCII character at the current cursor position."""

    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                region = sublime.Region(region.begin(), region.begin() + 1)
            text = self.view.substr(region)
            inverted = self._invert(text)
            self.view.replace(edit, region, inverted)

    def _invert(self, text):
        result = []
        for ch in text:
            code = ord(ch)
            # ATASCII inverse video is toggled by XOR with 0x80
            if (0x20 <= code <= 0x7F) or (0xA0 <= code <= 0xFF):
                result.append(chr(code ^ 0x80))
            else:
                result.append(ch)
        return "".join(result)
