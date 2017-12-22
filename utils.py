import re
import sublime


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
                if attr and ('=' in attr) and (attr != '>' and attr != '/>'):
                    if attr[:1] == '<':
                        attr = attr[1:]
                    if attr[-2:] == '/>':
                        attr = attr[:-2]
                    if attr[-1:] == '>':
                        attr = attr[:-1]
                    # Build obj. representation of trimmed tag
                    if attr != 'link':
                        attr = attr.split("=")
                        if attr[1][0:1] == '"' and attr[1][-1:] == '"':
                            trimd_tag[attr[0]] = attr[1][1:-1]
                            trimd_tag['_'] = 'link'

            # Check if the current import statement is valid, then store it
            has_rel_import = 'rel' in trimd_tag and trimd_tag['rel'] == 'import'
            has_href = 'href' in trimd_tag and trimd_tag['href']
            if has_rel_import and has_href:
                imports.append(trimd_tag)
        return imports

class SpolymerUtils():
    """
        DocString
    """
    @staticmethod
    def get_active_project_path():
        """
            DocString
        """
        import os
        window = sublime.active_window()
        folders = window.folders()
        if len(folders) == 1:
            return folders[0]
        else:
            active_view = window.active_view()
            active_file_name = active_view.file_name() if active_view else None
            if not active_file_name:
                return folders[0] if len(folders) else os.path.expanduser("~")
            for folder in folders:
                if active_file_name.startswith(folder):
                    return folder
            return os.path.dirname(active_file_name)
