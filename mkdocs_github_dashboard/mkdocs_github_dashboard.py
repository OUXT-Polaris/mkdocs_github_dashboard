"""Main module."""
from mkdocs.plugins import BasePlugin

class MkDocsGithubDashboardPlugin(BasePlugin):
    def on_page_markdown(self, markdown, **kwargs):
        return markdown