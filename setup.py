#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 
    'mkdocs>=1.1.2',
    'python-github-api',
    'tabulate',
    'pandas'
]

test_requirements = [ ]

setup(
    author="mkdocs-github-dashboard",
    author_email='ms.kataoka@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mkdocs_github_dashboard',
    name='mkdocs_github_dashboard',
    packages=find_packages(include=['mkdocs_github_dashboard', 'mkdocs_github_dashboard.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hakuturu583/mkdocs_github_dashboard',
    version='0.2.2',
    zip_safe=False,
    entry_points={
        'mkdocs.plugins': [
            'github-dashboard = mkdocs_github_dashboard.mkdocs_github_dashboard:MkDocsGithubDashboardPlugin'
        ]
    }
)
