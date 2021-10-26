
import json
import pprint # pretty print
tweets = []

Germany = 0
# USA = 0
France = 0
Poland = 0
Switzerland = 0
Canada = 0

MartinLuther = 0

UnitedNations = 0
RedCross = 0
total2 = 0
RCUN = 0

with open('dataset/laureate.json', encoding='ascii') as f:
    text3 = f.read()
    tweets = json.loads(text3)

for key in tweets:
    for t in tweets[key]: 
        if 'bornCountry' in t.keys():
            if 'germany' in t["bornCountry"].lower():
                Germany += 1 # this only counts one 'Trump' mention per tweet -- even in the ones he mentions himself twice
            # if 'USA' in t["bornCountry"].lower():
            #   USA += 1
            if 'france' in t["bornCountry"].lower():
                France += 1
            if 'poland' in t["bornCountry"].lower():
                Poland += 1
            if 'switzerland' in t["bornCountry"].lower():
                Switzerland += 1
            if 'canada' in t["bornCountry"].lower():
                Canada += 1
        if 'firstname' in t.keys(): 
            if 'martin luther' in t["firstname"].lower():
                MartinLuther += 1
            if t["firstname"].lower():
                total2 += 1
            if 'united nations' in t["firstname"].lower():
                UnitedNations += 1
            if 'red cross' in t["firstname"].lower():
                RedCross += 1 
            if t["firstname"].lower() != 'red cross' in t["firstname"].lower() or 'united nations' in t["firstname"].lower():
                RCUN += 1
            

# x axis needs to be the same for both: country
# blue for people
# red for organizations
# y axis is number of awards

# print('len(tweets)= ', len(tweets))
print('Germany:', Germany)
# print('USA:', USA)
print('France:', France)
print('Poland:', Poland)
print('Switzerland:', Switzerland)
print('Canada:', Canada)
print('Martin Luther:', MartinLuther)
print('United Nations:', UnitedNations)
print('Red Cross:', RedCross)
print('total2:', total2)
print('RCUN:', RCUN)




# with open('dataset/country.json', encoding='ascii') as f:
#     text = f.read()
#     tweets = json.loads(text)



# these are the term counts calculated in the lab
plot_dict = {'Germany': 97, 'France': 57, 'Poland': 31, 'Canada': 21, 'UnitedNations': 4}

terms = plot_dict.keys()
counts = plot_dict.values()

# the order of results in .keys() and .values() is nondeterministic == "random"

# this code generates a plot!!!: 

import matplotlib.pyplot as plt
import numpy as np

y = np.array([968, 6])
mylabels = ["Individuals", "United Nations & Red Cross"]

mycolors = ["gold", "hotpink"]
myexplode = [0, 0.4]


plt.pie(y, labels = mylabels, explode = myexplode, shadow = True, colors = mycolors)
plt.legend(title = "Type of Winner:")
plt.title("Nobel Prizes: Individuals vs. Organizations")
plt.show() 

'''
x = np.array([1, 2, 3, 4])
y = x*2
  
# first plot with X and Y data
plt.plot(x, y)
  
x1 = [2, 4, 6, 8]
y1 = [3, 5, 7, 9]
  
# second plot with x1 and y1 data
plt.plot(x1, y1, '-.')
  
plt.xlabel("Winner")
plt.ylabel("Number of Prizes")
plt.title('Nobel Prizes')
plt.show()
'''

'''
fig, ax = plt.subplots()
ax.set(title = "Nobel Prizes",
       xlabel = "Winner",
       ylabel = "Number of Prizes")
ax.bar(terms, counts)
plt.show()
'''