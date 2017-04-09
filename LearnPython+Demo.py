
# coding: utf-8

# In[3]:

get_ipython().system(u'curl -L https://www.dropbox.com/s/qsodvwpcyu3mxei/NYC%20Restaurants.csv?dl=1 -o NYC_Restaurants.csv')


# In[4]:

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[5]:

rests = pd.read_csv("NYC_Restaurants.csv")


# In[6]:

mRests=rests[rests['BORO']=="MANHATTAN"] 


# In[7]:

list(mRests.columns.values)


# In[8]:

mRests = mRests[mRests['GRADE']!="Not Yet Graded"]


# In[9]:

mRests = mRests[pd.notnull(mRests["GRADE"])]


# In[10]:

mRests = mRests[pd.notnull(mRests["SCORE"])]


# In[11]:

mRests["GRADE"] = mRests["GRADE"].astype("category",categories = ["A","B","C","P","Z"], ordered = True)


# In[12]:

mRests = mRests.reset_index(drop=True)
mRests.head()


# In[13]:

mRests['SCORE'].describe()


# In[14]:

# f, ax = plt.subplots()
data = mRests['SCORE']
plt.hist(data)
plt.xlabel("Score")
plt.ylabel("Count")
plt.title("Frequency of Scores")
plt.show()


# In[15]:

mRests['SCORE'].hist(bins=5)
plt.title("Frequency of Scores")


# In[16]:

mRests["GRADE"].value_counts().plot(kind = "bar")


# In[17]:

get_ipython().system(u'pip install seaborn')


# In[18]:

import seaborn as sns


# In[19]:

sns.set(style="whitegrid", color_codes=True) ### Updates only the seaborn charts created after the fact
plt.style.use('seaborn-colorblind') ### updates for all graphs in the page created after the fact


# In[20]:

sns.stripplot(x="GRADE", y="SCORE", data = mRests, jitter=True)


# In[21]:

sns.boxplot(x="GRADE", y="SCORE", data = mRests, hue= "CRITICAL FLAG")


# In[22]:

get_ipython().system(u'pip install inflect')

import inflect
p = inflect.engine()
word_to_number_mapping = {}

for i in range(1, 200):
    word_form = p.number_to_words(i)  # 1 -> 'one'
    ordinal_word = p.ordinal(word_form)  # 'one' -> 'first'
    ordinal_number = p.ordinal(i)  # 1 -> '1st'
    word_to_number_mapping[ordinal_word] = ordinal_number  # 'first': '1st'

import re
for i in range(len(mRests)):

    street= mRests['STREET'][i].split()    

    for j in range(len(street)):
        if street[j].lower() in word_to_number_mapping:

            street[j]=  word_to_number_mapping[street[j].lower()]
            print(street[j])
    for j in range(len(street)):
        if re.findall(r'([0-9]+(st|rd|th|nd)+)', street[j].lower())==[]:
            if street[j].isdigit():
                val=(street[j])
                street[j]=street[j].replace(str(val), str(p.ordinal(val)))    
        streetFull = ' '.join(street)
        mRests.set_value(i,'STREET',streetFull)

mRests["Address"]=mRests['BUILDING'].map(str)+ " " + mRests['STREET'].map(str)+ ", " + mRests['ZIPCODE'].map(str)


# In[23]:

mRests["Address"]


# In[24]:

import random
np.random.seed(seed=10)
rows = np.random.choice(mRests.index.values, 100)
samp = mRests.ix[rows]
samp= samp.reset_index(drop=True)
samp


# In[25]:

get_ipython().system(u"curl -L 'https://www.dropbox.com/s/p4145z5odvlypez/address.csv?dl=1' -o address.csv")
adds = pd.read_csv("address.csv")
samp['lat']= adds['latitude']
samp['long']= adds['longitude']


# In[26]:

get_ipython().system(u'conda install basemap --yes')


# In[27]:

from mpl_toolkits.basemap import Basemap
map = Basemap(projection='merc',
    resolution = 'h', area_thresh = .01,
    lat_0=40.7831, lon_0= -73.9712,
    llcrnrlon=-74.03, llcrnrlat=40.701,
    urcrnrlon=-73.86, urcrnrlat=40.901)

