
from collections import Counter
import collections
import urllib
from bs4 import BeautifulSoup
univ_set=collections.defaultdict(dict)
univ_artist_set=[]  #holds the set of all artist names
year_list = ["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"]
for year in year_list:
    wk="https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_"+year
    page=urllib.request.urlopen(wk)
    soup = BeautifulSoup(page, "lxml")
    mytabl = soup.find_all('table', class_='wikitable sortable')
    A=[]
    B=[]
    C=[]
    for row in mytabl:
        col=row.find_all('td');
        for col2 in col:
            A.append(col2.get_text())


    B = A[1::2]         #variable to hold the names of all the 100 artists
#    print(B)
    univ_artist_set.extend(B)
    C = A[0::2] #songs
    d=[]
    song_year={}
#    print(C)

    dict1 = dict(zip(C,B)) #combines the list of artists and songs into a dictionary for easier manipulation below
    c = Counter(B)  # enumerates the number of songs per artist 
    d=c.most_common(20) #finds the 20 most frequent artists featured on the  Hot 100 list for the year
    mykey={}
    mysinger=[]
    song_artist = {}
    song_count = {}
    thiscount=[]
    count_array={}
    for key,value in sorted(dict(d).items()):
        song_count.setdefault(key, []).append(value)
    for key,value in dict1.items():
        song_artist.setdefault(value, []).append(key)
        romano = song_artist[value]
        univ_set[value][year] = romano   #populating the songs under each artist into a dictionary
#    for key in B:
#        print(len(univ_set[key][year]), key)
#    print(song_artist)
#    print(mykey)
#    import yaml
#    print(yaml.dump(song_artist, default_flow_style=False))
#print(my_list1)
#    final = list(my_list1)
#    print(final)
    print("\n=========="+year+"===================\n")
print(len(set(univ_artist_set))) #finds the total number of unique artist names

myc= Counter(univ_artist_set)
myd=myc.most_common(20)   #finds the top 20 artists with most number of songs through the decade 
print(myd)

top_artists=collections.defaultdict(dict)

for key in dict(myd):
    print(key)
    print(univ_set[key])
    top_artists[key]=univ_set[key]
    print('\n')
print(top_artists) #prints a nested dictionary of artists with their songs released and grouoped by the year of release
