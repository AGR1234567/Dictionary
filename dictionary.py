planet = ['mercury', 4879, 3.7, False]
print(planet)
print(planet[0])

dict1 = {'name':'Aurin', 'age':11, 'year':2024, 'city':'Durgapur'}
print(dict1)
print(dict1['age'])
print(dict1.get('class','Unknown'))
dict1['class'] = '7V'
print(dict1)
print(len(dict1))
print(dict1.keys())
print(dict1.values())
print('city' in  dict1)
print('surname' in dict1)
del dict1['year']
print(dict1)
dict1['city'] = 'London'
print(dict1)
for i in dict1.keys():
    print(i, dict1[i])
student = []
for x in dict1:
    student.append(x)
print(student)
student.sort()
print(student)