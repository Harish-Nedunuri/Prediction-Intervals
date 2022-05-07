# prediction-intervals

[![PyPI](https://img.shields.io/pypi/v/prediction-intervals.svg)](https://pypi.org/project/prediction-intervals/)
[![Changelog](https://img.shields.io/github/v/release/Harish-Nedunuri/prediction-intervals?include_prereleases&label=changelog)](https://github.com/Harish-Nedunuri/prediction-intervals/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Harish-Nedunuri/prediction-intervals/blob/main/LICENSE)



## Installation

Install this library using `pip`:

    pip install prediction-intervals

Pyspark and JAVA installation locally done on windows

https://www.youtube.com/watch?v=NFpW6JgNaQk

1. Install java in C->Java
2. Edit system Env variables JAVA_HOME,SPARK_HOME
3. PATH + =C:\Spark\spark-3.0.3-bin-hadoop2.7\bin


## Usage

Usage instructions go here.

## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd prediction-intervals
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
