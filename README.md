# billboard_project
Scraping Wikipedia using Python's BeautifulSoup to get the names of the most popular artists on BillBoard between the years 2007 - 2016

The aim of this project is to determine which are top 10 most popular artists whose songs featured in the annual Billboard Hot 100 list between 2007 - 2016and also the number of songs for each of them 

Tools used:

1. Python3
2. BeautifulSoup4 (for scraping)

Data Source:

Wikipedia Pages for Billboard Hot 100 Songs list for 2007 - 2016

We have only taken solo entries and ignored collaborations as they are quite infrequent in a given year

We used Plot.Ly to draw a ScatterPlot of the top 10 artists. It is viewable here:
https://plot.ly/~vbhavin/50.embed

In case you are curious, here they are(Top 20):

[('Taylor Swift', 20), ('Rihanna', 17), ('Katy Perry', 14), ('Beyoncé', 11), ('Pink', 11), ('Maroon 5', 10), ('Britney Spears', 10), ('Lady Gaga', 10), ('Drake', 10), ('Adele', 10), ('Miley Cyrus', 9), ('Kelly Clarkson', 8), ('The Black Eyed Peas', 8), ('Jason Derulo', 8), ('Bruno Mars', 8), ('Ne-Yo', 7), ('Chris Brown', 7), ('OneRepublic', 7), ('Luke Bryan', 7), ('Justin Timberlake', 6)]
