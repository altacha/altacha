list=['banana','apple','orange']
count=[3,4,5]
price=[0.6,0.2,0.7]

for (Fruit,Counter,Price) in zip(list,count,price):
    print('I bought '+str(Counter)+ " " + Fruit + "s for " + str(Price) +"$")