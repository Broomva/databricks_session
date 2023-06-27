import io
import os
import json
import setuptools
import glob
import sys
from setuptools import find_packages, find_namespace_packages

if sys.version_info < (3, 8):
    find_namespace_packages()
    print("Error: databricks_session does not support this version of Python.")
    print("Please upgrade to Python 3.8 or higher.")
    sys.exit(1)


def prepare_data_files(directory, extensions):
    files = []
    for ext in extensions:
        files.extend(glob.glob(f"{directory}/*.{ext}"))
    return files


data_files_structure = [
    (
        "databricks_session",
        prepare_data_files(
            "databricks_session",
            ["csv", "sql", "txt", "md", "html", "css", "json", "yaml", "faiss", "pkl"],
        ),
    ),
]

# Package metadata.
name = "databricks_session"
description = (
    "A simple util to get a spark and mlflow session objects from an .env file"
)
# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 3 - Alpha"

with open("requirements.txt") as f:
    required = f.read().splitlines()
extras = {"protobuf": ["protobuf<5.0.0dev"]}

# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

version = {}
with open(os.path.join(package_root, "package.json")) as f:
    version = json.loads(f.read())["version"]

readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Carlos D. Escobar-Valbuena",
    author_email="carlosdavidescobar@gmail.com",
    license="MIT",
    classifiers=[
        release_status,
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules :: Databricks",
    ],
    packages=find_packages(),
    install_requires=required,
    extras_require=extras,
    python_requires=">=3.8",
    include_package_data=True,
    setup_requires=["setuptools", "wheel"],
    tests_require=["pytest"],
    test_suite="tests",
    zip_safe=False,
    url="https://github.com/Broomva/databricks_session",
    package_data={
        "databricks_session": [
            "*.json",
            "*.yaml",
            "*.sql",
            "*.csv",
            "*.txt",
            "*.md",
            "*.html",
            "*.css",
            "*.pkl",
            "*.faiss",
        ],
    },
    data_files=data_files_structure,
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "databricks_session=main:main",
        ],
    },
)
