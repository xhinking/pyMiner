# pyMiner - simple python Data Mining lib
# Author:   Eric Wang
# Create at:2011.06.24

from math import sqrt

# Euclidean Distance - Similarity
def e_distance(point1, point2):
	return sqrt(pow(point1-point2,2))

# Pearson Correlation Coefficient - Similarity
def p_correlation(si,prefs1,prefs2):

	n=len(si)

	if n==0: return 0

	sum1=sum([prefs1[it] for it in si])
	sum2=sum([prefs2[it] for it in si])

	sum1Sq=sum([pow(prefs1[it],2) for it in si])
	sum2Sq=sum([pow(prefs2[it],2) for it in si])

	pSum=sum([prefs1[it]*prefs2[it] for it in si])
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0

	r=num/den

	return r
