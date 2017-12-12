import sublime
import sublime_plugin

from SPolymer.linter import SploymerLinter


class Spolymer(sublime_plugin.EventListener):
    """
        Main listener class that handles user events
        and performs corresponding actions.
    """

    linter = SploymerLinter()

    def on_modified(self, view):
        view_content = view.substr(sublime.Region(0, view.size()))
        # Launch lint processes
        self.linter.lint_html_imports(view_content)
