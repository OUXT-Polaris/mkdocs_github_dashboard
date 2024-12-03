"""Main module."""
from mkdocs.plugins import BasePlugin
from python_github.python_github import Github
import re
import pandas as pd
import os

def is_env_var_true(env_var_name: str) -> bool:
    value = os.environ.get(env_var_name, "").strip().lower()
    if value == "true":
        return True
    elif value == "false":
        return False
    return False

class MkDocsGithubDashboardPlugin(BasePlugin):
    def on_page_markdown(self, markdown, **kwargs):
        if not is_env_var_true("SHOW_DASHBOARD"):
            return markdown
        github = Github()
        for m in re.finditer(r'@github_dashboard\(.+?\)', markdown, re.MULTILINE):
            replace_target = m.group()
            #print(replace_target)
            packages = replace_target[18:len(replace_target)-1].split(',')
            workflow_dict = {}
            pull_request_dict = {}
            for package in packages:
                package_url = "[" + package + "](https://github.com/" + package + ")"
                workflow_dict[package_url] = {}
                pull_request_text = {}
                print("processing package : " + package)
                if "workflows" in github.workflow.get(package).keys():
                    for workflow in github.workflow.get(package)["workflows"]:
                        if workflow["state"] == "active" and workflow["name"] != "pages-build-deployment":
                            workflow_dict[package_url][workflow["name"]] = "![Not Found](" + workflow["badge_url"] + ")"
                pull_request_index = 0
                for pull_request in github.pull_request.get(package):
                    text = "[" + pull_request["title"] + "](" + pull_request["html_url"] + ")"
                    pull_request_text[pull_request_index] = text
                    pull_request_index = pull_request_index + 1
                if len(pull_request_text) != 0:
                    pull_request_dict[package_url] = pull_request_text
            badge_urls = pd.DataFrame().from_dict(workflow_dict)
            pull_requests = pd.DataFrame().from_dict(pull_request_dict)
            #print(pull_requests.T.to_markdown())
            markdown = markdown.replace(replace_target, badge_urls.T.to_markdown() + "\n\n" + pull_requests.T.to_markdown())
        return markdown

if __name__ == '__main__':
    plugin = MkDocsGithubDashboardPlugin()
    #text = "@github_dashboard(OUXT-Polaris/color_names,OUXT-Polaris/data_buffer,OUXT-Polaris/dynamixel_hardware_interface,OUXT-Polaris/geographic_conversion,OUXT-Polaris/geographic_info)"
    text = "@github_dashboard(OUXT-Polaris/dynamixel_hardware_interface,OUXT-Polaris/geographic_info)"
    markdown = plugin.on_page_markdown(text)
    print("")
    print(markdown)
    #plugin.on_page_markdown(text)
