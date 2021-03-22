
#1
listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
print('Element at odd-index positions from list one \n', listOne[1:6:2])
print('Element at even-index positions from list two \n', listTwo[0:(len(listTwo)):2])
print('Printing Final third list \n', (listOne[1:6:2] + listTwo[0:(len(listTwo)):2]))
'''using list method, extend 
a = listOne[1:6:2]
b = listTwo[0:(len(listTwo)):2]
a.extend(b)
print(a)
'''
#2
list1 = [34, 54, 67, 89, 11, 43, 94]
list1.pop(4)
list1.insert(2, 11)
list1.insert(7, 11) #y is index -1 not working
print('Original list', list1)
print('List After removing element at index 4', list1)
print('List after Adding element at index 2', list1)
print('List after Adding element at last', list1)

#3
sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunk_1 = sampleList[0:(int(len(sampleList)/3))]
chunk_1.reverse()
chunk_2 = sampleList[3:6]
chunk_2.reverse()
chunk_3 = sampleList[6:len(sampleList)]
chunk_3.reverse()
print('Original list', sampleList)
print('Chunk  1', sampleList[0:(int(len(sampleList)/3))])
print('After reversing it', chunk_1)
print('Chunk  2', sampleList[3:6])
print('After reversing it', chunk_2)
print('Chunk  3', sampleList[6:len(sampleList)])
print('After reversing it', chunk_3)

#4
list_ = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict_ = {}
for x in list_:
    dict_.update({x: list_.count(x)})
print('Original list', list_)
print(dict_)

#5
list1 = [2, 3, 4, 5, 6, 7, 8]
list2 = [4, 9, 16, 25, 36, 49, 64]
#join_ = zip(list1, list2)
#print('join is', set(join_))
set1 = set(list1)
set2 = set(list2)
pair = {(a,b) for a, b in zip(set1, set2)}
print('First List', list1)
print('Second list', list2)
print('Result is ', pair)

#6
set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}
common = set1.intersection(set2)
print('First Set', set1)
print('Second Set', set2)
print('Intersection is',  common)
set1. difference_update(set2)
print('First Set after removing common element',  set1)

#7
firstSet = {57, 83, 29}
secondSet = {67, 73, 43, 48, 83, 57, 29}
print('First Set', firstSet)
print('Second Set', secondSet)
print('First set is subset of second set -', firstSet.issubset(secondSet))
print('Second set is subset of First set -', secondSet.issubset(firstSet))
print('First set is Super set of second set -', firstSet.issuperset(secondSet))
print('Second set is Super set of First set -', secondSet.issuperset(firstSet))
firstSet.clear()
print('First Set', firstSet)
print('Second Set', secondSet)

#8
rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
values = sampleDict.values()
wanted_elements = [i for i in rollNumber if i in values] #list comprehension
print('After removing unwanted elements from list', wanted_elements )
'''
list_ = []
for i in rollNumber:
    if i in values:
list_.append(i)
print('After removing unwanted elements from list', list_ ) using for and if
'''

#9
speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
list_ = list(dict.fromkeys(speed.values()))
print(list_)

#10
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
unique_list = list(dict.fromkeys((sampleList)))
mytuple = tuple(unique_list)
print('unique items', unique_list )
print('tuple', mytuple)
print('min:', min(mytuple))
print('max:', max(mytuple))

#11
class Vehicle:
    def __init__(self, make, model, year): #i tried to rename self
        self.make = make
        self.model = model
        self.year = year


v1 = Vehicle("Car", "Toyota", 2019)

print(v1.make)
print(v1.model)
print(v1. year)

#12
def jollof_rice():
    ingredients = ['tomato paste', 'onion', 'stock',
                    'seasoning', 'salt', 'oil', 'crayfish' ]
    print('add', ingredients[-2],'to a dry pot. Then put the',
           tuple(ingredients[0:4]), ', add', ingredients[-3], 'to taste and add',
          ingredients[-1], 'top up with adequate volume of water and'
            'allow to simmer'  )

    print('add already perboiled rice and cook')


jollof_rice()