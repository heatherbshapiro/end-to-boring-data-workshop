# An End to Boring Data with Python Visualizations Workshop

Put the days of trying to decipher meaning from boring spreadsheets behind you. Visualize data to give greater and immediate meaning to all those numbers with Python. We will explore the variety of options available for data visualization in Python using different libraries and understand which ones excel for what type of task. Create maps, statistical graphs and more detailed or interactive visualizations that can also be used on the web, ideal to take that blog post to a whole new level. This presentation tackles boring data by looking at python libraries available for mapping such as basemap and folium, statistical graphs from libraries such as matplotlib and seaborn, as well as libraries such as Bokeh and Plotly that can be used for making interactive graphs.

This workshop will walk through the steps of analyzing a NYC Restaurant Rating dataset and creating visualizations that can lead us to important realizations about the data.

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
1. Setting up Azure Notebooks
2. Importing dataset
3. Loading libraries
4. Understanding Pandas for data analysis
5. Basic Graphs
    - Matplotlib
    - Pandas
    - Seaborn
6. Mapping
    - Basemap
    - Folium
7. Interactive Graphs
    - Bokeh
    - Plot.ly


## 1. Setting up Azure Notebooks

To combat the problem of different operating systems and computer setups, we will be using [Azure Notebooks](https://notebooks.azure.com/) for our work environment. Azure Notebooks is a free service that provides Jupyter notebooks along with supporting libraries as a service. It means you can just login and use, no installation/setup is necessary.

1. Go to https://notebooks.azure.com/ and click [Sign in](https://notebooks.azure.com/account/signin) (or go directly to the sign in link).
2. If you already have a Microsoft account, please log in with that and skip the following steps. If you do not already have a Microsoft account, click "Create a new Microsoft Account" and follow the steps bulleted below. 
    - Enter an email and password that you would like to use for your new account. You may use an email that you already have and link the two. Otherwise click "Get a new email address" and follow the steps.
    - Click 'Next' 
    ![Microsoft account page](/images/microsoft-account-signup.PNG)
    - If you used an existing email, you will need to get the code sent to that email and enter it in.
    - If you used a new email you will have to enter a phone number and have a security code texted to you.
    - You will be asked to allow the app to have access to your account. Click 'Yes'.
    ![Microsoft App Access](/images/app-access-info.PNG)
3. Create a User ID (optional)
![Create a user ID](/images/user-id.PNG)