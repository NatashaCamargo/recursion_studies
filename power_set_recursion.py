"""
Created on Sun Aug 22 13:30:29 2021

@author: Natasha Camargo
"""
def power_set(list):
    if len(list) == 0:
        return [[]]
    without_first = power_set(list[1:])
    with_first = [[list[0]] + rest for rest in without_first]
    return with_first + without_first


universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

#print(power_set_of_universities)

for set in power_set_of_universities:
  print(set)