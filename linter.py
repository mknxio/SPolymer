import os

from SPolymer.utils import SpolymerParser


class SploymerLinter():
    """
        DocString
    """

    _html_content = ''
    _html_imports = []
    _errors = []

    def lint_html_imports(self, content):
        """
            Used to perform HTML imports checking.
            This method will parse the given HTML content and extract HTML
            import statements, then will check for valid file paths, and
            display an error tooltip if paths are not valid.
        """
        self._html_content = content
        self._html_imports = SpolymerParser.parse_html_imports(content)
        print(self._html_imports)
