# An End to Boring Data with Python Visualizations Workshop

Put the days of trying to decipher meaning from boring spreadsheets behind you. Visualize data to give greater and immediate meaning to all those numbers with Python. We will explore the variety of options available for data visualization in Python using different libraries and understand which ones excel for what type of task. Create maps, statistical graphs and more detailed or interactive visualizations that can also be used on the web, ideal to take that blog post to a whole new level. This presentation tackles boring data by looking at python libraries available for mapping such as basemap and folium, statistical graphs from libraries such as matplotlib and seaborn, as well as libraries such as Bokeh and Plotly that can be used for making interactive graphs.

This workshop will walk through the steps of analyzing a NYC Restaurant Rating dataset and creating visualizations that can lead us to important realizations about the data. A completed version of the python code can be found [here](https://github.com/heatherbshapiro/an-end-to-boring-data/blob/master/An_End_to_Boring_Data.ipynb).

### The Slides for this talk are available [here](http://www.slideshare.net/HeatherShapiro/an-end-to-boring-data-with-visualizations-in-python?ref=https://www.linkedin.com/).

## Libraries Used
- [Pandas](http://pandas.pydata.org/)
  - Python library to provide data analysis features
  - Built on NumPy, SciPy, and matplotlib
  - Key components
    - Series
    - DataFrames
- [Matplotlib](http://matplotlib.org)
  - MATLAB like plotting framework
- [Seaborn](https://stanford.edu/~mwaskom/software/seaborn/)
  - Built on top of matplotlib
  - Creates more sophisticated graphs that look more professional
- [Basemap](http://matplotlib.org/basemap/users/index.html)
  - library for plotting 2D data on maps in Python
  - Had lots of problems with installation
- [Folium](https://pypi.python.org/pypi/folium)
  - Visualize data on a Leaflet map
  - Built-in tilesets from:
    - OpenStreetMap, MapQuest Open, MapQuest Open Aerial, Mapbox, and Stamen, and supports custom tilesets with Mapbox or Cloudmade API keys.
- [Bokeh](http://bokeh.pydata.org/en/latest/)
  - A Python interactive visualization library that targets modern web browsers for presentations.
- [Plot.ly](https://plot.ly/python/)
  - Make interactive charts online from Excel or CSV data.


## Steps to take
1. [Setting up Azure Notebooks](#1-setting-up-azure-notebooks)
2. [Importing dataset and loading necessary libraries](#2-importing-the-dataset-and-necessary-libraries)
3. [Understanding Pandas for data analysis](#3-understanding-pandas-for-data-analysis)
4. [Traditional Statistical Graphs](#4-creating-traditional-statistical-graphs)
    - Matplotlib
    - Pandas
    - Seaborn
5. [Mapping](#5-creating-maps)
    - Basemap
    - Folium
6. [Interactive Graphs](#6-creating-interactive-graphs)
    - Bokeh
    - Plot.ly


## 1. Setting up Azure Notebooks

To combat the problem of different operating systems and computer setups, we will be using [Azure Notebooks](https://notebooks.azure.com/) for our work environment. Azure Notebooks is a free service that provides Jupyter notebooks along with supporting libraries as a service. It means you can just login and use, no installation/setup is necessary.

1. Go to https://notebooks.azure.com/ and click [Sign in](https://notebooks.azure.com/account/signin) (or go directly to the sign in link).
2. If you already have a Microsoft account, please log in with that and skip the following steps. If you do not already have a Microsoft account, click "Create a new Microsoft Account" and follow the steps explained in the create a Microsoft account [section](#create-a-microsoft-account). 
3. Create a User ID (optional)
![Create a user ID](/images/user id.PNG)
4. Click to create a new library. Give your library a name, and open the newly created library.
5. Click the button that says 'Go to Jupyter'.
![New Jupyter Server](/images/new-notebook.PNG)
6. Click 'New' and then select 'Python 3'.
![New Python3 Notebook](/images/new-python3.PNG)

## 2. Importing the dataset and necessary libraries

  - In order to get the dataset, you can import from the Dropbox link below. This data is several weeks date, but the latitudes and longitudes for these restaurants have already been calculated. Click [here](https://notebooks.azure.com/faq#upload_data) to learn other ways to import data in to Azure Notebooks.
```
!curl -L https://www.dropbox.com/s/qsodvwpcyu3mxei/NYC%20Restaurants.csv?dl=1 -o NYC_Restaurants.csv
```

  - We will need to import several libraries in order to analyze this data. Run the following code in a new cell. We will import more later on.
```
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
%matplotlib inline
```
  ** %matplotlib inline will display the plots in the browser without opening a new page.

## 3. Understanding Pandas for Data Analysis

### Read NYC Restaurant CSV

#### Read the data from the CSV into a Pandas DataFrame

```
rests = pd.read_csv("NYC_Restaurants.csv")
```

#### Filter the data 

  - Only look at Manhattan Data. Filter on the BORO column in the dataset to only values that equal 'MANHATTAN'.
```
mRests = rests[rests['BORO']=="MANHATTAN"] 
```
You can manipulate this dataframe now by running code like `mRests['Boro]`, or see column values by running `list(mRests.columns.values)`.

  - Remove stores that have not been graded yet.
```
mRests = mRests[mRests['GRADE']!="Not Yet Graded"]
```

  - Remove stores that have no grade.
```
mRests = mRests[pd.notnull(mRests["GRADE"])]
```

  - Using this knowledge, you can remove all the stores that also have no score.

  - Redefine the score levels so that A is best, then B, then C, P, and Z. 

```
mRests["GRADE"] = mRests["GRADE"].astype("category",categories = ["A","B","C","P","Z"], ordered = True)
```

  - Reset the index with the now filtered dataframe.
```
mRests = mRests.reset_index(drop=True)
mRests.head()
```
## 4. Creating traditional statistical graphs

### Matplotlib

  - Create figure area with axes.
` f, ax = plt.subplots() ## creates figure area with axes`

  - Create a histogram of the data using numpy. 
```
data = mRests['SCORE']
plt.hist(data)
```
  - Create labels for the axes and a title.
```
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.title("Frequency of Restaurant Scores")
```

  - Display the plot
`plt.show()`

### Pandas

Create the same graph as above with less code. You can play around with the bin size to change the way the graph looks.
```
mRests["SCORE"].hist(bins=20)
plt.title("Frequency of Restaurant Score")
```

#### Create a Pie Chart
```
mRests["GRADE"].value_counts().plot(kind = "pie")
```
#### Create a Bar Chart to understand the Critical Flag

```
mRests["Critical Flag"].value_counts().plot(kind = "bar")
```

### Seaborn
  - Install seaborn ` ## pip install seaborn`
  - Import Seaborn `import seaborn as sns`
  - Select the plot style

To see what styles are available  `plt.style.available`
You can select the style by running either of the following lines:
```
sns.set(style="whitegrid", color_codes=True) ### Updates only the seaborn charts created after the fact
plt.style.use('seaborn-colorblind') ### updates for all graphs in the page created after the fact
```
  - Create a Strip Plot
```
sns.stripplot(x="GRADE", y = "SCORE", data = mRests)
```
  - This plot does not allow us to see the depth of the data and how many datapoints are actually included. To change this, we can use the parameter `jitter = True`.
  - Break the data down by the Critical Flag using the `hue` parameter.
  - Try creating a boxplot and barplot using these same parameters (excluding jitter).

## 5. Creating maps

### Convert Addresses to Lat/Long

In order to plot the points on the maps, we will need to convert the addresses to a geolocation. The addresses right now are very inconsistent with their labeling so we have to go through each address and normalize them. We won't go into this code too much but it convert numbers to words, and orginal words to numbers. Copy the following code
```
# !pip install -e git+https://github.com/pwdyson/inflect.py#egg=inflect
# !conda update anaconda --y
!pip install inflect

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
    for j in range(len(street)):
        if re.findall(r'([0-9]+(st|rd|th|nd)+)', street[j].lower())==[]:
            if(filter(str.isdigit, street[j])!=''):
                val=int(filter(str.isdigit, street[j]))
                street[j]=street[j].replace(str(val), str(p.ordinal(val)))    
        streetFull = ' '.join(street)
        mRests.set_value(i,'STREET',streetFull)

mRests["Address"]=mRests['BUILDING'].map(str)+ " " + mRests['STREET'].map(str)+ ", " + mRests['ZIPCODE'].map(str)
```

### Sample Data with the same seed
There are over 80,000 data points in mRests so we will take a sample of 100 of these points in order to plot them on a map more easily. We will set the seed to be the same every time so that we always get the same data and can compare our results.

```
# import random
np.random.seed(seed=10)
rows = np.random.choice(mRests.index.values, 100)
samp = mRests.ix[rows]
# samp = random.sample(mRests,90)
samp= samp.reset_index(drop=True)
samp
```
### Geocode Addresses
Now let's geocode the addresses. Due to API restrictions, I used an external [site](http://www.findlatitudeandlongitude.com/batch-geocode/#.WArN5-grIvg) to match the addresses to lat/long points. I have already coded these addresses so we can skip this step and just use the same addresses :).

```
!curl -L 'https://www.dropbox.com/s/p4145z5odvlypez/address.csv?dl=1' -o address.csv
adds = pd.read_csv("address.csv")
samp['lat']= adds['latitude']
samp['long']= adds['longitude']
```
### Basemap

  - Install basemap `!conda install basemap --yes`
  - Import the basemap tool `from mpl_toolkits.basemap import Basemap]`
  - In order to create a map with basemap, we have to have the upper and lower corner limits for the area we want to zoom in on. This was very difficult to calculate.
```
map = Basemap(projection='merc',
    resolution = 'h', area_thresh = .01,
    lat_0=40.7831, lon_0= -73.9712,
    llcrnrlon=-74.03, llcrnrlat=40.701,
    urcrnrlon=-73.86, urcrnrlat=40.901)
```
  - Add boundaries and lines to the map; fill the continents.
```
map.drawcoastlines()
map.drawcountries()
map.drawstates()
map.drawrivers()
map.fillcontinents(color = 'gainsboro')
map.drawmapboundary(fill_color='steelblue')
```
  - Plot the map `map.plot(samp['lat'][1],samp['long'][1],'bo', markersize = 24)`


### Folium

  - Install folium `!pip install folium`
  - Import folium `import folium`
  - Create the maps. With folium we still need to have the center points for NYC but we no longer need the upper and lower limits as we did with basemap.

```
mCluster = folium.Map(location=[40.7831, -73.9712], zoom_start =12)
marker_cluster = folium.MarkerCluster().add_to(mCluster)
for i in range(len(samp)):
    if samp["GRADE"][i] =="A":
        folium.Marker([samp['lat'][i],samp['long'][i]], popup= "Name: " + str(samp['DBA'][i])+ '\n' + "Score: " + str(samp["SCORE"][i]) + '\n'+'Grade: '+ str(samp["GRADE"][i]),
                      icon=folium.Icon(color="green", icon='no-sign')).add_to(marker_cluster)
    elif samp["GRADE"][i]=="B":
         folium.Marker([samp['lat'][i],samp['long'][i]], popup= "Name: " + str(samp['DBA'][i])+ '\n' + "Score: " + str(samp["SCORE"][i]) + '\n'+'Grade: '+ str(samp["GRADE"][i]),
                      icon=folium.Icon(color='blue',icon='no-sign')).add_to(marker_cluster)
    else:
         folium.Marker([samp['lat'][i],samp['long'][i]], popup= "Name: " + str(samp['DBA'][i])+ '\n' + "Score: " + str(samp["SCORE"][i]) + '\n'+'Grade: '+ str(samp["GRADE"][i]),
                      icon=folium.Icon(color='red',icon='no-sign')).add_to(marker_cluster)
```
  - Remove clustering to the map by commenting out the marker_cluster line. and change all of the `add_to(marker_cluster)` to `add_to(m)`.
  - You can save the html for this file `m.save('restaurants.html')` and import it into your websites.

## 6. Creating Interactive Graphs

### Bokeh
  - Import Bokeh server and open a BokehJS notebook 
```
from bokeh.io import output_notebook
output_notebook()
```
  - Import Bokeh charts
``` 
from bokeh.charts import Histogram, output_file, show
```
  - Create a histogram `p1=Histogram(samp['SCORE'])`.
  - Display the chart `show(p1)`
  - You can update parameters for the title, number of bins, and where the legend is.
```
p2 = Histogram(mRests,'SCORE', color='GRADE',
              title="Score Grouped by Grade", bins = 15,
              legend='top_right')
```
  - Create a tabbed image with multiple graphs. 
```

from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show
from bokeh.plotting import figure

tab1 = Panel(child=p1, title="Frequency of Score")
tab2 = Panel(child=p2, title="By Grade")

tabs = Tabs(tabs=[ tab1, tab2 ])
```
  - Save the html file `output_file("tabs.html")`

### Plotly

We will use the offline version of plotly so we will not need to create any accounts here or upload our graphs. 
  - Import plotly
```
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
init_notebook_mode(connected=True)
```
  - Create a histogram
```
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
```
  - Display the chart `iplot(fig1)`

While plotly is good for interactive graphs it's not good with local data.
```
samp['text'] = "Name: " + samp['DBA'].astype(str)+ '\n' + "Score: " + samp["SCORE"].astype(str) + '\n'+'Grade: '+ samp["GRADE"].astype(str)

scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]

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
```

## Create a Microsoft Account
If you do not already have a Microsoft account, when you go to login click "Create a New Microsoft Account".
1.  Enter an email and password that you would like to use for your new account. You may use an email that you already have and link the two. Otherwise click "Get a new email address" and follow the steps.
2. Click 'Next' 
![Microsoft account page](/images/microsoft account signup.PNG)
3. If you used an existing email, you will need to get the code sent to that email and enter it in.
    - If you used a new email you will have to enter a phone number and have a security code texted to you.
4. You will be asked to allow the app to have access to your account. Click 'Yes'.
![Microsoft App Access](/images/app access info.PNG)
