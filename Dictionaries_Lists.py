#1.	Return all the duplicate values from list of arraylist
#Input:  [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
#Output:
#1 -> 2
#8 -> 2
#0 -> 3, 4 -> 2

InputList = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
newList = []

for i in range(len(InputList)):
    for j in range(len(InputList[i])):
        newList.append(InputList[i][j])

print(newList)

z = list(set(newList))

for i in range (len(z)):
    repeating = 0
    for j in range(1 , len(newList)):
        if z[i] == newList[j]:
            repeating +=1
    print(str(z[i]) + " ---->>>  " + str(repeating))

#2.	Merge two lists as shown below
#Given I/P
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]
#outpuy - ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
output = []

for i in range(len(list1)):
    for j in range(len(list2)):
        output.append(list1[i] + " " + list2[j])

print(output)

#Given a nested list extend it by adding the sub list ["h", "i", "j"]
# in such a way that it will look like the following list
#list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#Sub List to be added = ["h", "i", "j"]
#output = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
SubListtobeadded = ["h", "i", "j"]

list1[2][1][2].extend(SubListtobeadded)
print(list1)


#Map the dictionary in the following manner
#Keys = [‘Ten’, ‘Twenty’, ‘Thirty’]
#Value = [10,20,30]
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

Keys = ["Ten", "Twenty", "Thirty"]
Value = [10,20,30]
output = {}

for i in range(len(Keys)):
    output[Keys[i]] = Value[i]

print(output)

#Merge following two Python dictionaries into one
#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#Expected output:
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

#Rename key city to location in the following dictionary
#sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
print(sampleDict)
sampleDict["RenamedCity"] = sampleDict.pop("city")
print(sampleDict)


#Convert Dictionary to list
#The original dictionary is : {‘HuEx: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}
#The converted list is : [[‘HuEx, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

orgDict = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
listt =[]

for key, value in orgDict.items():
    listt.append([[key] + value])

print("From for loop")
print(listt)

















