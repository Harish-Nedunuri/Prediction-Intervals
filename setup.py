from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="prediction-intervals",
    description="",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Harish Nedunuri",
    url="https://github.com/Harish-Nedunuri/prediction-intervals",
    project_urls={
        "Issues": "https://github.com/Harish-Nedunuri/prediction-intervals/issues",
        "CI": "https://github.com/Harish-Nedunuri/prediction-intervals/actions",
        "Changelog": "https://github.com/Harish-Nedunuri/prediction-intervals/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["prediction_intervals"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
