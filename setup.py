import sys
from setuptools import setup, find_packages

setup(
    name="whtranscripts",
    version="0.0.0",
    description="whtranscripts helps you fetch and parse transcripts from the American Presidency Project's press-briefing and presidential-news-conference transcripts.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3"
    ],
    keywords="white house news conferences press briefings american presidency project",
    author="John Templon",
    author_email="john.templon@buzzfeed.com",
    url="http://github.com/buzzfeednews/whtranscripts/",
    license="MIT",
    packages=find_packages(exclude=["test",]),
    namespace_packages=[],
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "requests",
        "lxml",
        "cssselect"
    ],
    tests_require=[
        "nose",
    ],
    test_suite="test",
    entry_points={
        "console_scripts": [
        ]
    }
)