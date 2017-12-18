import os
import sublime

from SPolymer.utils import SpolymerParser


class SploymerLinter():
    """
        DocString
    """

    _view = None
    _html_imports = []
    _errors = []

    def lint_html_imports(self, view):
        """
            Used to perform HTML imports checking.
            This method will parse the given HTML content and extract HTML
            import statements, then will check for valid file paths, and
            display an error tooltip if paths are not valid.
        """
        content = view.substr(sublime.Region(0, view.size()))
        self._view = view
        self._html_imports = SpolymerParser.parse_html_imports(content)

        print(view.file_name()[0:view.file_name().rfind('/')])
        for imp in self._html_imports:
            print(os.path.isfile(imp['href']))
