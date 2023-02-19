from setuptools import setup
import os
import json

VERSION = "0.0.5"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()

with open("package_setup.json", "r") as f:
    package_setup = json.load(f)
    package_name = package_setup["package_name"]
    package_version = package_setup["package_version"]
    package_description = package_setup["package_description"]
    package_tasks = package_setup["functions"]


setup(
    name="prediction-intervals",
    description="A package with statistical machine Learning methods for prediction interval estimation",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Harish Nedunuri",
    url="https://github.com/Harish-Nedunuri/prediction-intervals",
    entry_points={"console_scripts": [
            f"{package_name}.{task}={package_name}.{task}.entry:main"
            for task in package_tasks
        ]},
    project_urls={
        "Issues": "https://github.com/Harish-Nedunuri/prediction-intervals/issues",
        "CI": "https://github.com/Harish-Nedunuri/prediction-intervals/actions",
        "Changelog": "https://github.com/Harish-Nedunuri/prediction-intervals/releases",
    },
    
    version=VERSION,
    packages=["prediction_intervals"],
    install_requires=["findspark==2.0.1","pandas==1.4.1","pyspark==3.1.3","matplotlib==3.5.0","scikit-learn==1.0.2"],
    extras_require={"test": ["tox==3.24.4",
            "black==22.3.0",
            "flake8==4.0.1",
            "pytest==7.0.1",
            "pytest-cov==3.0.0"]
},
    python_requires=">=3.8",
)
