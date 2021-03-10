import numpy as np

def sigmoid(a):
	return 1/(1+np.exp(-a))

def train(init,result,weight):


	rate=1

	v1=np.dot(init, weight['w1']) + weight['b1']

	v2=sigmoid(v1)
	v3=np.dot(v2,weight['w2'])+weight['b2']
	v4=sigmoid(v3)

	e=result-v4
	loss=np.sum((0.5*(np.power((v4-result),2))))
	t1=sigmoid(v3)*(1-sigmoid(v3))

	d1=e*t1

	changeW2=np.dot(v2.T, d1)
	changeB2=np.sum(e*d1)

	t2=np.dot(d1,weight['w2'].T)
	d2=sigmoid(v1)*(1-sigmoid(v1))
	changeW1=np.dot(init.T,d2*t2)
	changeB1=np.sum(d2*t2)




	weight['w1']+=rate*changeW1
	weight['b1']+=rate*changeB1
	weight['w2']+=rate*changeW2
	weight['b2']+=rate*changeB2

	print(loss)

	return {"w1": w1, "w2": w2, "b1": b1, "b2": b2}

w1 = [[0.1, 0, 0.3], [-0.2, 0.2, -0.4]]
w2 = [[-0.4, 0.2], [0.1, -0.1], [0.6, -0.2]]
b1 = [0.1, 0.2, 0.5]
b2 = [-0.1, 0.6]
w1=np.asarray(w1)
w2=np.asarray(w2)
b1=np.asarray(b1)
b2=np.asarray(b2)
weight = {"w1": w1, "w2": w2, "b1": b1, "b2": b2}
init=np.asarray([[0.6,0.1],[0.2,0.3]])
result=np.asarray([[1,0],[0, 1]])

for i in range(5000):
	train(init,result,weight)








