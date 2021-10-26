
import json
import pprint # pretty print
tweets = []

# files = ['trump_tweet_data_archive/condensed_2009.json', 'trump_tweet_data_archive/condensed_2010.json', 'trump_tweet_data_archive/condensed_2011.json', 'trump_tweet_data_archive/condensed_2012.json', 'trump_tweet_data_archive/condensed_2013.json', 'trump_tweet_data_archive/condensed_2014.json', 'trump_tweet_data_archive/condensed_2015.json', 'trump_tweet_data_archive/condensed_2016.json', 'trump_tweet_data_archive/condensed_2017.json', 'trump_tweet_data_archive/condensed_2018.json']
# files = ['dataset/prize.json']
# files2 = ['dataset/country.json']

physics = 0
economics = 0
literature = 0
medicine = 0
peace = 0
chemistry = 0
with open('dataset/prize.json', encoding='ascii') as f:
    text = f.read()
    tweets = json.loads(text)

for key in tweets:
    for t in tweets[key]: 
        if 'physics' in t["category"].lower():
            physics += 1 # this only counts one 'Trump' mention per tweet -- even in the ones he mentions himself twice
        if 'economics' in t["category"].lower():
            economics += 1
        if 'literature' in t["category"].lower():
            literature += 1
        if 'medicine' in t["category"].lower():
            medicine += 1
        if 'peace' in t["category"].lower():
            peace += 1
        if 'chemistry' in t["category"].lower():
            chemistry += 1

# print('len(tweets)= ', len(tweets))
print('physics:', physics)
print('economics:', economics)
print('literature:', literature)
print('medicine:', medicine)
print('peace:', peace)
print('chemistry:', chemistry)


# with open('dataset/country.json', encoding='ascii') as f:
#     text = f.read()
#     tweets = json.loads(text)


# x axis: year
# y axis: number of prizes
# comparing econ vs medicine vs physics

# these are the term counts calculated in the lab
# plot_dict = {'physics': 121, 'economics': 53, 'literature': 121, 'medicine': 121, 'peace': 121, 'chemistry': 121}

# terms = plot_dict.keys()
# counts = plot_dict.values()

# the order of results in .keys() and .values() is nondeterministic == "random"

# this code generates a plot
import numpy as np 
import matplotlib.pyplot as plt

X = ['2019','2020','2021']
APhysics = [1,1,1]
BEconomics = [1,1,1]

X_axis = np.arange(len(X))

# n=4
# r = np.arange(n)
# width = 0.25
    
# THE BELOW IS THE PLOT THAT WILL APPEAR
'''
plt.bar(X_axis - 0.2, APhysics, 0.4, label = 'Physics')
plt.bar(X_axis + 0.2, BEconomics, 0.4, label = 'Economics')

plt.xticks(X_axis, X)
plt.xlabel("Year")
plt.ylabel("Number of Prizes")
plt.title("Nobel Prizes: Physics vs. Economics")
plt.legend()
plt.show()
'''

# fig, ax = plt.subplots()
# ax.set(title = "Nobel Prize",
#        xlabel = "Category",
#        ylabel = "Number of Prizes")
# plt.xticks(r + width/2,['2019','2020','2021'])
# plt.legend()
# plt.show()
