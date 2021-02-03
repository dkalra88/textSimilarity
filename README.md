# textSimilarity

#####Running the code

The code here takes two texts and compare them to give a similarity score

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
