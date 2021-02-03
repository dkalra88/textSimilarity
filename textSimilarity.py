import string
import argparse
from collections import Counter
import itertools
import re
import time

class TextCompare(object):
    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2
        self.uniqueWordsCombinationsList = None
        self.vectorLength = None
        self.vec1 = None
        self.vec2 = None
        self.score = None
        
    def run(self):
        start = time.time()
        text1 = self.cleanupText(self.text1)
        text2 = self.cleanupText(self.text2)
        step1 = time.time()
        print("time taken for cleanup {}".format(round(step1 - start, 3)))
        self.uniqueWordsCombinationsList = self.getUniqueWordsCombination(text1, text2)
        self.vectorLength = len(self.uniqueWordsCombinationsList)
        step2 = time.time()
        print("time taken for getting unique words and combinations {}".format(round(step2 - step1, 3)))
        self.vec1 = self.getTextVector(text1)
        self.vec2 = self.getTextVector(text2)
        step3 = time.time()
        print("time taken for getting word vectors {}".format(round(step3 - step2, 3)))
        self.score = self.getComparisonScore(self.vec1, self.vec2)
        step4 = time.time()
        print("time taken for calculating score {}".format(round(step4 - step3, 3)))
        return self.score

    def cleanupText(self, text):
        text = text.lower()
        text = "".join([word for word in text if word not in string.punctuation]) 
        return text

    def getUniqueWordsCombination(self, text1, text2):
        combinedTextList = text1.split() + text2.split()
        combinedUniqueWordsList = []
        for word in combinedTextList:
            if word not in combinedUniqueWordsList:
                combinedUniqueWordsList.append(word)

        twoWordPairs = []
        for pair in itertools.combinations(combinedTextList,2):
            twoWordPairs.append(' '.join(pair))
        threeWordPairs = []
        for pair in itertools.combinations(combinedTextList,3):
            threeWordPairs.append(' '.join(pair))

        expandedUniqueWordList = combinedUniqueWordsList + twoWordPairs + threeWordPairs
        return(expandedUniqueWordList)

    def getTextVector(self, text):
        wordCountDict = {}
        for word in self.uniqueWordsCombinationsList:
            wordCountDict[word] = 0

        dictCount = self.getWordCounts(text, wordCountDict.copy())
        vec = [0]*self.vectorLength
        for k,v in dictCount.items():
            if v > 0:
                ind = self.uniqueWordsCombinationsList.index(k)
                vec[ind] = v
        return(vec)

    def getWordCounts(self, text, initializedDict):
        for key in initializedDict.keys():
            count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(key), text))
            initializedDict[key] = count
        return(initializedDict)

    def getComparisonScore(self, v1, v2):
        mag_v1 = self.getProduct(v1,v1) ** 0.5
        mag_v2 = self.getProduct(v2,v2) ** 0.5
        dot_prod = self.getProduct(v1, v2)
        return(dot_prod/(mag_v1*mag_v2))

    def getProduct(self, v1, v2):
        return(sum([i*j for (i, j) in zip(v1, v2)]))
        
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-text1",action="store",dest="text1",
                        help="first text enclosed in double quotes", required=True, type=str)
    parser.add_argument("-text2",action="store",dest="text2",
                        help="second text enclosed in double quotes", required=True, type=str)

    args = parser.parse_args()
    text1 = args.text1
    text2 = args.text2
    compObj = TextCompare(text1, text2)
    score = compObj.run()
    print("The score for comparison is {}".format(score))

if __name__ == '__main__':
    main()
