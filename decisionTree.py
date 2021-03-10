import csv
from math import log

def readData(path):
	with open(path,'r') as f:
		reader=csv.reader(f)
		data=[]
		for row in reader:
			data.append(row)
	return data




def calShanEnt(data):
	entries=len(data)
	labelCount={}
	for feature in data:
		currentLabel=feature[-1]
		if currentLabel not in labelCount.keys():
			labelCount[currentLabel]=0
		labelCount[currentLabel]+=1
	shanEnt=0.0
	for key in labelCount:
		prob=float(labelCount[key])/entries
		shanEnt-=prob*log(prob,2)
	#print(shanEnt)
	return shanEnt
'''
def calShanEnt(result):
	yCount=0
	for i in result:
		if i=='yes':
			yCount=yCount+1
	print(yCount)
	nCount=len(result)-yCount
	py=yCount/len(result)
	pn=nCount/len(result)
	shanEntropy=float(-py*log(py,2)-pn*log(pn,2))

	return shanEntropy
'''

def splitdata(data,axis,value):
	subdata=[]
	for i in data:
		if i[axis]==value:
			subFeature=i[:axis]
			subFeature.extend(i[axis+1:])
			subdata.append(subFeature)
	return subdata

def informationGain(data):
	featureNum = len(data[0]) - 1
	shanEnt = calShanEnt(data)
	bestIG=0.0
	bestFeature=-1


	for i in range(featureNum):
		features = [a[i] for a in data]
		pValue = set(features)
		newEnt = 0.0
		for value in pValue:
			subData = splitdata(data, i, value)
			p = len(subData) / float(len(data))
			newEnt += p * calShanEnt((subData))
		IG = shanEnt - newEnt
		print("informationGain for attrubute %d is %.3f" % (i, IG))

		if (IG > bestIG):
			bestIG = IG
			bestFeature = i
	return bestFeature

def appCount(attributes):
	aType={}
	for i in attributes:
		if i not in aType.keys():
			aType[i]=0
			aType[i]+=1
		sortA=sorted(aType.items(),key=operator.itemgetter(1),reverse=True)
		return sortA[0][0]


def createTree(data,labels,fLabels):
	aType=[a[-1] for a in data]
	if aType.count(aType[0])==len(aType):
		return aType[0]
	if len(data[0])==1:
		return appCount(aType)
	bFeature=informationGain(data)
	bLabel=labels[bFeature]
	fLabels.append(bLabel)
	tree={bLabel:{}}
	del(labels[bFeature])
	fValue=[a[bFeature] for a in data]
	pValue=set(fValue)
	for value in pValue:
		tree[bLabel][value]=createTree(splitdata(data,bFeature,value),labels,fLabels)
	return tree


data=readData('data.csv')
labels=['outlook','temperature','humidity','windy']
fLabels=[]
informationGain(data)
#tree=createTree(data,labels,fLabels)
#print(tree)

























