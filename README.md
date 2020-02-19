# analyzePredict Package
The package is developed by EDSA students to display their competence in using github repo's and producing pip installable packages. The analyzePredict package contains only a single module (analyzeModule) with 7 functions.


## Description
The first function calculates the mean, median, variance, standard deviation, minimum and maximum of list of items.
The second function takes in a list of integers and returns a dictionary of the five number summary.
The third function is a date parser function that extracts the date from a given column and returns only the date in 'yyyy-mm-dd' format.
The fourth function takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information  about the municipality and hashtag of the tweet.
The fifth function calculates the number of tweets that were posted per day.
The sixth function splits the sentences in a dataframe's column into a list of the separate words.
The seventh function removes english stop words from a tweet.


## Table of contents
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)


## Installation
The module was designed for python3. Use [pip](https://pip.pypa.io/en/stable/) package manager to install analyzePredict Package. This package requires the importing of Numpy and Pandas. The follwing shell commands can be used to install package on local computer. (Internet access will be required)

```bash
pip install git+https://github.com/OmphileL/Team21.git
```

The following shell command is used to update to latest version of package
```bash
pip install --upgrade git+https://github.com/OmphileL/Team21.git
```


## Contributing
Changes only allowed by EDSA staff or invited contributors.

## Authors
Omphile Louw, Gavin Pillay, Suvarna Chetty, Nombulelo Msibi and Tuduetso Mmokwa


## License
[MIT](https://choosealicense.com/licenses/mit/)

## Function 3
This is a date parse function that extracts the date from a given column



