#!/usr/bin/env python
# coding: utf-8

# ##  Assignment: Predicting Housing Prices 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[ ]:


data = pd.read_csv(r"kc_house_train_data.csv")
data.head(2)


# In[ ]:


data.describe()


# In[549]:


data.info()


# ### Our initial hypotheses were:
# 
# 1. Prices are positively correlated with number of bedrooms,bathrooms, living and lot area in sqft, grades, views, waterfront presence, condition, basement area.
# 2. Prices are negatively correlated with year of renovation (if considered as number of years since renovation, ie, fewer years since renovation-->newer property-->higher price)
# 3. Certain zipcodes will have higher house prices due to higher living,lot area, higher  number of views, waterfront, etc. 
# 4. We assume a high correlation between some sets of predictors. For eg, bedroooms and sqftliving, number of floors and basements
# 

#  
# Since the remaining variables have a large number of values as outliers, we will not remove or alter them as of now.  We will  work on them  during feature engineering.

# ### Experiment: Univariate Analysis
# 

# In[666]:


#We are using the graph we created for our final python assignment
import os
os.chdir("/Users/aanchalkhanna72/Downloads/")
from graphsave import *
Graph_v5(data)


# In[550]:


data.hist(column="price", grid=False, figsize=(6,4), edgecolor = 'black')

plt.xlabel('price')
plt.title('Histogram of price')

plt.show()


# In[551]:


data.hist(column="sqft_living", grid=False, figsize=(6,4), edgecolor = 'black')

plt.xlabel('sqft_living')
plt.title('Histogram of sqft_living')

plt.show()


# In[552]:


data.hist(column="sqft_lot", grid=False, figsize=(6,4), edgecolor = 'black')

plt.xlabel('sqft_lot')
plt.title('Histogram of sqft_lot')

plt.show()


# In[13]:


data.hist(column="sqft_above", grid=False, figsize=(6,4), bins=15, edgecolor = 'black')

plt.xlabel('sqft_above')
plt.title('Histogram of sqft_above')

plt.show()


# In[667]:


data.hist(column="sqft_basement", grid=False, figsize=(6,4), bins=15, edgecolor = 'black')

plt.xlabel('sqft_basement')
plt.title('Histogram of sqft_basement')

plt.show()


# In[15]:


data.hist(column="sqft_living15", grid=False, figsize=(6,4), bins=15, edgecolor = 'black')

plt.xlabel('sqft_living15')
plt.title('Histogram of sqft_living15')

plt.show()


# In[16]:


data.hist(column="sqft_lot15", grid=False, figsize=(6,4), bins=15, edgecolor = 'black')

plt.xlabel('sqft_lot15')
plt.title('Histogram of sqft_lot15')

plt.show()


# ### UNIVARIATE SUMMARY
# 
# 9761 houses were sold in King County between the year 2014-15. Majority of the houses sold were not waterfront properties and had an adequate view. The average price of a house was  $542,735 with a large  variability in prices.  The median price was less  than  the mean price which indicated a right skew of price distribution. In other words, most of the house prices lay on the lower end of the prices spectrum. On an avg, houses sold had 2 bathrooms, 1-1.5 floors (indicating presence of attic  space), a grade of 7.5 on a scale of 1-13 and a living area of 2100 sq ft. Most houses didn't have basements.
# 
# 75% of the houses had a living area less than 2570 sq ft, but alarmingly, the remaining 25% of the houses had a living  area between a wide range of 2570-12050 sq ft. There were many anomalies in the characteristics of the houses, which indicated either incorrect data collection or presence of outliers that were skewing the information we were seeing. The average lot size for houses was about  15000 sq ft, the minimum being 520 sq ft. 75% of the houses had a lot size of  less than 10.5k sq ft. Due to the pressence of  outliers, the mean here was being pulled up to a higher number. According  to the latest data collection in  2015, the avg lot size of the houses sold decreased from 2100  ssq ft to  1992 sqft for all quartiles. The oldest house was built in 1900 whereas the most recent house was built in 2014. 
# 

