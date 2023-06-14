#load libraries 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv(r"Netflix_Revenue.csv")

#view the data 
df.head()

#view the total number of rows and columns of the dataframe 
df.shape

#Data Visualisation 

#Netflix global users vs time 
plt.figure(figsize=(15,10),dpi=700, facecolor= "red")
plt.plot(df['Date'],df["Netflix Global Users"],color= "red")
plt.xlabel("Date",fontdict= {'family':'fantasy','color':'black','size':15})
plt.xticks(rotation=90, ha='right')
plt.ylabel("Netflix Global Users",fontdict= {'family':'fantasy','color':'black','size':15})
plt.title("Netflix Global Users vs Time", fontdict= {'family':'fantasy','color':'black','size':20})
plt.show()

#Global revenue with time 
plt.figure(figsize=(15,10),dpi=700, facecolor="red")
plt.plot(df['Date'],df["Global Revenue"],color= "blue")
plt.xlabel("Date",fontdict= {'family':'fantasy','color':'black','size':15})
plt.xticks(rotation=90, ha='right')
plt.ylabel("Global Revenue",fontdict= {'family':'fantasy','color':'black','size':15})
plt.title(" Global Revenue vs Time",fontdict= {'family':'fantasy','color':'black','size':20})
plt.show()

#Domestic vs international revenue trends 
fig, axs = plt.subplots(2)
fig.suptitle('Domestic vs International Revenue Trends',fontdict= {'family':'fantasy','color':'blue'})
axs[0].plot(df['Date'],df["Domestic Revenue"],color= "green")
axs[1].plot(df['Date'],df["International Revenue"],color= "brown")
axs[0].set_title('Domestic Revenue vs Time', fontdict= {'family':'fantasy','color':'black','size':10})
axs[1].set_title('International Revenue vs Time',fontdict= {'family':'fantasy','color':'black','size':10})
plt.xticks(rotation=90, ha='right')
for ax in axs.flat:
    ax.set(xlabel='Date', ylabel='Revenue')
for ax in axs.flat:
    ax.label_outer()

#Domestic vs Internation free trials trends 
fig, axs = plt.subplots(2)
fig.suptitle('Domestic vs International Free Trialers Trends',fontdict= {'family':'fantasy','color':'purple'})
axs[0].plot(df['Date'],df["Domestic Free Trialers"],color= "green")
axs[1].plot(df['Date'],df['Interntaional Free Trialers'],color= "brown")
axs[0].set_title('Domestic Free Trialers vs Time', fontdict= {'family':'fantasy','color':'black','size':10})
axs[1].set_title('International Free Trialers vs Time',fontdict= {'family':'fantasy','color':'black','size':10})
plt.xticks(rotation=90, ha='right')
for ax in axs.flat:
    ax.set(xlabel='Date', ylabel='Free Trialers')

for ax in axs.flat:
    ax.label_outer()

