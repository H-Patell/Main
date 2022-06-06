#!/usr/bin/env python
# coding: utf-8
# ###  Q1. Create a function named Graph_v1 that takes a dataset as input and exports boxplots and histograms (in the form of PNG files) for all the numerical columns in the data and bar plots for all the categorical columns of the data.

# In[ ]:


def Graph_v1(data):
    
    import matplotlib.pyplot as plt
    import seaborn as sns     
    
    #separating categorical and  numerical variables
    categorical = list(data.select_dtypes(include =  ['object']))
    numerical = list(data.select_dtypes(include = ['number']))
    print('categorical:', categorical)
    print('numerical:',numerical)
    
    #for all columns in dataset, create respective graphs
    for i in data.columns:
        
        if i in categorical:
            #creates bar charts for str type vars ----------------------------------
            fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi=500)
            data[i].value_counts().plot(kind='bar',color="#006699",width=0.5,  fontsize=9,rot=10 , grid=True)
            plt.title("Bar chart", fontsize = 9)
            plt.xlabel(i, fontsize = 9)
            plt.ylabel("Frequency", fontsize = 9)
            #saves graph with name of var
            plt.savefig('Barcategorical%03s.png'%(i),orientation='portrait',transparent=False)
            plt.show()
                      
        elif i in numerical:
             # creates boxplot and histogram for int/float type vars---------------------
            figure  = plt.figure(figsize=[10,6], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                             constrained_layout = True, dpi=500)
            plt.subplot(412, projection=None, polar=False, facecolor='#b3e6ec')      #Add an Axes to the current figure or retrieve an existing Axes.
                                                                                     #(nrows, ncols, index)
            data.boxplot(i, notch=False, vert=False, grid =True, patch_artist = True, whis=2.0, showfliers=True, showmeans=True,
                         capprops = dict(color = 'black'), boxprops=dict(facecolor='#006699', color='black'),
                         whiskerprops = dict(color = 'black'), flierprops = dict(color ='black'), 
                         medianprops = dict(color='black'),
                         meanprops = dict(color='black'))
            plt.xlabel(i, fontsize= 9)    
            plt.title("Boxplot of " + i, fontsize= 9)
            plt.savefig('Boxplotcont%03s.png'%(i), dpi=300)
            plt.show()
            # histogram--------------------
            plt.hist(data[[i]], bins=None, density=True, cumulative= False, histtype='bar', align='mid', orientation='vertical', 
                     rwidth=None, log=False,  color="#191970", stacked=False,  edgecolor="black")
            plt.xlabel(i, fontsize= 9)    
            plt.title("Histogram of " + i, fontsize= 9)
             #saves graph with name of var
            plt.savefig('Histcont%03s.png'%(i), dpi=300)
            plt.show()
        else:
            i=len(data.columns)
            break
           


# In[ ]:


import pandas as pd
data=pd.read_csv("/Users/aanchalkhanna72/Desktop/Praxis/IML/attrition.csv")
data.head()


# In[ ]:


Graph_v1(data)


# ### Q2. Create a function named Graph_v2 that takes a dataset as input and exports bar plots for all the categorical columns of the data and for the numeric columns it checks if the if the variable is discrete (or contains a lesser number of unique values) or continuous and plot the graph accordingly. For discrete numeric variables, it plots bar plot and for continuous it plots histogram & boxplot.

# In[ ]:


