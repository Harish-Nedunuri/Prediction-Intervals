# prediction-intervals

[![PyPI](https://img.shields.io/pypi/v/prediction-intervals.svg)](https://pypi.org/project/prediction-intervals/)
[![Changelog](https://img.shields.io/github/v/release/Harish-Nedunuri/prediction-intervals?include_prereleases&label=changelog)](https://github.com/Harish-Nedunuri/prediction-intervals/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Harish-Nedunuri/prediction-intervals/blob/main/LICENSE)

## Contact details
[![Contact](https://user-images.githubusercontent.com/97321212/167557927-8770a357-adde-41d3-a0ee-5b59c34b157e.png)](https://www.linkedin.com/in/harish-nedunuri/)


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

1. A .vscode/launch.json - to leverage the VS code debugging feature.(This will not be a part of the final PyPi package)

2. A setup.py and requirements.txt files - to recreate the virtual env (This will not be a part of the final PyPi package)

3. prediction_intervals- the main python functions 

4. gitactions- automated testing on github CI and CD pipeline (tbc)

5. tests- a collection of unit and integration tests (dummy code included)

6. tests/data/- collection of energy consumption history (.csv) data. Acquired and cleaned from following source
https://www.drivendata.org/competitions/51/electricity-prediction-machine-learning/


## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    #windows
    cd prediction-intervals
    py -m venv .venv
    .venv\Scripts\activate
    
    #bash
    cd prediction-intervals
    python -m venv .venv
    source .venv/Scripts/activate
    

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
