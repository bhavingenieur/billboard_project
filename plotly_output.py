#Used Plot.Ly to plot the number of songs per artist among the top 10 most popular artists between 2007 - 2016 

@author: Bhavin Vadalia
"""

import plotly.plotly as py
import plotly.graph_objs as go

taylors = go.Scatter(
    y=[1,3,3,3,1,1,2,1,4,1],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=[
'"Teardrops on My Guitar"','"Our Song", "Teardrops on My Guitar", "Love Story"','"Love Story", "You Belong with Me", "White Horse"','"Mine", "You Belong with Me", "Today Was a Fairytale"',
'"Back to December"', '"We Are Never Ever Getting Back Together"','"I Knew You Were Trouble", "22"','"Shake It Off"', '"Blank Space", "Shake It Off", "Style", "Wildest Dreams"','"Wildest Dreams"'],
    mode='markers',name='Taylor Swift',
    marker=dict(
        size=[100,300,300,300,100,100,200,100,400,100],
        sizeref=2,
        sizemode='area',
    )
)

rihanna = go.Scatter(
    y=[1,3,1,2,3,3,2,0,1,1],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['"Shut Up and Drive"','"Take a Bow", "Disturbia", "Don\'t Stop the Music"','"Disturbia"','"Rude Boy", "Only Girl (In the World)"', '"S&M", "Only Girl (In the World)", "Cheers (Drink to That)"','"Where Have You Been", "You da One", "Diamonds"','"Diamonds", "Pour It Up"','','"Bitch Better Have My Money"','"Needed Me"'],
    mode='markers',name='Rihanna',
    marker=dict(
        size=[100,300,100,200,300,300,200,0,100,100],
        sizeref=2,
        sizemode='area',
    )
)
katyp = go.Scatter(
    y=[0,2,2,1,3,3,1,2,0,0],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['','"I Kissed a Girl", "Hot n Cold"','"Hot n Cold", "Waking Up in Vegas"','"Teenage Dream"','"Firework","Last Friday Night (T.G.I.F.)", "Teenage Dream"','"Wide Awake", "Part of Me", "The One That Got Away"','"Roar"','"Roar", "Birthday"','',''],
    mode='markers',name='Katy Perry',
    marker=dict(
        size=[0,200,200,100,300,300,100,200,0,0],
        sizeref=2,
        sizemode='area',
    )
)
 
beyon = go.Scatter(
    y=[1,0,5,1,1,0,0,1,1,1],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['"Irreplaceable"','','"Single Ladies (Put a Ring on It)", "Halo", "If I Were a Boy", "Sweet Dreams", "Diva"','"Sweet Dreams"','"Best Thing I Never Had"','','','"Partition"','"7/11"','"Sorry"'],
    mode='markers',name='Beyonce',
    marker=dict(
        size=[100,0,500,100,100,0,0,100,100,100],
        sizeref=2,
        sizemode='area',
    )
)
pinky = go.Scatter(
    y=[2,1,3,0,2,1,1,0,0,1],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['"U + Ur Hand", "Who Knew"','"So What"','"Sober", "So What", "Please Don\'t Leave Me"','','"Raise Your Glass", "Fuckin\' Perfect"','"Blow Me (One Last Kiss)"','"Try"','','','"Just Like Fire"'],
    mode='markers',name='Pink',
    marker=dict(
        size=[200,100,300,0,200,100,100,0,0 ,100],
        sizeref=2,
        sizemode='area',
    )
)
maron5 = go.Scatter(
    y=[1,0,0,1,0,1,3,1,2,0],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['"Makes Me Wonder"','','','"Misery"','','"One More Night"','"Daylight", "One More Night", "Love Somebody"','"Maps"','"Sugar", "Animals"',''],
    mode='markers',name='Marron 5',
    marker=dict(
        size=[100,0,0,100,0,100,300,100,200,0],
        sizeref=2,
        sizemode='area',
    )
)
lgaga = go.Scatter(
    y=[0,0,3,3,3,0,1,0,0,0],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['','','"Poker Face", "LoveGame", "Paparazzi"','"Bad Romance", "Alejandro", "Paparazzi"','"Born This Way", "The Edge of Glory", "Yoü and I"','','"Applause"','','',''],
    mode='markers',name='Lady Gaga',
    marker=dict(
        size=[0,0,300,300,300,0,100,0,0,0],
        sizeref=2,
        sizemode='area',
    )
)
drak = go.Scatter(
    y=[0,0,1,2,1,0,1,1,2,2],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['','','"Best I Ever Had"','"Find Your Love", "Over"','"Headlines"','','"Started from the Bottom"','"0 to 100 / The Catch Up"','"Hotline Bling", "Back to Back"','"Hotline Bling", "Controlla"'],
    mode='markers',
    name='Drake',
    marker=dict(
        size=[0,0,100,200,100,0,100,100,200,200],
        sizeref=2,
        sizemode='area',
    )
)
adele = go.Scatter(
    y=[0,0,0,0,2,4,0,0,1,3],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['','','','','"Rolling in the Deep", "Someone Like You"','"Set Fire to the Rain", "Someone like You", "Rumour Has It", "Rolling in the Deep"','','','"Hello"','"Hello", "Send My Love (To Your New Lover)", "When We Were Young"'],
    mode='markers',name='Adele',
    marker=dict(
        size=[0,0,0,0,200,400,0,0,100,300],
        sizeref=2,
        sizemode='area',
    ))
miley = go.Scatter(
    y=[0,2,2,1,0,0,2,2,0,0],
    x=["2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016"],
    text=['','"See You Again", "7 Things"','"The Climb", "Party in the U.S.A."','"Party in the U.S.A."','','','"We Can\'t Stop", "Wrecking Ball"','"Wrecking Ball", "Adore You"','',''],
    mode='markers',name='Miley Cyrus',
    marker=dict(
        size=[0,200,200,100,0,0,200,200,0,0],
        sizeref=2,
        sizemode='area',
    )
)

data=[taylors,rihanna,katyp,beyon,pinky,maron5,lgaga,drak,adele,miley]
py.plot(data, filename = 'basic-scatter-songs2')