def Graph_v2(dataset):
    import matplotlib.pyplot as plt
    import seaborn as sns 
    import numpy as np
    
    #separating categorical and  numerical variables
    categorical = list(data.select_dtypes(include =  ['object']))
    numerical = list(data.select_dtypes(include = ['number']))
    print('categorical:', categorical)
    print('numerical:',numerical)
    
    #for all columns in dataset, create respective graphs
    for i in data.columns:
        
        if i in categorical:
            # creates bar charts for str type vars----------------------------------
            fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi=500)
            data[i].value_counts().plot(kind='bar',color="#006699",width=0.5,  fontsize=9,rot=10 , grid=True)
            plt.title("Bar chart", fontsize = 9)
            plt.xlabel(i, fontsize = 9)
            plt.ylabel("Frequency", fontsize = 9)
            plt.savefig('Barcategorical%03s.png'%(i),orientation='portrait',transparent=False)
            #plt.savefig(fname, dpi=None, facecolor='w', edgecolor='w', orientation='portrait', papertype=None, format=None, 
            #             transparent=False, bbox_inches=None, pad_inches=0.1, frameon=None, metadata=None)
            plt.show()
                      
        elif i in numerical:
            #create list of discrete and continuous vars
            discrete = []
            continuous = [] 
            
            #establishing conditions for discrete (with few unique values, assuming int type) and continuous variables:
            if (data[i].dtype == np.int64) and (len(set(data[i])) < 10):       
                    discrete.append(i)
        
            #continuous are assumed to be float type or (int type with multiple unique values):
            elif (data[i].dtype == np.float64) or ((data[i].dtype == np.int64 and len(set(data[i]))) > 10):
                    continuous.append(i)
            
            #bifurcates graphs according to categorization
            if i in discrete:
            #bar----------------------------------
                fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                     constrained_layout = True, dpi=500)
                data[i].value_counts().plot(kind='bar',color="#006699",width=0.5,  fontsize=9,rot=10 , grid=True)
                plt.title("Bar chart", fontsize = 9)
                plt.xlabel(i, fontsize = 9)
                plt.ylabel("Frequency", fontsize = 9)
                plt.savefig('Bardiscrete%03s.png'%(i),orientation='portrait',transparent=False)
                plt.show()
  
            elif i in continuous:
                # boxplot---------------------
                figure  = plt.figure(figsize=[10,6], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi=500)
                plt.subplot(412, projection=None, polar=False, facecolor='#b3e6ec')      #Add an Axes to the current figure or retrieve an existing Axes.
                                                                                         #(nrows, ncols, index)
                data.boxplot(i, notch=False, vert=False, grid =True, patch_artist = True, whis=2.0, showfliers=True, showmeans=True,
                             capprops = dict(color = 'black'), boxprops=dict(facecolor='#006699', color='black'),
                             whiskerprops = dict(color = 'black'), flierprops = dict(color ='black'), 
                             medianprops = dict(color='black'),
                             meanprops = dict(color='black'))
                plt.xlabel(i, fontsize= 9)    
                plt.title("Boxplot of " + i, fontsize= 9)

                plt.savefig('Boxplotcont%03s.jpeg'%(i), dpi=300)
                plt.show()
                
                # histogram--------------------
                plt.hist(data[[i]], bins=None, density=True, cumulative= False, histtype='bar', align='mid', orientation='vertical', 
                         rwidth=None, log=False,  color="#191970", stacked=False,  edgecolor="black")
                plt.xlabel(i, fontsize= 9)    
                plt.title("Histogram of " + i, fontsize= 9)
                plt.savefig('Histcont%03s.png'%(i), dpi=300)
                plt.show()
        else:
            i=len(data.columns)
            break


# In[ ]:


Graph_v2(data)


# ### Q3. Create a function named Graph_v3 that functions similar to Graph_v2 but takes 2 arguments – data, columns. Using the argument columns one can provide a list of interested columns. The graphs are plotted only of the columns provided. If nothing is mentioned then the graphs are plotted for all the columns.

# In[ ]:


