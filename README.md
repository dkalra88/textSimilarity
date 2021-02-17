# textSimilarity

What are the requirements?
The focus was on having some fun and to use only the standard libraries for better understanding of the concepts.The document similarity algorithm does not need to perform well, and you doesn't need to account for all edge cases.
Examples of libraries that CANNOT be used:
-scikit-learn
-NLTK
-spaCy
-numpy

#########################
The code here takes two texts and compare them to give a similarity score.

The objective was to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

A number of decisions were made to come up with this solution:

-Do you count punctuation or only words?
-Which words should matter in the similarity comparison?
-Do you care about the ordering of words?
-What metric do you use to assign a numerical value to the similarity?
-What type of data structures should be used?

#############################
Running the code:
The code can be run in two ways:
1. python textSimilarity.py -text1 "Hello" -text2 "Hello there"

usage: textSimilarity.py [-h] -text1 TEXT1 -text2 TEXT2
optional arguments:
  -h, --help    show this help message and exit
  -text1 TEXT1  first text enclosed in double quotes
  -text2 TEXT2  second text enclosed in double quotes

2. python api.py
 * Serving Flask app "api" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://###.#.#.#:XXXX/ (Press CTRL+C to quit)
 
 please go to your browser and type http://localhost:XXXX where XXXX is what you will see when you run the api.
 
 The second way of running will require a flask library which is not part of start python package. 
 If using second method of running the code, I recommend installing anaconda and using the python binary from there.
