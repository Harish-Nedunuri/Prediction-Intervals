from setuptools import setup
import os

VERSION = "0.0.4"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="prediction-intervals",
    description="A package with statistical machine Learning methods for prediction interval estimation",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Harish Nedunuri",
    url="https://github.com/Harish-Nedunuri/prediction-intervals",
    entry_points={"console_scripts": ["prediciton_intervals=prediction_intervals.__init__:main",]},
    project_urls={
        "Issues": "https://github.com/Harish-Nedunuri/prediction-intervals/issues",
        "CI": "https://github.com/Harish-Nedunuri/prediction-intervals/actions",
        "Changelog": "https://github.com/Harish-Nedunuri/prediction-intervals/releases",
    },
    
    version=VERSION,
    packages=["prediction_intervals"],
    install_requires=["findspark==2.0.1","pandas==1.4.1","pyspark==3.0.0","matplotlib==3.5.0","scikit-learn==1.0.2"],
    extras_require={"test": ["tox==3.24.4",
            "black==22.3.0",
            "flake8==4.0.1",
            "pytest==7.0.1",
            "pytest-cov==3.0.0"]
},
    python_requires=">=3.8",
)