def Graph_v3(dataset, columns='All'):
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    #creating  empty lists to store variable names
    cols = []
    categorical = list(data.select_dtypes(include = ['object']))
    numerical = list(data.select_dtypes(include = ['number']))
    
    #stating possible inputs for argument "columns" (has to be input by user in the  form of a list)
    if columns == "All":
        cols = list(data[data.columns[0:]]) #cols becomes all columns
    else:
        cols = columns #cols becomes only the specified columns in the argument
    print(cols)
    
    #create list of discrete and continuous vars
    discrete = []
    continuous = [] 
    
    #separating vars to discrete and continuous        
    for i in numerical:
        if (data[i].dtype == np.int64) and (len(set(data[i])) < 10): #(int type+unique values<10) accepted only 
                discrete.append(i)
        elif (data[i].dtype == np.float64) or ((data[i].dtype == np.int64 and len(set(data[i]))) > 10):#(int type+unique values>10) and float type  accepted 
                continuous.append(i)
    
    #creating graphs only for those vars specified in columns  
    for i in cols:
        
        if i in categorical:
            #bar chart-------------------------
            fig = plt.figure(figsize=[10,5], facecolor ='#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi = 200)
            data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize=9, rot=10, grid=True)
            plt.title("Bar chart", fontsize = 9)
            plt.xlabel(i, fontsize = 9)
            plt.ylabel("Frequency", fontsize = 9)
            plt.savefig('barcategorical%03s.png'%(i))
            plt.show()

                      
        elif i in numerical:
            
            if i in discrete:
                #bar chart---------------------------------
                fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi = 200)
                data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize= 9, rot=10, grid=True)
                plt.title("Bar chart", fontsize = 9)
                plt.xlabel(i, fontsize = 9)
                plt.ylabel("Frequency", fontsize = 9)
                plt.savefig('bardiscrete%03s.png'%(i))
                plt.show()
            
            if i in continuous:
                #boxplot-----------------------------
                figure  = plt.figure(figsize=[10,6], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi = 200)
                plt.subplot(412, projection=None, polar=False, facecolor='#b3e6ec' )      
                data.boxplot(i, notch=False, vert=False, grid =True, patch_artist = True, whis=2.0, showfliers=True, showmeans=True,
                             capprops = dict(color = 'black'), boxprops=dict(facecolor='#006699', color='black'),
                             whiskerprops = dict(color = 'black'), flierprops = dict(color ='black'), 
                             medianprops = dict(color='black'),
                             meanprops = dict(color='black'))
                plt.xlabel(i, fontsize= 9)    
                plt.title("Boxplot of " + i, fontsize= 9)
                plt.savefig('boxplotcont%03s.png'%(i))
                plt.show()
               #histogram-----------------------------------
                plt.hist(data[[i]], bins=None, density=True, cumulative= False, histtype='bar', align='mid', orientation='vertical', 
                         rwidth=None, log=False,  color="#191970", stacked=False,  edgecolor="black")
                plt.xlabel(i, fontsize= 9)    
                plt.title("Histogram of " + i, fontsize= 9)
                
                plt.savefig('histcont%03s.png'%(i))
                plt.show()
        else:
            i=len(data.columns)
            break          


# In[ ]:


Graph_v3(data, columns=["Age","OverTime"])


# ### Q4.Create a function named Graph_v4 that gives the same output as Graph_v3 but takes 3 arguments – data, columns, dir. “dir” is used to specify a folder where the graphs should be exported. If kept blank then the graph gets exported in the working directory.

# In[ ]:


