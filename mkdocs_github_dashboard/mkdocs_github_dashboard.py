"""Main module."""
from mkdocs.plugins import BasePlugin
from python_github.python_github import Github
import re
import pandas as pd

class MkDocsGithubDashboardPlugin(BasePlugin):
    def on_page_markdown(self, markdown, **kwargs):
        github = Github()
        for m in re.finditer(r'@github_dashboard\(.+?\)', markdown, re.MULTILINE):
            replace_target = m.group()
            packages = replace_target[18:len(replace_target)-1].split(',')
            dict = {}
            for package in packages:
                package_url = "[" + package + "](https://github.com/" + package + ")"
                dict[package_url] = {}
                for workflow in github.workflow.get(package)["workflows"]:
                    if workflow["state"] == "active":
                        dict[package_url][workflow["name"]] = "![Not Found](" + workflow["badge_url"] + ")"
            badge_urls = pd.DataFrame().from_dict(dict)
            markdown = markdown.replace(replace_target, badge_urls.T.to_markdown())

        return markdown