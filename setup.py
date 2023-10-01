from setuptools import find_packages, setup

REPO_URL = "https://github.com/mandarons/bounciepy"
VERSION = "0.3.0"

with open("README.md") as fh:
    long_description = fh.read()
with open("requirements.txt") as fh:
    required = fh.read().splitlines()

setup(
    name="bounciepy",
    version=VERSION,
    author="Mandar Patil",
    author_email="mandarons@pm.me",
    description="Python library to interact with bouncie.com API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_URL,
    package_dir={".": ""},
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=required,
)