# #### SCOPE: QUESTIONS FOR BIVARIATE AND MULTIVARIATE ANALYSIS
# 1. Which pincode(lat/long) has the highest/lowest price?
# 2. Given that the number of bedroooms is 3 (avg)/lot size is 7642 sq ft(avg)/floors  is 1.5 (individually), what are the different house prices?
# 3. Year  built vs price  increase. Is there a premium to  be paid  by buyer  for older houses considering the architecture? See Heritage Homes
# 4. Price difference of Renovated  homes (code renovated  homes as 0-not renovated,1-renovated)
# 5. How are grades  determined? (linear regression can be done  on grades  too) What is the impact of higher grades on prices? Do certain areas/zipcodes get better grades?
# 6. What to do with  outliers?
# 7. Mapping lat/long to check if houses are in vicinity? What are the amenities nearby - schools, libraries, grocery stores, malls, etc.?
# 8. Check for  multicollinearity: condition, renovation; sqftliving:bedrooms
# 9. Check for Correlation: a. Basements and prices as basement usually has many amenitiess, home theatre,etc., 10. yr.built, zipcode, prices (some areas have more  heritage homes) relationship
# 

# ###  Experiment:  Bivariate Analysis

# In[668]:


plt.figure(figsize=(20,20))
sns.scatterplot(x='bedrooms', y='zipcode' , data=data,)
plt.yticks(np.arange(98000, 98200, 2))
plt.title('price and bedrooms scatterplot')
#plt.savefig('zipcode-vs-price-scatter.png')
plt.show()


# In[669]:


plt.figure(figsize=(20,20))
sns.scatterplot(x='price', y='zipcode' , data=data,)
plt.yticks(np.arange(98000, 98200, 2))
plt.title('price and zipcode  scatterplot')
#plt.savefig('zipcode-vs-price-scatter.png')
plt.show()


# In[670]:


plt.figure(figsize=(20,20))
sns.scatterplot(x='price', y='bathrooms', data=data,)
plt.title('price and bathrooms scatterplot')
plt.show()


# In[671]:


plt.figure(figsize=(20,20))
sns.scatterplot(y='price', x='sqft_living' , data=data)
plt.title('price and sqft_living scatterplot')
plt.show()


# In[672]:


plt.figure(figsize=(20,20))
sns.scatterplot(x='price', y='floors' , data=data,)
plt.title('price and floors scatterplot')
plt.show()


# In[673]:


plt.figure(figsize=(20,20))
sns.scatterplot(x='price', y='sqft_lot', data=data,)
plt.title('price and sqft_lot scatterplot')
plt.show()


# In[674]:


plt.figure(figsize=(20,20))
sns.scatterplot(y='price', x='yr_built',data=data,)
plt.title('price and year built scatterplot')
plt.show()


# In[675]:


plt.figure(figsize=(20,20))
sns.scatterplot(y='price',x='house_age' , data=data)
plt.title('price and age of house scatterplot')
plt.show()


# In[676]:


plt.figure(figsize=(20,20))
sns.scatterplot(y='price',x='grade' , data=data)
plt.title('price and grade scatterplot')
plt.show()


# In[677]:


plt.figure(figsize=(20,20))
sns.scatterplot(y='zipcode',x='grade' , data=data)
plt.yticks(np.arange(98000, 98200, 2))
plt.title('grade and zipcode')
plt.show()


# In[678]:


plt.figure(figsize=(20,20))
sns.scatterplot(x='condition',y='house_age' , data=data)
plt.title('age of house and condition scatterplot')
plt.show()


# In[565]:


#creating a new variable "house_age" 
house_age= 2015 - data['yr_built']


# In[566]:


data.insert(21, 'house_age', house_age, True)


# In[568]:


data.corr()


# In[36]:


plt.figure(figsize=(20,8))
sns.heatmap(data.corr())


