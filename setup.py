from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="booleanfix",
    version="1.2.0",
    description="Fix for boolean variables in Python",
    long_description=long_description,
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