def Graph_v4(data, columns='All', directory=''):
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import os #to get/change directory
    
    #creating  empty lists to store variable names
    cols = []
    discrete = []
    continuous = []
    categorical = list(data.select_dtypes(include = ['object']))
    numerical = list(data.select_dtypes(include = ['number']))
    
    #stating possible inputs for argument "directory"
    if directory == '':
        cwd = os.getcwd() #get working directory specified in the "directory"  argument
    else:
        cwd = directory #default working directory when nothing specified in the "directory"  argument
    
    #stating possible inputs for argument "columns"
    if columns == "All":
        cols = list(data[data.columns[0:]])
    else:
        cols = columns
    
    #separating vars to discrete and continuous
    for i in numerical:
        if (data[i].dtype == np.int64) and (len(set(data[i])) < 10):         
                discrete.append(i)
        elif (data[i].dtype == np.float64) or ((data[i].dtype == np.int64 and len(set(data[i]))) > 10):
                continuous.append(i)
    
    #creating graphs only for those vars specified in columns             
    for i in cols:
        
        if i in categorical:
            fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi = 200)
            data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize= 9, rot=10, grid=True)
            plt.title("Bar chart", fontsize = 9)
            plt.xlabel(i, fontsize = 9)
            plt.ylabel("Frequency", fontsize = 9)
            #saving in the specified directory
            plt.savefig(cwd + 'barcategorical%03s.png'%(i), dpi=200,bbox_inches ="tight",pad_inches = 1,transparent = True,facecolor ="white",edgecolor ='black',orientation ='landscape')
            plt.show()
                               
        elif i in numerical:
            
            if i in discrete:
                fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi = 200)
                data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize=9, rot=10, grid=True)
                plt.title("Bar chart", fontsize = 9)
                plt.xlabel(i, fontsize = 9)
                plt.ylabel("Frequency", fontsize = 9)
                
                plt.savefig(cwd + 'bardiscrete%03s.png'%(i))
                plt.show()
            
            if i in continuous:
                figure  = plt.figure(figsize=[10,6], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                 constrained_layout = True, dpi = 200)
                plt.subplot(412, projection=None, polar=False, facecolor='#b3e6ec' )      
                                                                                       
                # boxplot
                data.boxplot(i, notch=False, vert=False, grid =True, patch_artist = True, whis=2.0, showfliers=True, showmeans=True,
                             capprops = dict(color = 'black'), boxprops=dict(facecolor='#006699', color='black'),
                             whiskerprops = dict(color = 'black'), flierprops = dict(color ='black'), 
                             medianprops = dict(color='black'),
                             meanprops = dict(color='black'))
                plt.xlabel(i, fontsize= 9)    
                plt.title("Boxplot of " + i, fontsize= 9)
                
                plt.savefig(cwd + 'boxplotcont%03s.png'%(i))
                plt.show()
                
                # histogram
                plt.hist(data[[i]], bins=None, density=True, cumulative= False, histtype='bar', align='mid', orientation='vertical', 
                         rwidth=None, log=False,  color="#191970", stacked=False,  edgecolor="black")
                plt.xlabel(i, fontsize= 9)    
                plt.title("Histogram of " + i, fontsize= 9)
                 
                plt.savefig(cwd + 'histcont%03s.png'%(i))
                plt.show()
        else:
            i=len(data.columns)
            break  


# In[ ]:


Graph_v4(data,columns=["Age","MaritalStatus"],directory="/Users/aanchalkhanna72/Desktop/PythonHWTrial/Trial")


# ### Q5. Suggestion: Creating a function  called "plotgrid" that combines all the visuals of the  dataset in one PNG  file that can be exported.

# In[ ]:


#Goal: Our goal was to create one single grid (similar to pairplot grid) of all variables graphed correctly. Instead
# of exporting graphs one by one and creating multiple images that our user can find difficult to go through, our function would use subplots to put all boxplots, histograms, bar charts in one grid,
#which woould then be exported to the desired directory. We were unable to give column argument here because our
#grid  would not accept a small number of column names to be graphed and plotted together in a grid. 

#Please zoom in on the downloaded PNG file to see the image  in detail.

def plotgrid(data, directory=''):

    import seaborn as sns
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    
    #creating  empty lists to store variable names
    discrete = []
    continuous = []
    categorical = list(data.select_dtypes(include = ['object'])) #contains all categorical vars
    numerical = list(data.select_dtypes(include = ['number']))

    #stating possible inputs for argument "directory"
    if directory == '':
        cwd = os.getcwd()
    else:
        cwd = directory
    
    #separating vars to discrete, continuous     
    for i in numerical:
        if (data[i].dtype == np.int64) and (len(set(data[i])) < 10):      
                discrete.append(i)
        elif (data[i].dtype == np.float64) or (len(set(data[i])) > 10):
                continuous.append(i)
        else:
            pass 
    
    #specifies size, spacing of each figure in grid
    fig = plt.figure(figsize=(15,150))
    a=len(data.columns) #number of rows
    b=2 # number of columns
    c=1 # initialize plot counter

    for i in discrete:
        #creates  barcharts for discrete vars
        plt.subplot(a, b, c)
        plt.title('{} (bar), subplot: {},{},{}'.format(i, a, b, c))
        data[i].value_counts().plot(kind='bar',color="pink",width=0.5,  fontsize=9,rot=10, grid=False)
        plt.title("Bar chart", fontsize = 9)
        plt.xlabel(i, fontsize = 9)
        plt.ylabel("Frequency", fontsize = 9)
        c = c + 1

    for i in continuous:
        #creates  boxplots and histplots for continuous vars
        plt.subplot(a, b, c)
        plt.title('{} (hist), subplot: {},{},{}'.format(i, a, b, c))
        plt.xlabel(i)
        sns.histplot(data[i])
        c = c + 1

        plt.subplot(a, b, c)
        plt.title('{} (box), subplot: {},{},{}'.format(i, a, b, c))
        plt.xlabel(i)
        plt.boxplot(x = data[i], vert=False)
        c = c + 1

    for i in categorical:
        #creates  barcharts for categorical vars
        plt.subplot(a, b, c)
        plt.title('{} (bar), subplot: {},{},{}'.format(i, a, b, c))
        data[i].value_counts().plot(kind='bar',color="turquoise",width=0.5, fontsize=9,rot=10 , grid=False)
        plt.title("Bar chart", fontsize = 9)
        plt.xlabel(i, fontsize = 9)
        plt.ylabel("Frequency", fontsize = 9)
        c = c + 1

    plt.savefig(cwd+'Plotgrid.png') #saves graph in give directory
    plt.show()


