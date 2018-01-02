import pandas
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np

data =  pandas.read_excel(open('./data/results_new.xlsx','rb'), sheet_name=0);
result =  pandas.read_excel(open('./data/results_new.xlsx','rb'), sheet_name=1);

X = data.values
Y=result.values[:,0]

N = 200

vars=[9,7,1,6,2,4,5,3,10,0,8]
EN=np.zeros(11)

f = open('./data/Nvar_Models.txt','a');

for nvars in range (0,11): 
	print vars[0:nvars+1]
	XX = X[:,vars[0:nvars+1]]
	print nvars

	validation_size=0.2
	seed = 7
	X_t, X_v, Y_t, Y_v = model_selection.train_test_split(XX, Y, test_size=validation_size, random_state=seed)

	#clf =LinearDiscriminantAnalysis()
	#clf = LogisticRegression()
	#clf = SVC()
	#clf = KNeighborsClassifier()
	#clf = DecisionTreeClassifier()
	#clf = GaussianNB()
	clf = RandomForestClassifier()
	clf.fit(X_t,Y_t)
	Y_p = clf.predict(X_v)
	error= np.zeros(N)
	#print len(error)
	#print len(Y_v)
	#print len(Y_p)
	#print N
	for ii in range(0,N):
		error[ii] = (float(Y_v[ii]-Y_p[ii])/Y_v[ii])**2

	print np.sqrt(sum(error))/N
	print max(error)
	print np.std(error)

	EN[nvars]=np.sqrt(sum(error))/N

#plt.plot(X,Y)
for err in EN:
	f.write('%.4f ' % err)
f.write('\n')
#plt.plot(EN)
#plt.show()
f.close()

#CC = np.logspace(1,2.9,10)
#t = np.logspace(-7,-3,10)
#CC=np.int_(CC)

#cc=np.zeros(len(CC)*len(t))
#tt=np.zeros(len(CC)*len(t))
#et=np.zeros(len(CC)*len(t))
#index=0

#ET=np.zeros((len(CC),len(t)))
	
#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
#ax.set_aspect('equal')
#for i in range(len(CC)):
#	for j in range(len(t)):
#		clf = LinearDiscriminantAnalysis(n_components=CC[i],tol=t[j],solver='eigen')
#		clf.fit(X_t,Y_t)
#		Y_p = clf.predict(X_v)
#		error= np.zeros(N)
#		for ii in range(0,N):
#			error[ii] = (float(Y_v[ii]-Y_p[ii])/Y_v[ii])**2
#		ET[i]=np.sqrt(sum(error))/N
#		et[index]=np.sqrt(sum(error))/N
#		cc[index]=CC[i]
#		tt[index]=tt[j]
#		index=index+1
#plt.imshow(ET, interpolation='nearest', cmap=plt.cm.hot)
#plt.colorbar()
#plt.semilogx(CC,ET)
#plt.show()

#print ET
#id = np.argmin(ET)
#print et[id]
#print cc[id]
#print tt[id]