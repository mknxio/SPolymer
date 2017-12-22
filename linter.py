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

        view_filepath = view.file_name()
        if view_filepath:
            view_filedir = view_filepath[0:view_filepath.rfind('/')]
            import_filepath = None
            for imp in self._html_imports:
                if imp['href'][0:1] == '/':
                    pass
                elif imp['href'][0:2] == './':
                    pass
                elif imp['href'][0:3] == '../':
                    pass
                else:
                    import_filepath = '{}/{}'.format(view_filedir, imp['href'])
                print(import_filepath)
