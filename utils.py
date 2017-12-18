import re

class SpolymerParser():
    """
        DocString
    """
    @staticmethod
    def parse_html_imports(content):
        """
            Parse the given text content to extract valid HTML imports tags.
            A valid import is a <link> tag composed of a 'rel="import"' attr.
            and an "href" attr. with any character in it.

            Args:
                content (str): The content to parse.

            Returns:
                list: A list of 'dict' representations of imports.
        """
        rgx_html_import = '(<link +.*rel=\"import\".*\/?>)'
        matches = re.findall(rgx_html_import, content, re.I)
        imports = []
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
                imports.append(trimd_tag)
        return imports