map.drawcoastlines()
map.drawcountries()
map.drawstates()
map.drawrivers()
map.fillcontinents(color = 'gainsboro')
map.drawmapboundary(fill_color='steelblue')

map.plot(samp['lat'],samp['long'],'bo', markersize = 24)


# In[28]:

get_ipython().system(u'pip install folium')


# In[29]:

import folium

mCluster = folium.Map(location=[40.7831, -73.9712], zoom_start =20)
# marker_cluster = folium.MarkerCluster().add_to(mCluster)
for i in range(len(samp)):
    if samp["GRADE"][i] =="A":
        folium.Marker([samp['lat'][i],samp['long'][i]], popup= "Name: " + str(samp['DBA'][i])+ '\n' + "Score: " + str(samp["SCORE"][i]) + '\n'+'Grade: '+ str(samp["GRADE"][i]),
                      icon=folium.Icon(color="green", icon='no-sign')).add_to(mCluster)
    elif samp["GRADE"][i]=="B":
         folium.Marker([samp['lat'][i],samp['long'][i]], popup= "Name: " + str(samp['DBA'][i])+ '\n' + "Score: " + str(samp["SCORE"][i]) + '\n'+'Grade: '+ str(samp["GRADE"][i]),
                      icon=folium.Icon(color='blue',icon='no-sign')).add_to(mCluster)
    else:
         folium.Marker([samp['lat'][i],samp['long'][i]], popup= "Name: " + str(samp['DBA'][i])+ '\n' + "Score: " + str(samp["SCORE"][i]) + '\n'+'Grade: '+ str(samp["GRADE"][i]),
                      icon=folium.Icon(color='red',icon='no-sign')).add_to(mCluster)


# In[ ]:




# In[30]:

mCluster


# In[31]:

mCluster.save('restaraunts.html')


# In[35]:

get_ipython().system(u'ls')


# In[37]:

get_ipython().system(u'curl --upload-file restaraunts.html https://transfer.sh/restaruants.html')


# In[93]:

from bokeh.io import output_notebook
output_notebook()


# In[94]:

from bokeh.charts import Histogram, output_file, show


# In[96]:

p1 = Histogram(samp["SCORE"])
show(p1)


# In[103]:

p2 = Histogram(mRests,'SCORE', color='GRADE',
              title="Score Grouped by Grade", bins = 15,
              legend='top_left')

show(p2)


# In[99]:

from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure

tab1 = Panel(child=p1, title="Frequency of Score")
tab2 = Panel(child=p2, title="By Grade")

tabs = Tabs(tabs=[ tab1, tab2 ])
show(tabs)


# In[100]:

import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
init_notebook_mode(connected=True)


# In[102]:

x = mRests['GRADE']

tr1 = go.Histogram(x=x, histnorm='probability density', 
                xbins=dict(start=np.min(x), size= 0.25, end= np.max(x)),
                marker=dict(color='rgb(0,0,100)'))
title =" Probability Density of Grades"

layout = dict(
            title=title,
            autosize= True,
            bargap= 0.015,
            height= 600,
            width= 700,       
            hovermode= 'x',
            xaxis=dict(
            autorange= True,
            zeroline= False),
            yaxis= dict(
            autorange= True,
            showticklabels= True,
           ))
fig1 = go.Figure(data=go.Data([tr1]), layout=layout)
iplot(fig1)


# In[105]:

samp['text'] = "Name: " + samp['DBA'].astype(str)+ '\n' + "Score: " + samp["SCORE"].astype(str) + '\n'+'Grade: '+ samp["GRADE"].astype(str)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

data = [ dict(
        type = 'scattergeo',
        locationmode = 'USA-states',
        lon = samp['long'],
        lat = samp['lat'],
        text = samp['text'],
        mode = 'markers',
        marker = dict( 
            size = 8, 
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = 0,
            color = samp['SCORE'],
            cmax = samp['SCORE'].max(),
            colorbar=dict(
                title="Restaurant Score"
            )
        ))]

layout = dict(
        title = 'Restaurant Scores',
#         colorbar = True,   
        geo = dict(
            scope='usa',
#             projection=dict( type='albers usa' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5        
        ),
    )

fig = dict( data=data, layout=layout )
iplot(fig)