# ### BIVARIATE SUMMARY 
# **ANSWERS TO QUESTIONS FOR BIVARIATE AND MULTIVARIATE ANALYSIS:**
# 1. Which pincode(lat/long) has the highest/lowest price?
# 
# Certain pincodes are associated with higher price range whereas some are associated with lower prices. The latter  category has lower variability and more consistent observations, whereas zipcodes with highly priced houses have houses in the lower or mid range as well. 
# 
# 2. Do prices increase as number of rooms/bathrooms increases? Given that the number of bedroooms is 3 (avg), what are the different house prices?
# Surprsingly, no. We notice that these two  variables have a low (linear) correlation of 0.30. Additionally, when we plotted a scatterplot for price and beddrooms, we noticed that for given number of bedrooms, there was a large  vavriability in prices. Some  outliers are present with high number of bedrooms but low prices, which is intriguing. 
# 
# On the other hand, bathrooms and  prices have a higher correlation of 0.52. Even in our boxplot, we are  able to notice that there is a ladder-like trend, inddicating that as number of bathrooms increase,  the price range also begins to increase. 
# 
# 3. Given that the living size is 2100 sq ft(avg), what are the different house prices? 
# As  hypothesized, there  is a  strong correlation between house prices and sqft living space. This is also visible in the scatterplot where prices seem to increase slowly (flatter slope) as sqft_living increases. There is less variability in prices at 2100 sq ft,  i.e., prices are in the lower range for these houses. 
# 
# 4.  Correlation between lot size and prices
# Contrary to our hypothesis, there is a really low, almost negligible, linear correlation between lot sizes and prices. This is counter-intuitive as our understanding was that  houses  with bigger lot sizes would cover more sqft area and therefore have higher prices. Perhaps this is dependent on other factors such as zipcode. 
# 
# 5. Year  built vs price  increase. Is there a premium to  be paid  by buyer  for older houses considering the architecture? See Heritage Homes
# 
# To assess this, we created a variable called house_age which is the difference betweem 2015 and the year built. Our hypotheses is disproved as older houses aren't associated with higher prices. In fact, a small number of newer, modern houses are associated with higher prices, however, these could just  be outliers.  
# 
# 6. Price difference of Renovated  homes (code renovated  homes as 0-not renovated,1-renovated)
# Looking at average prices of renovated houses and non-renovated  houses in Excel, we find that the average price  of renovated  homes is higher (about 650k vs. 500k). We will be categorizing these into dummy variables during feature engineering.
# 
# 7.  What is the impact of higher grades on prices? Do certain areas/zipcodes get better grades?
# There is a high correlation between grades and prices (0.66). Higher grades are related with higher  prices. We cannot read  the correlation coeffiecient for zipcode and grades,  as the zipcode data is being read as numerical data.
# 
# 8. Does having a waterfront increase  the price of the home?
# Surprisingly,no. There is low correlation between prices and presence of waterfront.  
# 
# 
# 9. Check for  multicollinearity: condition, house_age; sqftliving:bedrooms
# a.condition, house_age: low correlation (0.35)
# b.sqftliving:bedrooms: moderately correlated (0.56)
# 
# 10. Check for Correlation: 
# a. Basements and prices (as basement usually has many amenitiess, home theatre,etc.): low correlation (0.30)
# b. house_age, zipcode: unable to say as zipcode can't be handled numerically
# 

# ### Experiment: Data Cleaning before Model Fittinng

# As observed earlier, we found many outliers across the features, however, we chose to keep the outliers as they were large in number, and hence did not indicate incorrect data collection. However, there were a few observations  that we cleaned up as they had values which did not seem plausible considering its other features. For instance, there was a  house with  33 bedrooms with 1620 sqft  of living space and 6000 sqft  lot space. It had 1.75  bathrooms. Its other features (highlighted below) seem plausible so we decided to correct the bedrooms to 3  (Which is also  the  average number in our dataset).

# In[569]:


#updating bedroom values for outliers/anomalies with average bedrooms
data[data.bedrooms==33]


# In[570]:


#updating bedroom values for outliers/anomalies with average bedrooms where the remaining features are plausible
data.at[7204,'bedrooms'] = 3


# In[571]:


data.at[7204,'bedrooms']


# In[572]:


#updating bedroom values for outliers/anomalies with average bedrooms where the remaining features are plausible
data[data['bedrooms']==0]


# In[573]:


data.at[[8840,8338,2228,3177,4472,4507],'bedrooms'] = 3


# In[574]:


data.at[[8840,3177,4472,4507],'bathrooms'] = 2


# In[575]:


data.iloc[[8840,8338,2228,3177,4472,4507]]


# In[576]:


