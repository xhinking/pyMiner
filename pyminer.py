# pyMiner - simple python Data Mining lib
# Author:   Eric Wang
# Create at:2011.06.24

from math import sqrt

# Euclidean Distance - Similarity
def e_distance(point1, point2):
	return sqrt(pow(point1-point2,2))

