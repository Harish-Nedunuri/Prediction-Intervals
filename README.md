# prediction-intervals

[![PyPI](https://img.shields.io/pypi/v/prediction-intervals.svg)](https://pypi.org/project/prediction-intervals/)
[![Changelog](https://img.shields.io/github/v/release/Harish-Nedunuri/prediction-intervals?include_prereleases&label=changelog)](https://github.com/Harish-Nedunuri/prediction-intervals/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Harish-Nedunuri/prediction-intervals/blob/main/LICENSE)
[![Contact](https://www.linkedin.com/in/harish-nedunuri/)]


## Installation

Install this library using `pip`:

    pip install prediction-intervals

Pyspark and JAVA installation locally done on windows

https://www.youtube.com/watch?v=NFpW6JgNaQk

1. Install java 
2. Edit system Env variables JAVA_HOME,SPARK_HOME
3. PATH + =C:\Spark\spark-3.0.3-bin-hadoop2.7\bin
4. pip install findspark and pyspark (see setup.py file)

## Usage and Comments

1. A .vscode/launch.json is added to leverage teh vs code debugging feature.(This will not be a part of the final PyPi package)

2. A setup.py and requirements.txt file is included as a backup to setup.py file to recreate the virtual env (This will not be a part of the final PyPi package)

3. prediction_intervals the main python functions 

4. gitactions- automated testing on github CI and CD pipeline (tbc)

5. tests- a collection of unit and integration tests (dummy code included)

6. tests/data/- collection of energy consumption history (.csv) data files acquired from following source
https://www.drivendata.org/competitions/51/electricity-prediction-machine-learning/


## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd prediction-intervals
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
