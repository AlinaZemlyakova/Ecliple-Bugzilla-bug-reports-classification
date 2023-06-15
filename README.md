# Ecliple-Bugzilla-bug-reports-classification
## Code and data provided for the masters's thesis 'NLP Application in Routing Customer Requests'.
The paper considers the problem of multiclass classification of customer requests in the field of software development. In order to study machine learning methods based on natural language processing to find the most efficient routing strategy, the most complete Eclipse development environment error dataset has been created to date, consisting of more than 580 thousand bugs. To find the most effective preprocessing and classification techniques, various methods of stemming, lemmatization, spelling correction, regular expression cleaning, imbalance reduction, hyperparameter tuning as well as 4 methods of vector representation of words were tested; after finding the optimal combination of preprocessing steps, a random forest classifier, a k-nearest neighbors algorithm (kNN), a support vector machine (SVM) and a naive Bayes claffifier were tested. This study has shown that the most accurate of the traditional models is the SVM. The obtained results emphasize the importance of choosing methods and approaches when working with text data and can be useful for researchers and practitioners in the field of text analysis and processing customer requests in the field of development.

## This repository contains the following files:
- bugzilla-load.py - web-parser for fetching basic information from Eclipse Bugzilla; to get up-to-date bug reports, run the code after changing end_bug_number to 600.000 or more
- eclipse_all_bugs.csv.zip - an ultimate dataset of all Eclipse bug reports till May 31, 2023
- preprocess_EDA.ipynb - basic preprocessing and EDA
- baseline_logreg.ipynb - building the most basic model
- cleaning_tuning.ipynb - all the experiments with data cleaning, text vectorization, other models
