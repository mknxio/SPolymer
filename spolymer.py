import sublime
import sublime_plugin

from SPolymer.linter import SploymerLinter


class Spolymer(sublime_plugin.EventListener):
    """
        Main listener class that handles user events
        and launch corresponding processes.
    """

    linter = SploymerLinter()

    def on_modified(self, view):
        print('============= SPOLYMER DEBUG =============')

        view_content = view.substr(sublime.Region(0, view.size()))
        # Launch lint processes
        self.linter.lint_html_imports(view_content)

        print('========== SPOLYMER DEBUG / END ==========')