# In[ ]:


plotgrid(data, directory="/Users/aanchalkhanna72/Desktop/PythonHWTrial/Trial")


# ### Suggestion 6: User input to determine accuracy of variables graphed and to rectify errors based on feedback given by user.
# 

# In[ ]:


import pandas as pd
data=pd.read_csv("/Users/aanchalkhanna72/Desktop/Praxis/IML/attrition.csv")


# In[ ]:


#Goal: Since our previous codes are not entirely generalized to all  datasets, there is a chance that a variable
#will be wrongly categorized into discrete,continuous,categorical. To prevent this from happening, we allow our user to
#change  categories before plotting graphs. Our process involves removal and appending of lists with variable names. Once all
#lists contain  accurate var names, graphs are plotted using the above codes. We wanted to  shorten our  code
#by calling a previously defined function within  this function, but we were unable to do so. We  believe that
#this code  can be made even better with time by including Try-Except, shortening of code, etc. 

def Graph_v5(data):
    import pandas as pd
    import numpy as np
    import  matplotlib.pyplot as plt

    #initial summary of data types, data categories are given for the user to scan through
    desc=data.dtypes  #gives whether data is  int/float/str
    discrete = []
    continuous = []
    #initial basic categorization
    categorical = list(data.select_dtypes(include = ['object']))
    numerical = list(data.select_dtypes(include = ['number']))

    #better categorization (but best option that can be handled by our code)
    for i in numerical:
        if (data[i].dtype == np.int64) and (len(set(data[i])) < 10):        
            discrete.append(i)
        elif (data[i].dtype == np.float64) or (data[i].dtype == np.int64 and len(set(data[i])) > 10):
            continuous.append(i)
            
    #gives the best possible categorizations of data types, categories
    print('Categorical:',categorical, "\n")
    print('Discrete:', discrete, "\n")
    print('Continuous:', continuous, "\n")
    print('Description:', desc, "\n") 
    
    #user input to improve categorizations
    q1 = input("Are the variables categorized correctly? yes/no: ")
    if q1.lower()=="yes":
        #if yes, all graphs will be printed
        for i in data.columns:
        
            if i in categorical:
                fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                     constrained_layout = True, dpi = 200)
                data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize= 9, rot=10, grid=True)
                plt.title("Bar chart", fontsize = 9)
                plt.xlabel(i, fontsize = 9)
                plt.ylabel("Frequency", fontsize = 9)

                #plt.savefig('categorical%03s.png'%(i))
                #os.getcwd()
                #os.path.abspath() 
                plt.savefig('barcategorical%03s.png'%(i), dpi=200,bbox_inches ="tight",pad_inches = 1,transparent = True,facecolor ="white",edgecolor ='black',orientation ='landscape')
                plt.show(

            elif i in numerical:

                if i in discrete:
                    fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                     constrained_layout = True, dpi = 200)
                    data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize=9, rot=10, grid=True)
                    plt.title("Bar chart", fontsize = 9)
                    plt.xlabel(i, fontsize = 9)
                    plt.ylabel("Frequency", fontsize = 9)

                    plt.savefig('bardiscrete%03s.png'%(i))
                    plt.show()

                if i in continuous:
                    figure  = plt.figure(figsize=[10,6], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                                     constrained_layout = True, dpi = 200)
                    plt.subplot(412, projection=None, polar=False, facecolor='#b3e6ec' )      

                    # boxplot
                    data.boxplot(i, notch=False, vert=False, grid =True, patch_artist = True, whis=2.0, showfliers=True, showmeans=True,
                                 capprops = dict(color = 'black'), boxprops=dict(facecolor='#006699', color='black'),
                                 whiskerprops = dict(color = 'black'), flierprops = dict(color ='black'), 
                                 medianprops = dict(color='black'),
                                 meanprops = dict(color='black'))
                    plt.xlabel(i, fontsize= 9)    
                    plt.title("Boxplot of " + i, fontsize= 9)

                    plt.savefig('boxplotcont%03s.png'%(i))
                    plt.show()

                    # histogram
                    plt.hist(data[[i]], bins=None, density=True, cumulative= False, histtype='bar', align='mid', orientation='vertical', 
                             rwidth=None, log=False,  color="#191970", stacked=False,  edgecolor="black")
                    plt.xlabel(i, fontsize= 9)    
                    plt.title("Histogram of " + i, fontsize= 9)

                    plt.savefig('histcont%03s.png'%(i))
                    plt.show()
            #import os
            #os.chdir("/Users/aanchalkhanna72/Downloads/")
            #import graph.py as g 
            #g.Graph_v2(data)

    elif q1.lower()=="no":
        while True:
            q2=input("Which variable is not categorized correctly?: ")
                
            if q2 in categorical:
                categorical.remove(q2)
                q3=input("Is this variable discrete/continuous (disc/cont):")
                if (q3 == "discrete") or (q3 == "disc"):
                    discrete.append(q2)
                    print("The discrete numerical variables now are: ", discrete)
                if (q3 == "continuous") or (q3 =="cont"):
                    continuous.append(q2)
                    print("The continuous numerical variables now are: ", continuous)

            elif q2 in discrete:
                discrete.remove(q2)
                q4=input("Is this variable categorical/continuous (cat/cont):")
                if (q4.lower() == "cat") or (q4.lower() == "categorical"):
                    categorical.append(q2)
                    print("The categorical variables now are: ", categorical)
                if (q4.lower() == "continuous") or (q4.lower() == "cont"):
                    continuous.append(q2)
                    print("The continuous numerical variables now are: ", continuous)

            else:
                continuous.remove(q2)
                q5=input("Is this variable discrete/categorical (disc/cat):")
                if (q5.lower() == "discrete") or (q5.lower() =="disc"):
                    discrete.append(q2)
                    print("The discrete numerical variables now are: ", discrete)
                if (q5.lower() == "cat") or (q5.lower() == "categorical"):
                    categorical.append(q2)
                    print("The categorical variables are: ", categorical)
        
            q6 = input("Are the variables categorized correctly? yes/no: ")
            if q6.lower()=="yes":
                break 

    print("\n---------------------", "\nCategorical:",categorical,"\nContinuous:",continuous, "\nDiscrete:",discrete)
    #Printing graphs after all the categories are rectified
    for i in categorical:
        fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                             constrained_layout = True, dpi = 200)
        data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize= 9, rot=10, grid=True)
        plt.title("Bar chart", fontsize = 9)
        plt.xlabel(i, fontsize = 9)
        plt.ylabel("Frequency", fontsize = 9)

        #plt.savefig('categorical%03s.png'%(i))
        #os.getcwd()
        #os.path.abspath() 
        plt.savefig('barcategorical%03s.png'%(i), dpi=200,bbox_inches ="tight",pad_inches = 1,transparent = True,facecolor ="white",edgecolor ='black',orientation ='landscape')
        plt.show()


    for i in discrete:
        fig = plt.figure(figsize=[10,5], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                         constrained_layout = True, dpi = 200)
        data[i].value_counts().plot(kind='bar',color="#006699", width=0.5, fontsize=9, rot=10, grid=True)
        plt.title("Bar chart", fontsize = 9)
        plt.xlabel(i, fontsize = 9)
        plt.ylabel("Frequency", fontsize = 9)

        plt.savefig('bardiscrete%03s.png'%(i))
        plt.show()

    for i in continuous:
        figure  = plt.figure(figsize=[10,6], facecolor = '#b3e6ec', frameon=True, edgecolor = "black", 
                         constrained_layout = True, dpi = 200)
        plt.subplot(412, projection=None, polar=False, facecolor='#b3e6ec' )      

        # boxplot
        data.boxplot(i, notch=False, vert=False, grid =True, patch_artist = True, whis=2.0, showfliers=True, showmeans=True,
                     capprops = dict(color = 'black'), boxprops=dict(facecolor='#006699', color='black'),
                     whiskerprops = dict(color = 'black'), flierprops = dict(color ='black'), 
                     medianprops = dict(color='black'),
                     meanprops = dict(color='black'))
        plt.xlabel(i, fontsize= 9)    
        plt.title("Boxplot of " + i, fontsize= 9)

        plt.savefig('boxplotcont%03s.png'%(i))
        plt.show()

        # histogram
        plt.hist(data[[i]], bins=None, density=True, cumulative= False, histtype='bar', align='mid', orientation='vertical', 
                 rwidth=None, log=False,  color="#191970", stacked=False,  edgecolor="black")
        plt.xlabel(i, fontsize= 9)    
        plt.title("Histogram of " + i, fontsize= 9)

        plt.savefig('histcont%03s.png'%(i))
        plt.show()


