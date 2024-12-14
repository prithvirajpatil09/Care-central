
def return_list(disease):
    disease_list = []
    match = disease.replace('^','_').split('_')
    ctr = 1
    for group in match:
        if ctr%2==0:
            disease_list.append(group)
        ctr = ctr + 1

    return disease_list

def searchdisease(*args):
    from sklearn import model_selection

    from sklearn.naive_bayes import MultinomialNB
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    import csv
    from collections import defaultdict
    import pandas as pd
    import numpy as np
    disease_list = []
    #reader = pd.read_csv("MDTouch/machinelearning/dataset_uncleaned.csv", encoding ="ISO-8859-1")
    with open("MDTouch/machinelearning/dataset_uncleaned.csv", 'r', encoding='mac_roman' ) as csvfile:
        reader = csv.reader(csvfile)
        disease=""
        print(reader)
        weight = 0
        disease_list = []
        dict_wt = {}
        dict_=defaultdict(list)
        for row in reader:
            if row[0]!="\xc2\xa0" and row[0]!="":
                disease = row[0]
                disease_list = return_list(disease)
                weight = row[1]

            if row[2]!="\xc2\xa0" and row[2]!="":
                symptom_list = return_list(row[2])

                for d in disease_list:
                    for s in symptom_list:
                        dict_[d].append(s)
                    dict_wt[d] = weight

    with open("MDTouch/machinelearning/dataset_clean.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        for key,values in dict_.items():
            for v in values:
                #key = str.encode(key)
                key = str.encode(key).decode('utf-8')
                #.strip()
                #v = v.encode('utf-8').strip()
                #v = str.encode(v)
                writer.writerow([key,v,dict_wt[key]])

    columns = ['Source','Target','Weight']
    data = pd.read_csv("MDTouch/machinelearning/dataset_clean.csv",names=columns, encoding ="ISO-8859-1")
    #print(data.head())
    data.to_csv("MDTouch/machinelearning/dataset_clean.csv",index=False)
    slist = []
    dlist = []

    with open("MDTouch/machinelearning/nodetable.csv","w") as csvfile:
        writer = csv.writer(csvfile)
        for key,values in dict_.items():
            for v in values:
                if v not in slist:
                    writer.writerow([v,v,"symptom"])
                    slist.append(v)
            if key not in dlist:
                writer.writerow([key,key,"disease"])
                dlist.append(key)
    nt_columns = ['Id','Label','Attribute']
    nt_data = pd.read_csv("MDTouch/machinelearning/nodetable.csv",names=nt_columns, encoding ="ISO-8859-1",)
    #print(nt_data['Id'].unique())
    nt_data.to_csv("MDTouch/machinelearning/nodetable.csv",index=False)
    data = pd.read_csv("MDTouch/machinelearning/dataset_clean.csv", encoding ="ISO-8859-1")

    df = pd.DataFrame(data)
    df_1 = pd.get_dummies(df.Target)
    #print(df_1.head())
    df_s = df['Source']
    df_pivoted = pd.concat([df_s,df_1], axis=1)
    df_pivoted.drop_duplicates(keep='first',inplace=True)
    #print(df_pivoted[:5])
    len(df_pivoted)
    cols = df_pivoted.columns
    cols = cols[1:]
    df_pivoted = df_pivoted.groupby('Source').sum()
    df_pivoted = df_pivoted.reset_index()
    #print(df_pivoted[:5])
    #print(len(df_pivoted))
    df_pivoted.to_csv("MDTouch/machinelearning/df_pivoted.csv")
    x = df_pivoted[cols]
    y = df_pivoted['Source']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    mnb = MultinomialNB()
    mnb = mnb.fit(x_train, y_train)
    mnb.score(x_test, y_test)
    mnb_tot = MultinomialNB()
    mnb_tot = mnb_tot.fit(x, y)
    mnb_tot.score(x, y)
    disease_pred = mnb_tot.predict(x)
    disease_real = y.values
    #for i in range(0, len(disease_real)):
    #    if disease_pred[i]!=disease_real[i]:
    #        print ('Pred: {0} Actual:{1}'.format(disease_pred[i], disease_real[i]))
    #print ("DecisionTree")
    dt = DecisionTreeClassifier()
    clf_dt=dt.fit(x,y)
    #print ("Acurracy: ", clf_dt.score(x,y))
    #export_graphviz(dt,out_file='DOT-files/tree.dot',feature_names=cols)
    data = pd.read_csv("MDTouch/machinelearning/Manual-Data/Training.csv")
    df = pd.DataFrame(data)
    #print(df.head())
    cols = df.columns
    cols = cols[:-1]
    x = df[cols]
    y = df['prognosis']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    mnb = MultinomialNB()
    mnb = mnb.fit(x_train, y_train)
    mnb.score(x_test, y_test)
    #print ("cross result========")
    scores = model_selection.cross_val_score(mnb, x_test, y_test, cv=3)
    #print (scores)
    #print (scores.mean())
    test_data = pd.read_csv("MDTouch/machinelearning/Manual-Data/Testing.csv")
    testx = test_data[cols]
    testy = test_data['prognosis']
    #print(mnb.score(testx, testy))
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
    #print ("DecisionTree")
    dt = DecisionTreeClassifier()
    clf_dt=dt.fit(x_train,y_train)
    #print ("Acurracy: ", clf_dt.score(x_test,y_test))
    #print(args)
    with open("MDTouch/machinelearning/Manual-Data/disease.csv","w") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(args[0])
        writer.writerow(args[1])

    #csvFile.close()
    x_test = pd.read_csv("MDTouch/machinelearning/Manual-Data/disease.csv", encoding = "ISO-8859-1")
    return clf_dt.predict(x_test[-1:])
    '''
    from sklearn import model_selection
    #print ("cross result========")
    scores = model_selection.cross_val_score(dt, x_test, y_test, cv=3)
    #print (scores)
    #print (scores.mean())
    #print ("Acurracy on the actual test data: ", clf_dt.score(testx,testy))
    #from sklearn import tree
    importances = dt.feature_importances_
    indices = np.argsort(importances)[::-1]
    #print("Feature ranking:")
    features = cols
    #for f in range(10):
    #    print("%d. feature %d - %s (%f)" % (f + 1, indices[f], features[indices[f]] ,importances[indices[f]]))
    #export_graphviz(dt,out_file='DOT-files/tree-top5.dot',feature_names=cols,max_depth = 5)
    feature_dict = {}
    for i,f in enumerate(features):
        feature_dict[f] = i
    #print(feature_dict[args])
    sample_x = [i/feature_dict[args] if i ==feature_dict[args] else i*0 for i in range(len(features))]
    sample_x = np.array(sample_x).reshape(1,len(sample_x))
    dt.predict(sample_x)
    res = dt.predict(sample_x)
    #print(res[0])
    dt.predict_proba(sample_x)
    #print(data['prognosis'].unique())
    return res
    '''







'''

import csv
from collections import defaultdict
import matplotlib.pyplot as plt
disease_list = []

def return_list(disease):
    disease_list = []
    match = disease.replace('^','_').split('_')
    ctr = 1
    for group in match:
        if ctr%2==0:
            disease_list.append(group)
        ctr = ctr + 1

    return disease_list

with open("dataset_uncleaned.csv") as csvfile:
    reader = csv.reader(csvfile)
    disease=""
    weight = 0
    disease_list = []
    dict_wt = {}
    dict_=defaultdict(list)
    for row in reader:

        if row[0]!="\xc2\xa0" and row[0]!="":
            disease = row[0]
            disease_list = return_list(disease)
            weight = row[1]

        if row[2]!="\xc2\xa0" and row[2]!="":
            symptom_list = return_list(row[2])

            for d in disease_list:
                for s in symptom_list:
                    dict_[d].append(s)
                dict_wt[d] = weight

with open("dataset_clean.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    for key,values in dict_.items():
        for v in values:
            #key = str.encode(key)
            key = str.encode(key).decode('utf-8')
            #.strip()
            #v = v.encode('utf-8').strip()
            #v = str.encode(v)
            writer.writerow([key,v,dict_wt[key]])
import pandas as pd
columns = ['Source','Target','Weight']
data = pd.read_csv("dataset_clean.csv",names=columns, encoding ="ISO-8859-1")
print(data.head())
data.to_csv("dataset_clean.csv",index=False)
slist = []
dlist = []
with open("Scraped-Data/nodetable.csv","w") as csvfile:
    writer = csv.writer(csvfile)

    for key,values in dict_.items():
        for v in values:
            if v not in slist:
                writer.writerow([v,v,"symptom"])
                slist.append(v)
        if key not in dlist:
            writer.writerow([key,key,"disease"])
            dlist.append(key)
nt_columns = ['Id','Label','Attribute']
nt_data = pd.read_csv("Scraped-Data/nodetable.csv",names=nt_columns, encoding ="ISO-8859-1",)
print(nt_data['Id'].unique())
nt_data.to_csv("Scraped-Data/nodetable.csv",index=False)
data = pd.read_csv("dataset_clean.csv", encoding ="ISO-8859-1")
print(data.head())
print(len(data['Source'].unique()))
print(len(data['Target'].unique()))

df = pd.DataFrame(data)
df_1 = pd.get_dummies(df.Target)
print(df_1.head())
df_s = df['Source']
df_pivoted = pd.concat([df_s,df_1], axis=1)
df_pivoted.drop_duplicates(keep='first',inplace=True)
print(df_pivoted[:5])
len(df_pivoted)
cols = df_pivoted.columns
cols = cols[1:]
df_pivoted = df_pivoted.groupby('Source').sum()
df_pivoted = df_pivoted.reset_index()
print(df_pivoted[:5])
print(len(df_pivoted))
df_pivoted.to_csv("Scraped-Data/df_pivoted.csv")
x = df_pivoted[cols]
y = df_pivoted['Source']

import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
#matplotlib inline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
mnb = MultinomialNB()
mnb = mnb.fit(x_train, y_train)
mnb.score(x_test, y_test)
mnb_tot = MultinomialNB()
mnb_tot = mnb_tot.fit(x, y)
mnb_tot.score(x, y)
disease_pred = mnb_tot.predict(x)
disease_real = y.values
for i in range(0, len(disease_real)):
    if disease_pred[i]!=disease_real[i]:
        print ('Pred: {0} Actual:{1}'.format(disease_pred[i], disease_real[i]))

from sklearn.tree import DecisionTreeClassifier, export_graphviz

print ("DecisionTree")
dt = DecisionTreeClassifier()
clf_dt=dt.fit(x,y)
print ("Acurracy: ", clf_dt.score(x,y))
from sklearn import tree
from sklearn.tree import export_graphviz
#export_graphviz(dt,out_file='DOT-files/tree.dot',feature_names=cols)
data = pd.read_csv("Manual-Data/Training.csv")
df = pd.DataFrame(data)
print(df.head())
cols = df.columns
cols = cols[:-1]
x = df[cols]
y = df['prognosis']

import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
mnb = MultinomialNB()
mnb = mnb.fit(x_train, y_train)
mnb.score(x_test, y_test)
from sklearn import model_selection
print ("cross result========")
scores = model_selection.cross_val_score(mnb, x_test, y_test, cv=3)
print (scores)
print (scores.mean())
test_data = pd.read_csv("Manual-Data/Testing.csv")
testx = test_data[cols]
testy = test_data['prognosis']
print(mnb.score(testx, testy))


from sklearn.tree import DecisionTreeClassifier, export_graphviz
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
print ("DecisionTree")
dt = DecisionTreeClassifier()
clf_dt=dt.fit(x_train,y_train)
print ("Acurracy: ", clf_dt.score(x_test,y_test))
from sklearn import model_selection
print ("cross result========")
scores = model_selection.cross_val_score(dt, x_test, y_test, cv=3)
print (scores)
print (scores.mean())
print ("Acurracy on the actual test data: ", clf_dt.score(testx,testy))
#from sklearn import tree
from sklearn.tree import export_graphviz

#export_graphviz(dt,out_file='DOT-files/tree.dot',feature_names=cols)
print(dt.__getstate__())
import numpy as np
import matplotlib.pyplot as plt

importances = dt.feature_importances_
indices = np.argsort(importances)[::-1]
print("Feature ranking:")
features = cols
for f in range(10):
    print("%d. feature %d - %s (%f)" % (f + 1, indices[f], features[indices[f]] ,importances[indices[f]]))
#export_graphviz(dt,out_file='DOT-files/tree-top5.dot',feature_names=cols,max_depth = 5)
feature_dict = {}
for i,f in enumerate(features):
    feature_dict[f] = i
print(feature_dict['internal_itching'])
sample_x = [i/93 if i ==93 else i*0 for i in range(len(features))]
sample_x = np.array(sample_x).reshape(1,len(sample_x))
dt.predict(sample_x)
res = dt.predict(sample_x)
print(res[0])
dt.predict_proba(sample_x)
print(data['prognosis'].unique())
'''
