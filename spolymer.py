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
        print('\n\n============= SPOLYMER DEBUG =============')

        # Launch lint processes
        self.linter.lint_html_imports(view)

        print('========== SPOLYMER DEBUG / END ==========')