data.iloc[[8840,3177,4472,4507]]


# In[577]:


np.mean(data[data['bathrooms']==0.75])


# In[578]:


np.mean(data[data['bathrooms']==1])


# In[579]:


#updating to 2 rooms as the avg bedrooms of houses with 1 and 0.75 bathrooms are 2.63 and 2.02 respectively
data.at[[8338,2228],'bedrooms']=2


# In[580]:


data.columns


# ### Experiment: Initial Decision Tree Model Fitting Step (without Feature engineering)

# In[581]:


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import confusion_matrix
from  sklearn import tree


# #### Trial Model 1

# In[679]:


#We chose these variables because they had highest correlation with house prices 
X_train=data[["sqft_living","grade","bathrooms"]]
y_train=data[["price"]]


# In[680]:


# Train-Validate Split


# In[681]:


#function test-train split
from sklearn.model_selection import  train_test_split


# In[682]:


(X_train, X_valid, y_train, y_valid) = train_test_split(X_train, y_train, test_size=0.25)


# In[683]:


len(X_train), len(X_valid), len(y_train), len(y_valid)


# In[684]:


# Fitting a Regression tree Model


# In[685]:


#Set up model
reg_tree=DecisionTreeRegressor(max_depth=4, min_samples_leaf=3)
reg_tree.fit(X_train,y_train)


# In[686]:


y_pred=reg_tree.predict(X_valid)


# In[687]:


y_valid=np.array(y_valid)


# In[61]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('Model1.jpeg')
plt.show()


# In[ ]:


# Calculating Error metrics (RMSE, MAPE) and R**2


# In[688]:


# RMSE (Root Mean Squared Error)
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[689]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# #### SCOPE: In this model, we notice that grades, sqft_living are the 2 variables where the first few splits take place. Most of the  stem nodes have  these  variables. The MAPE shows that  on  ann average, the predicted values are away from the actual values by  65%, which is a high  number.  We would like to add 2 new predictors 'sqft_lot','house_age', which we  believe will bring down the error rate. We chose these  variables because we assumed  that  a higher  lot size  would indicate a  higher total sq ft area, thereby increasing the house price. Additionally, although house age doesn't have a linear correlation with price, we believe that older houses will have a lower prices and vice versa. 

# ### Experiment: Second Trial  (following the  same steps for all  consecutive  trials)
# 

# In[584]:


# Setting Predictors and Target Variable for Trial 2

X_train = data[[ 'sqft_living', 'grade', 'bathrooms','sqft_lot', 'house_age'] ]
y_train= data.price


# In[585]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25,  random_state=10)


# In[586]:


len(X_train), len(X_valid)


# In[67]:


# Fitting a Regression tree Model

