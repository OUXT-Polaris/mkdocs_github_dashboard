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
            print(replace_target)
            packages = replace_target[18:len(replace_target)-1].split(',')
            dict = {}
            for package in packages:
                package_url = "[" + package + "](https://github.com/" + package + ")"
                dict[package_url] = {}
                print("processing package : " + package)
                print(github.workflow.get(package))
                if "workflows" in github.workflow.get(package).keys():
                    for workflow in github.workflow.get(package)["workflows"]:
                        if workflow["state"] == "active":
                            dict[package_url][workflow["name"]] = "![Not Found](" + workflow["badge_url"] + ")"
            badge_urls = pd.DataFrame().from_dict(dict)
            markdown = markdown.replace(replace_target, badge_urls.T.to_markdown())

        return markdown

if __name__ == '__main__':
    plugin = MkDocsGithubDashboardPlugin()
    text = "@github_dashboard(OUXT-Polaris/color_names,OUXT-Polaris/data_buffer,OUXT-Polaris/dynamixel_hardware_interface,OUXT-Polaris/geographic_conversion,OUXT-Polaris/geographic_info,OUXT-Polaris/geometry_msgs_data_buffer,OUXT-Polaris/hermite_path_planner,OUXT-Polaris/image_processing_utils,OUXT-Polaris/joy_to_twist,OUXT-Polaris/lua_vendor,OUXT-Polaris/message_synchronizer,OUXT-Polaris/miniv_control,OUXT-Polaris/miniv_description,OUXT-Polaris/navi_sim,OUXT-Polaris/nmea_gps_driver,OUXT-Polaris/nmea_hardware_interface,OUXT-Polaris/nmea_to_geopose,OUXT-Polaris/odom_frame_publisher,OUXT-Polaris/ouxt_common,OUXT-Polaris/pcl_apps,OUXT-Polaris/perception_bringup,OUXT-Polaris/playstation_controller_drivers,OUXT-Polaris/quaternion_operation,OUXT-Polaris/realsense_hardware_interface,OUXT-Polaris/robotx_behavior_tree,OUXT-Polaris/robotx_costmap_calculator,OUXT-Polaris/robotx_ekf,OUXT-Polaris/scan_segmentation,OUXT-Polaris/sol_vendor,OUXT-Polaris/tcp_sender,OUXT-Polaris/unisim_ros2_control,OUXT-Polaris/usv_controller)"
    print(plugin.on_page_markdown(text))
    #plugin.on_page_markdown(text)