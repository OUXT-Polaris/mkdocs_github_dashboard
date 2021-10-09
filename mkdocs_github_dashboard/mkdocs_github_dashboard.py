"""Main module."""
from mkdocs.plugins import BasePlugin
import re

class MkDocsGithubDashboardPlugin(BasePlugin):
    def on_page_markdown(self, markdown, **kwargs):
        for m in re.finditer(r'@github_dashboard\(.+?\)', markdown, re.MULTILINE):
            replace_target = m.group()
            packages = replace_target[18:len(replace_target)-1].split(',')
            for package in packages:
                print(package)
        return markdown