import pandas
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import numpy as np

data =  pandas.read_excel(open('./data/results.xlsx','rb'), sheet_name=0);
result =  pandas.read_excel(open('./data/results.xlsx','rb'), sheet_name=1);

X = data.values
Y=result.values[:,0]

validation_size=0.2
seed = 7
X_t, X_v, Y_t, Y_v = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

N = len(Y_v)

CC = np.logspace(0,3,10)
#t = np.logspace(-7,-3,10)
CC=np.int_(CC)

cc=np.zeros(len(CC))
et=np.zeros(len(CC))
index=0

ET=np.zeros(len(CC))
	
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for i in range(len(CC)):
	clf = RandomForestClassifier(n_estimators=CC[i],max_features='log2')
	clf.fit(X_t,Y_t)
	Y_p = clf.predict(X_v)
	error= np.zeros(N)
	for ii in range(0,N):
		error[ii] = (float(Y_v[ii]-Y_p[ii])/Y_v[ii])**2
	ET[i]=np.sqrt(sum(error))/N
	et[index]=np.sqrt(sum(error))/N
	cc[index]=CC[i]
	index=index+1
	print i
#plt.imshow(ET, interpolation='nearest', cmap=plt.cm.hot)
#plt.colorbar()
plt.plot(CC,ET)
plt.show()

print ET
id = np.argmin(ET)
print et[id]
print cc[id]

clf = RandomForestClassifier(n_estimators=CC[id],max_features='log2')
clf.fit(X_t,Y_t)
Y_p = clf.predict(X_v)
error= np.zeros(N)
for ii in range(0,N):
	error[ii] = (float(Y_v[ii]-Y_p[ii])/Y_v[ii])**2

print np.sqrt(sum(error))/N
print max(error)
print np.std(error)