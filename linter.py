import re


class SploymerLinter():
    """
        DocString
    """

    _rgx_html_import = '(<link +({}|{}).*\/?>)'.format(
                            'rel="import" +(.* +)?href=".+"',
                            'href=".+" +(.* +)?rel="import"?')

    def lint_html_imports(self, content):
        pattern = re.compile(self._rgx_html_import, re.I | re.M)
        matches = pattern.match(content)
        if matches:
            print(pattern.match(content).group(1))
