import os
import sublime

from SPolymer.utils import SpolymerParser, SpolymerUtils


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
            display an error if not.
        """
        content = view.substr(sublime.Region(0, view.size()))
        self._view = view
        self._html_imports = SpolymerParser.parse_html_imports(content)

        view_filepath = view.file_name()
        if view_filepath:
            view_filedir = view_filepath[0:view_filepath.rfind('/')]
            import_filepath = None
            project_path = SpolymerUtils.get_active_project_path()
            for imp in self._html_imports:
                if imp['href'][0:1] == '/':
                    import_filepath = '{}/{}'.format(
                                                project_path,
                                                imp['href'][1:])
                elif imp['href'][0:2] == './':
                    import_filepath = '{}/{}'.format(
                                                view_filedir,
                                                imp['href'][2:])
                elif imp['href'][0:3] == '../':
                    import_filepath = '{}/{}'.format(
                                                view_filedir[0:view_filedir.rfind('/')],
                                                imp['href'][3:])
                else:
                    import_filepath = '{}/{}'.format(view_filedir, imp['href'])
                print(import_filepath)
