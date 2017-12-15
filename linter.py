import re
import os


class SploymerLinter():
    """
        DocString
    """

    _errors = []

    def lint_html_imports(self, content):
        """
            Used to perform HTML imports checking.
            This method will parse the given HTML content and extract HTML
            import statements, then will check for valid file paths, and
            display an error tooltip if paths are not valid.
        """
        rgx_html_import = '(<link +({}|{}).*\/?>)'.format(
                                            'rel="import" +(.+ +)?(href=".+")',
                                            '(href=".+") +(.+ +)?rel="import"')
        matches = re.findall(rgx_html_import, content, re.I)

