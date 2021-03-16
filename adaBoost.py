from libsvm.commonutil import *
from libsvm.svmutil import *
from libsvm.svm import *
from sklearn.model_selection import KFold
import numpy as np
import math

def adaBoost(K,instance,train_label,test_label):
	num=len(instance)
	train_label=np.array(train_label)
	test_label=np.array(test_label)
	w=[1/num]*num
	arr=[]
	for i in range(K):
		tmp=train_label-test_lable
		delta=[]
		for j in range(len(tmp)):
			delta.append(int(bool(tmp[j])))
		error=np.dot(w,delta)
		alpha=0.5*(math.log((1-error)/error))
		arr.append(alpha)

		changedW=(w*(math.exp(alpha)))/sum


train_path = 'C:/Users/sxtyg/Desktop/DogsVsCats/DogsVsCats/DogsVsCats.train'
test_path = 'C:/Users/sxtyg/Desktop/DogsVsCats/DogsVsCats/DogsVsCats.test'
y,x=svm_read_problem(train_path)
m,n=svm_read_problem(test_path)

linear=svm_train(y,x,'-t 0')
p_label,p_acc,p_val=svm_predict(y1,x1,linear)

adaBoost(10,x1,y1,linear)
adaBoost(20,x1,y1,linear)