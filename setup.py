from setuptools import setup, find_packages

setup(
    name="booleanfix",
    version="1.0.0",
    description="Fix for boolean variables in Python",
    long_description="If you come from another programming language, you may have noticed that Python's boolean variables are a bit different. This module aims to fix that, by giving you boolean variables like you're used to.",
    long_description_content_type="text/markdown",
    url="https://github.com/EDM115/booleanfix",
    author="EDM115",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
	project_urls={
        "Documentation": "https://github.com/EDM115/booleanfix",
        "Funding": "https://github.com/EDM115#support-me-",
        "Source": "https://github.com/EDM115/booleanfix",
        "Tracker": "https://github.com/EDM115/booleanfix/issues",
    },
    packages=find_packages(),
)