# ### Suggestion 6.1: User input to determine accuracy of variables graphed and to rectify errors based on feedback given by user. In this version, plotgrid will be created instead of  individual graphs.

# In[ ]:


#Goal: Since our previous codes are not entirely generalized to all  datasets, there is a chance that a variable
#will be wrongly categorized into discrete,continuous,categorical. To prevent this from happening, we allow our user to
#change  categories before plotting graphs. Our process involves removal and appending of lists with variable names. Once all
#lists contain  accurate var names, a plotgrid is plotted using the above code. This shortens  our code, however, we  believe that
#this code  can be made even better with time by including Try-Except, further shortening of code, etc. 

def Graph_v5(data):
    import pandas as pd
    import numpy as np
    import  matplotlib.pyplot as plt
    import seaborn as sns

    #initial summary of data types, data categories are given for the user to scan through
    desc=data.dtypes  #gives whether data is  int/float/str
    discrete = []
    continuous = []
    #initial basic categorization
    categorical = list(data.select_dtypes(include = ['object']))
    numerical = list(data.select_dtypes(include = ['number']))

    #better categorization (but best option that can be handled by our code)
    for i in numerical:
        if (data[i].dtype == np.int64) and (len(set(data[i])) < 10):        
            discrete.append(i)
        elif (data[i].dtype == np.float64) or (data[i].dtype == np.int64 and len(set(data[i])) > 10):
            continuous.append(i)
            
    #gives the best possible categorizations of data types, categories
    print('Categorical:',categorical, "\n")
    print('Discrete:', discrete, "\n")
    print('Continuous:', continuous, "\n")
    print('Description:', desc, "\n") 
    
    #user input to improve categorizations
    q1 = input("Are the variables categorized correctly? yes/no: ")
    if q1.lower()=="yes":
        #if yes, all graphs will be printed as a plotgrid
        #specifies size, spacing of each figure in grid
        fig = plt.figure(figsize=(15,150))
        a=len(data.columns) #number of rows
        b=2 # number of columns
        c=1 # initialize plot counter

        for i in discrete:
            #creates  barcharts for discrete vars
            plt.subplot(a, b, c)
            plt.title('{} (bar), subplot: {},{},{}'.format(i, a, b, c))
            data[i].value_counts().plot(kind='bar',color="pink",width=0.5,  fontsize=9,rot=10, grid=False)
            plt.title("Bar chart", fontsize = 9)
            plt.xlabel(i, fontsize = 9)
            plt.ylabel("Frequency", fontsize = 9)
            c = c + 1

        for i in continuous:
            #creates  boxplots and histplots for continuous vars
            plt.subplot(a, b, c)
            plt.title('{} (hist), subplot: {},{},{}'.format(i, a, b, c))
            plt.xlabel(i)
            sns.histplot(data[i])
            c = c + 1

            plt.subplot(a, b, c)
            plt.title('{} (box), subplot: {},{},{}'.format(i, a, b, c))
            plt.xlabel(i)
            plt.boxplot(x = data[i], vert=False)
            c = c + 1

        for i in categorical:
            #creates  barcharts for categorical vars
            plt.subplot(a, b, c)
            plt.title('{} (bar), subplot: {},{},{}'.format(i, a, b, c))
            data[i].value_counts().plot(kind='bar',color="turquoise",width=0.5, fontsize=9,rot=10 , grid=False)
            plt.title("Bar chart", fontsize = 9)
            plt.xlabel(i, fontsize = 9)
            plt.ylabel("Frequency", fontsize = 9)
            c = c + 1

        plt.savefig(cwd+'Plotgrid.png') #saves graph in give directory
        plt.show()

    elif q1.lower()=="no":
        while True:
            q2=input("Which variable is not categorized correctly?: ")
                
            if q2 in categorical:
                categorical.remove(q2)
                q3=input("Is this variable discrete/continuous (disc/cont):")
                if (q3 == "discrete") or (q3 == "disc"):
                    discrete.append(q2)
                    print("The discrete numerical variables now are: ", discrete)
                if (q3 == "continuous") or (q3 =="cont"):
                    continuous.append(q2)
                    print("The continuous numerical variables now are: ", continuous)

            elif q2 in discrete:
                discrete.remove(q2)
                q4=input("Is this variable categorical/continuous (cat/cont):")
                if (q4.lower() == "cat") or (q4.lower() == "categorical"):
                    categorical.append(q2)
                    print("The categorical variables now are: ", categorical)
                if (q4.lower() == "continuous") or (q4.lower() == "cont"):
                    continuous.append(q2)
                    print("The continuous numerical variables now are: ", continuous)

            else:
                continuous.remove(q2)
                q5=input("Is this variable discrete/categorical (disc/cat):")
                if (q5.lower() == "discrete") or (q5.lower() =="disc"):
                    discrete.append(q2)
                    print("The discrete numerical variables now are: ", discrete)
                if (q5.lower() == "cat") or (q5.lower() == "categorical"):
                    categorical.append(q2)
                    print("The categorical variables are: ", categorical)
        
            q6 = input("Are the variables categorized correctly? yes/no: ")
            if q6.lower()=="yes":
                break 

    print("\n---------------------", "\nCategorical:",categorical,"\nContinuous:",continuous, "\nDiscrete:",discrete)
    #Printing graphs after all the categories are rectified
    #specifies size, spacing of each figure in grid
    
    fig = plt.figure(figsize=(15,150))
    a=len(data.columns) #number of rows
    b=2 # number of columns
    c=1 # initialize plot counter

    for i in discrete:
        #creates  barcharts for discrete vars
        plt.subplot(a, b, c)
        plt.title('{} (bar), subplot: {},{},{}'.format(i, a, b, c))
        data[i].value_counts().plot(kind='bar',color="pink",width=0.5,  fontsize=9,rot=10, grid=False)
        plt.title("Bar chart", fontsize = 9)
        plt.xlabel(i, fontsize = 9)
        plt.ylabel("Frequency", fontsize = 9)
        c = c + 1

    for i in continuous:
        #creates  boxplots and histplots for continuous vars
        plt.subplot(a, b, c)
        plt.title('{} (hist), subplot: {},{},{}'.format(i, a, b, c))
        plt.xlabel(i)
        sns.histplot(data[i])
        c = c + 1

        plt.subplot(a, b, c)
        plt.title('{} (box), subplot: {},{},{}'.format(i, a, b, c))
        plt.xlabel(i)
        plt.boxplot(x = data[i], vert=False)
        c = c + 1

    for i in categorical:
        #creates  barcharts for categorical vars
        plt.subplot(a, b, c)
        plt.title('{} (bar), subplot: {},{},{}'.format(i, a, b, c))
        data[i].value_counts().plot(kind='bar',color="turquoise",width=0.5, fontsize=9,rot=10 , grid=False)
        plt.title("Bar chart", fontsize = 9)
        plt.xlabel(i, fontsize = 9)
        plt.ylabel("Frequency", fontsize = 9)
        c = c + 1

    plt.savefig('Plotgrid.png')
    plt.show()


# In[ ]:


Graph_v5(data)
