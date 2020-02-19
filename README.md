analyzePredict Package¶
Packages relates to calculating metrics using Eskom data.

Table of contents
General info
Description
Installation
Technologies
Status
License
Authors
General info
The package is developed by EDSA students to display their competence in using Github repo's and producing pip installable packages. The analyzePredict package contains only a single module (analyzeModule) with 7 functions.

Description
The first function calculates the mean, median, variance, standard deviation, minimum and maximum of list of items.
The second function takes in a list of integers and returns a dictionary of the five number summary.
The third function is a date parser function that extracts the date from a given column and returns only the date in 'yyyy-mm-dd' format.
The fourth function takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.
The fifth function calculates the number of tweets that were posted per day.
The sixth function splits the sentences in a dataframe's column into a list of the separate words.
The seventh function removes english stop words from a tweet.
Installation
The module was designed for python3. Use pip package manager to install analyzePredict Package. The follwing shell commands can be used to install package on local computer. (Internet access will be required) The following shell command is used to update to latest version of package

pip install --upgrade git+https://github.com/OmphileL/Team21.git
Technologies
Python 3.7
Numpy
Pandas
Status
Package is: completed and will be updated with new metrics every second quarter.

License
MIT

Authors
Suvarna Chetty
Nombulelo Msibi
Tuduetso Mmokwa
Omphile Louw
Gavin Pillay

