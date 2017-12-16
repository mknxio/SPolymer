import re
import os


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
        rgx_html_import = '(<link +.*rel=\"import\".*\/?>)'
        matches = re.findall(rgx_html_import, content, re.I)
        for match in matches:
            match = match.split(' ')
            # Remove unwanted withspaces & characters
            trimd_tag = {}
            for attr in match:
                if attr and attr != '>' and attr != '/>':
                    if attr[:1] == '<':
                        attr = attr[1:]
                    if attr[-2:] == '/>':
                        attr = attr[:-2]
                    if attr[-1:] == '>':
                        attr = attr[:-1]
                    # Build obj. representation of trimmed tag
                    trimd_tag['_'] = 'link'
                    if attr != 'link':
                        attr = attr.split("=")
                        trimd_tag[attr[0]] = attr[1][1:-1]
            # Check if the current import statement is valid, then store it
            has_rel_import = 'rel' in trimd_tag and trimd_tag['rel'] == 'import'
            has_href = 'href' in trimd_tag and trimd_tag['href']
            if has_rel_import and has_href:
                self._html_imports.append(trimd_tag)
        print(self._html_imports)