reg_tree = DecisionTreeRegressor(max_depth=4, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[68]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('Model2.jpeg')
plt.show()


# In[69]:


y_pred = reg_tree.predict(X_valid)
y_pred


# In[70]:


y_valid=np.array(y_valid)


# In[71]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[72]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# #### SCOPE: In this model, we notice a  drastic change in MAPE. The predicted values are away from the actual values by 31.4%. In the decision tree, we see that bathrooms is not considered for splits and it has been  pushed  out of the tree altogether. We can say that the variable  "bathrooms" is not as important for  determining prices. We wanted to check the variable 'bedrooms' because there  was no collinearity between bedrooms and house prices (stated in univariate analysis). 

# ### Experiment: Third Trial 

# In[587]:


# Setting Predictors and Target Variable for Trial 3

X_train = data[['sqft_living', 'grade','bathrooms', 'sqft_lot','house_age','bedrooms'] ]
y_train = data.price


# In[588]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25,  random_state=10)


# In[152]:


# Fitting a Regression tree Model
reg_tree = DecisionTreeRegressor(max_depth=4, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[153]:


y_pred = reg_tree.predict(X_valid)
y_pred


# In[154]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('Model3.jpeg')
plt.show()


# In[147]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[148]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# #### SCOPE: In this model, we notice a  negligible change in MAPE. The predicted values are away from the actual values by 31.4%. In the decision tree, we see again that only house_age,sqft_living and grade are considered for splits. We wonder about the relevance of the additional variables added to the model. We want to now  add 'condition' and 'floors' variables to the model because our intuition is that a potential housebuyer would pay more for a house with additional floors (and living space) as well as a house in  better condition.

# ### Fourth Trial

# In[589]:


# Setting Predictors and Target Variable for Trial 4

X_train = data[['sqft_living', 'grade','sqft_lot','bedrooms','bathrooms','condition','floors'] ]
y_train = data.price


# In[590]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25,  random_state=10)


# In[591]:


# Fitting a Regression tree Model
reg_tree = DecisionTreeRegressor(max_depth=4, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[198]:


y_pred = reg_tree.predict(X_valid)
y_pred


# In[201]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('Model4.jpeg')
plt.show()


# In[203]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[204]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# #### SCOPE: In this model, we notice an increase in MAPE. The predicted values are away from the actual values by 32.9%. We notice that the  variable "condition" is being  used for the purpose of splitting, whereas bedrooms and bathrooms continue  to be left out of the decision tree, thereby confirming the irrelevance of  these variables. Presence of  a water  body and having a good view potentially increases the price of house.

# ### Experiment: Fifth Trial

# In[592]:


# Setting Predictors and Target Variable for Trial 5
X_train = data[['sqft_living', 'house_age', 'grade', 'floors','sqft_lot','condition','waterfront','view'] ]
y_train = data.price


# In[593]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25,  random_state=10)


# In[594]:


# Fitting a Regression tree Model
reg_tree = DecisionTreeRegressor(max_depth=5, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[214]:


y_pred = reg_tree.predict(X_valid)
y_pred


# In[ ]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('Model5.jpeg')
plt.show()


# In[215]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[216]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# #### SCOPE: We see a drop in MAPE. Next, we want to remove "sqft_living" and replace it with "sqft_above" to see if it changes the MAPE. We asume that sqft_above is a proxy for sqft_living as it also represents  the size of the living space. 

# ### Sixth Trial

# In[595]:


X_train = data[['floors','sqft_above','grade', 'condition','waterfront','view','sqft_lot','house_age'] ]
y_train = data.price


# In[596]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25,  random_state=10)


# In[597]:


len(X_train),len(X_valid)


# In[220]:


reg_tree = DecisionTreeRegressor(max_depth=5, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[ ]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('Model6.jpeg')
plt.show()


# In[221]:


y_pred = reg_tree.predict(X_valid)
y_pred


# In[222]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[223]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# #### SCOPE: We see a drop in MAPE. Next, we want to add "sqft_basement" to see if it changes the MAPE. We asume that sqft_basement, in addition to sqft_living, is a better proxy for sqft_living as it  represents  the 'total' size of the living space. We also added bedrooms to see if it would make any difference, although there is no logical reason for  adding it over and above sqft_living.

# ### Experiment: Seventh Trial

# In[598]:


X_train = data[['floors','sqft_above','grade', 'condition','waterfront','view','sqft_lot','sqft_basement','house_age','bedrooms']]
y_train = data.price


# In[599]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25,  random_state=10)


# In[600]:


reg_tree = DecisionTreeRegressor(max_depth=5, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[274]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('Model7.jpeg')
plt.show()


# In[275]:


y_pred = reg_tree.predict(X_valid)
y_pred


# In[276]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[277]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# Since this is our lowest MAPE, we want to experiment with hypertuning the parameters of this model.

# In[279]:


#Hyperparameter tuning 
depth = np.arange(1,15)
mape = []

for k in depth:
    reg_tree = DecisionTreeRegressor(max_depth=k, min_samples_leaf=3)
    reg_tree.fit(X_train, y_train)
    y_pred = reg_tree.predict(X_valid)
    mape.append(np.mean(np.abs(y_valid - y_pred)/y_valid)*100) #MAPE


# In[379]:


mape


# In[380]:


plt.plot(depth, np.array(mape))
plt.show()


# Select  depth=7 or 8 to get  the best model without feature engineering. We chose depth=8 as it gave the lowest MAPE.

# In[382]:


reg_tree = DecisionTreeRegressor(max_depth=8, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)
y_pred=reg_tree.predict(X_valid)
# RMSE
rmse=np.sqrt(np.mean((y_valid - y_pred)**2))
mape=np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# In[286]:


rmse, mape


# #### SCOPE: Hypertuning the parameters has brought down  the RMSE and MAPE slightly. We will use this model on  our test data. Our intuition is that  zipcode,  as well as some other variables,  will be better predictors and will lower MAPE and RMSE. We will try to create these variables using  feature engineering methods.

# ### Experiment:  FEATURE ENGINEERING

# We are unable to use variables like zipcode, yr_renovated in our analysis as they are categorical variables. Additionally, we wanted to run our  regression tree on the  variable "basement" which simply indicates the presence of a basement (0 vs 1).

# In[601]:


#Pandas dummies for transforming zipcode variable
zipcodes = pd.get_dummies(data.zipcode,drop_first=True)
data = pd.concat([data, zipcodes], axis='columns')
data


# In[602]:


# dummies for transforming "yr_renovated" variable
data["renovated"]=np.where(data["yr_renovated"]>0,1,0)


# In[603]:


# dummies for transforming "sqft_basement" variable
data["basement"]=np.where(data["sqft_basement"]>0,1,0)


# In[612]:


# log transform of price
log_price = np.log(data.price)
data.insert(93, 'log_price', log_price, True)


# ### Experiment:   MODEL FITTING AFTER FEATURE ENGINEERING 

# #### Model 1:  Adding feature engineered variables to the best model we found before feature engineering  

# In[690]:


X_train=data[['floors','sqft_above','grade', 'condition','waterfront','view','sqft_lot',
               'sqft_basement','house_age','bedrooms','renovated','basement']]
y_train = data.price


# In[607]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25)


# In[460]:


reg_tree = DecisionTreeRegressor(max_depth=7, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[461]:


y_pred=reg_tree.predict(X_valid)
y_pred


# In[462]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('FEModel1.jpeg')
plt.show()


# In[464]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[465]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# In[466]:


#Hyperparameter tuning 
depth = np.arange(1,15)
mape = []

for k in depth:
    reg_tree = DecisionTreeRegressor(max_depth=k, min_samples_leaf=3)
    reg_tree.fit(X_train, y_train)
    y_pred = reg_tree.predict(X_valid)
    mape.append(np.mean(np.abs(y_valid - y_pred)/y_valid)*100) #MAPE


# In[467]:


mape


# In[411]:


plt.plot(depth, np.array(mape))
plt.show()


# In[468]:


#Choose k=8,9


# In[473]:


leaf = np.arange(1,15)
mape = []

for i in leaf:
    reg_tree = DecisionTreeRegressor(max_depth=9, min_samples_leaf=i)
    reg_tree.fit(X_train, y_train)
    y_pred = reg_tree.predict(X_valid)
    mape.append(np.mean(np.abs(y_valid - y_pred)/y_valid)*100) #MAPE


# In[474]:


mape


# Choose depth=9,leaf=2 where MAPE is the lowest (27.392)  , which is what we chose before hyperparameter tuning. This is the lowest  error we can get after feature engineering in this model. We will implement  this on the  test data. 

# #### Model 2: Our next model includes zipcodes created with one-hot encoding. 

# In[642]:


#We also tried feature engineering on zipcode, however, the MAPE was 0.86, which hinted at  an  error in our  encoding.
X_train = data.drop(['sqft_above','bedrooms','bathrooms','sqft_basement','floors','yr_built','yr_renovated','date','id','lat','long','sqft_living15','sqft_lot15','log_price','zipcode','waterfront'],axis=1)
y_train = data.price


# In[609]:


#Train-Validation Split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size = 0.25)


# In[477]:


reg_tree = DecisionTreeRegressor(max_depth=7, min_samples_leaf=3) 
reg_tree.fit(X_train, y_train)


# In[478]:


y_pred=reg_tree.predict(X_valid)
y_pred


# In[479]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('FEModel2.jpeg')
plt.show()


# In[480]:


# RMSE
np.sqrt(np.mean((y_valid - y_pred)**2))


# In[481]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_valid - y_pred)/y_valid)*100


# Our first model after feature engineering and hyperparameter tuning shows that the reduction in MAPE and  RMSE is very low. There is not  much difference that feature engineering has made in this model.
# Our second model post feature engineering of zipcodes shows a drastic change in  RMSE and MAPE. We are unsure of the reasons for this  drastic change. We will implement this model in our test data to see if it's replicable.

# ### Experiment: Model Testing  

# In[617]:


test=pd.read_csv("/Users/aanchalkhanna72/Downloads/kc_house_test_data.csv")
test.head()


# In[618]:


len(test)


# In[691]:


#cleaning the data, as was done with train data
data[data['bedrooms']==0]


# In[620]:


data[data['bathrooms']==0]


# In[621]:


test.info()


# Since there  no anomalies with bedrooms/bathrooms=0 or any null  values, we don't need to make any  changes.

# In[622]:


test.describe()


# In[623]:


#creating variable "house_age" and "log_price"
house_age = 2015 - test['yr_built']
test.insert(21, 'house_age', house_age, True)


# In[625]:


# log transform of price
log_price = np.log(test.price)
test.insert(22, 'log_price', log_price, True)


# In[626]:


#creating dummies for "renovated","basement"
test['renovated'] = np.where(test['yr_renovated'] > 0, 1, 0)
test['basement'] = np.where(test['sqft_basement'] > 0, 1, 0)


# In[627]:


#one-hot encoding for zipcodes
zipcodes = pd.get_dummies(test.zipcode, drop_first=True)
test = pd.concat([test, zipcodes], axis='columns')


# In[628]:


#Running two models on test data 
X_train=data[['floors','sqft_above','grade', 'condition','waterfront','view','sqft_lot',
               'sqft_basement','house_age','bedrooms','basement','renovated']]
y_train = data.price


# In[630]:


X_test=test[['floors','sqft_above','grade', 'condition','waterfront','view','sqft_lot',
               'sqft_basement','house_age','bedrooms','basement','renovated']]
y_test = test.price


# In[639]:


#fitting the model
reg_tree = DecisionTreeRegressor(max_depth=9, min_samples_leaf=2) 
reg_tree.fit(X_train,y_train)


# In[640]:


#predicting y_test in this the model
y_predt=reg_tree.predict(X_test)
y_predt


# In[641]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('TestModel1.jpeg')
plt.show()


# In[646]:


# RMSE
np.sqrt(np.mean((y_test - y_predt)**2))


# In[647]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_test - y_predt)/y_test)*100


# #### SCOPE: Our model shows MAPE of 29.06% which means that on aaverage,  our predicted values are 29% away  from the actual values. We will also try our model with zipcode on our test data.

# ###  Experiment: Running Model 2 (with zipcode feature engineer variable) on  test data

# In[643]:


X_train = data.drop(['sqft_above','bedrooms','bathrooms','sqft_basement','floors','yr_built','yr_renovated','date','id','lat','long','sqft_living15','sqft_lot15','log_price','zipcode','waterfront'],axis=1)
y_train = data.price


# In[644]:


X_test = test.drop(['sqft_above','bedrooms','bathrooms','sqft_basement','floors','yr_built','yr_renovated','date','id','lat','long','sqft_living15','sqft_lot15','log_price','zipcode','waterfront'],axis=1)
y_test = test.price


# In[654]:


#fitting the model
reg_tree = DecisionTreeRegressor(max_depth=9, min_samples_leaf=2) 
reg_tree.fit(X_train,y_train)


# In[655]:


#predicting y_test in this model
y_predt=reg_tree.predict(X_test)
y_predt


# In[656]:


#Plotting Reg Decision Tree
fig, axes  = plt.subplots(figsize=(3,3), dpi=500)
tree.plot_tree(reg_tree, feature_names=list(X_train), filled=False)
plt.savefig('TestModel2.jpeg')
plt.show()


# In[657]:


# RMSE (Root mean squared error)
np.sqrt(np.mean((y_test - y_predt)**2))


# In[660]:


# MAPE (Mean Absolute Percentage Error)
np.mean(np.abs(y_test - y_predt)/y_test)*100


# #### SCOPE: The error  in  our model is really low, almost next to 0 percent. This is highly suspicious, however, it is worth exploring as to why we are getting such a low MAPE.

# In[ ]:




