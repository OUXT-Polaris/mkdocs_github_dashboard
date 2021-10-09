# Mkdocs Github Dashboard Plugin

Mkdocs Plugin for generating tables of repository infomations in github.

## How it works
1. Get github access token via environment variable.
1. Find sentence like "@github_dashboard(OUXT-Polaris/behavior_tree_action_builder,OUXT-Polaris/color_names)" in your mkdocs file.
1. Generate markdown tables for the commna-separated repositories in ()