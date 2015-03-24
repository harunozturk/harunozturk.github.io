#! /usr/bin/python

import math
import sys

MAX_CLUSTERS = 5
VEC_LEN = 7
INPUT_PATTERNS = 7
INPUT_TESTS = 6
DECAY_RATE = 0.96 # About 100 iterations.
MIN_ALPHA = 0.01
RADIUS_REDUCTION_POINT = 0.023 # Last 20% of iterations.

# Weight matrix with randomly chosen values between 0.0 and 1.0
w = [[0.2, 0.6, 0.5, 0.9, 0.4, 0.2, 0.8],
     [0.9, 0.3, 0.6, 0.4, 0.5, 0.6, 0.3],
     [0.8, 0.5, 0.7, 0.2, 0.6, 0.9, 0.5],
     [0.6, 0.4, 0.2, 0.3, 0.7, 0.2, 0.4],
     [0.8, 0.9, 0.7, 0.9, 0.3, 0.2, 0.5]]

pattern = [[1, 1, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 1, 1],
           [0, 0, 1, 1, 1, 0, 0],
           [0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [1, 0, 1, 0, 1, 0, 1]]

tests = [[1, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 1, 1],
         [0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 1]]

class SOM_Class2:
    def __init__(self, vectorLength, maxClusters, numPatterns, numTests, minimumAlpha, decayRate, reductionPoint, weightArray):
        self.mVectorLen = vectorLength
        self.mMaxClusters = maxClusters
        self.mNumPatterns = numPatterns
        self.mNumTests = numTests
        self.mMinAlpha = minimumAlpha
        self.mDecayRate = decayRate
        self.mReductionPoint = reductionPoint
        self.mAlpha = 0.6
        self.d = []
        self.w = weightArray
        return
    
    def compute_input(self, vectorArray, vectorNumber):
        self.d = [0.0] * self.mMaxClusters
    
        for i in range(self.mMaxClusters):
            for j in range(self.mVectorLen):
                self.d[i] += math.pow((self.w[i][j] - vectorArray[vectorNumber][j]), 2)
    
        return

    def get_minimum(self, nodeArray):
        minimum = 0
        foundNewMinimum = False
        done = False
    
        while not done:
            foundNewMinimum = False
            for i in range(self.mMaxClusters):
                if i != minimum:
                    if nodeArray[i] < nodeArray[minimum]:
                        minimum = i
                        foundNewMinimum = True
    
            if foundNewMinimum == False:
                done = True
    
        return minimum

    def update_weights(self, vectorNumber, dMin, patternArray):
        for i in range(self.mVectorLen):
            # Update the winner.
            self.w[dMin][i] = self.w[dMin][i] + (self.mAlpha * (patternArray[vectorNumber][i] - self.w[dMin][i]))
    
            # Only include neighbors before radius reduction point is reached.
            if self.mAlpha > self.mReductionPoint:
                if (dMin > 0) and (dMin < (self.mMaxClusters - 1)):
                    # Update neighbor to the left...
                    self.w[dMin - 1][i] = self.w[dMin - 1][i] + (self.mAlpha * (patternArray[vectorNumber][i] - self.w[dMin - 1][i]))
                    # and update neighbor to the right.
                    self.w[dMin + 1][i] = self.w[dMin + 1][i] + (self.mAlpha * (patternArray[vectorNumber][i] - self.w[dMin + 1][i]))
                else:
                    if dMin == 0:
                        # Update neighbor to the right.
                        self.w[dMin + 1][i] = self.w[dMin + 1][i] + (self.mAlpha * (patternArray[vectorNumber][i] - self.w[dMin + 1][i]))
                    else:
                        # Update neighbor to the left.
                        self.w[dMin - 1][i] = self.w[dMin - 1][i] + (self.mAlpha * (patternArray[vectorNumber][i] - self.w[dMin - 1][i]))
    
        return

    def training(self, patternArray):
        iterations = 0
        reductionFlag = False
        reductionPoint = 0
        
        while self.mAlpha > self.mMinAlpha:
            iterations += 1
            for i in range(self.mNumPatterns):
                self.compute_input(patternArray, i)
    
                dMin = self.get_minimum(self.d)
    
                self.update_weights(i, dMin, patternArray)
            
            # Reduce the learning rate.
            self.mAlpha = self.mDecayRate * self.mAlpha
    
            # Reduce radius at specified point.
            if self.mAlpha < self.mReductionPoint:
                if reductionFlag == False:
                    reductionFlag = True
                    reductionPoint = iterations
    
        sys.stdout.write("Iterations: " + str(iterations) + "\n")
    
        sys.stdout.write("Neighborhood radius reduced after " + str(reductionPoint) + " iterations.\n")
    
        return
    
    def print_results(self, patternArray, testArray):
        # Print clusters created.
        sys.stdout.write("Clusters for training input:\n")
        for i in range(self.mNumPatterns):
            self.compute_input(patternArray, i)
            
            dMin = self.get_minimum(self.d)
            
            sys.stdout.write("Vector (")
            for j in range(self.mVectorLen):
                sys.stdout.write(str(patternArray[i][j]) + ", ")
            
            sys.stdout.write(") fits into category " + str(dMin) + "\n")
        
        # Print weight matrix.
        sys.stdout.write("------------------------------------------------------------------------\n")
        for i in range(self.mMaxClusters):
            sys.stdout.write("Weights for Node " + str(i) + " connections:\n")
            sys.stdout.write("     ")
            for j in range(self.mVectorLen):
                sys.stdout.write("{:03.3f}".format(self.w[i][j]) + ", ")
            
            sys.stdout.write("\n")
        
        # Print post-training tests.
        sys.stdout.write("------------------------------------------------------------------------\n")
        sys.stdout.write("Categorized test input:\n")
        for i in range(self.mNumTests):
            self.compute_input(testArray, i)
            
            dMin = self.get_minimum(self.d)
            
            sys.stdout.write("Vector (")
            for j in range(self.mVectorLen):
                sys.stdout.write(str(testArray[i][j]) + ", ")
            
            sys.stdout.write(") fits into category " + str(dMin) + "\n")
        
        return

if __name__ == '__main__':
    som = SOM_Class2(VEC_LEN, MAX_CLUSTERS, INPUT_PATTERNS, INPUT_TESTS, MIN_ALPHA, DECAY_RATE, RADIUS_REDUCTION_POINT, w)
    som.training(pattern)
    som.print_results(pattern, tests)
    
