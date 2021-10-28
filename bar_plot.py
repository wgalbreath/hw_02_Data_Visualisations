
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


X = []
for i in range(2001,2022,10):
    yr = X.append(i)

# Y_axis = []
# PhysValue = 0
# EconValue = 0
# for w in tweets:
#     if tweets['prizes'][0]['category'] == 'physics':
#         PhysValue += 1
# for w in tweets:
#     if tweets['prizes'][0]['category'] == 'economics':
#         EconValue += 1

X_axis = np.arange(len(X))
Y_axis = [0,1]
n=4
r = np.arange(n)
width = 10

nobel_physics = {}
for i in tweets:
    for j in range(2001,2022):
        if tweets["prizes"][0]['category'] != 'physics':
            nobel_physics[j] = 1
        else:
            nobel_physics[j] = 0
print(nobel_physics)

nobel_econ = {}
for i in tweets:
    for j in range(2001,2022):
        if tweets['prizes'][0]['category'] != 'economics':
            nobel_econ[j] = 1
        else:
            nobel_econ[j] = 0
print(nobel_econ)

# THE BELOW IS THE PLOT THAT WILL APPEAR

# plt.bar(X_axis, nobel_physics, label = 'Physics')
# plt.bar(X_axis, nobel_econ, label = 'Economics')


# plt.bar(Y_axis, nobel_physics, label = 'Physics')
# plt.bar(Y_axis, nobel_econ, label = 'Economics')

# width = .3
# x = np.arange(len(nobel_physics.keys()))

fig, ax = plt.subplots()
rects1 = ax.bar([year-0.2 for year in nobel_econ.keys()], nobel_econ.values(), width=0.3, label='Economics',color='red')
rects2 = ax.bar([year+0.1 for year in nobel_physics.keys()], nobel_physics.values(), width=0.3, label='Physics',color='blue')

#Labels/Title
plt.xticks(X)
plt.xlabel("Year")
plt.yticks(Y_axis)
plt.ylabel("Number of Prizes")
plt.title("Nobel Prizes: Physics vs. Economics")
plt.legend()
#plt.tick_params(axis='x', which='major', labelsize=6)
plt.show()
