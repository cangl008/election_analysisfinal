print('Hello World')

type(3)
#declaring a list
counties=["Arapahoe","Denver","Jefferson"]
print(counties)
#the number unless otherwise told refers to the index in teh below ex 0 refers to arapahoe
print(counties[0])
#out put of about is Arapahoe

#len() is used to get the total number of items in a list
print(len(counties))
#out put is 3

#slicing list is used to get specific items from a list ex: list[start:end]
#list[start:end] returnd a list containing a copy of the iitems from the list from teh starting index up to but not including the ending index value
print(counties[0:2])
#output is [arapahoe, denver]

#also could use counties[:2] teh beginning is ommited so it will return same output as ^
# or counties[1:] output would be denver and jefferson

#items can be added to a list using append() function list.append()
counties.append('El Paso')
print(counties)

# to add a new item to a specific place use list.insert(index,obj)
#index is where we want it placed
#obj is the item
counties.insert(2,'El Paso')
print(counties)

#to remove an item use .remove which will remove the first occurence of the value
counties.remove('El Paso')
print(counties)

#pop() will remove an item from a soecific index(place) in the list
counties.pop(3)
print(counties)

#to replace an item in the list counties[2]='El Paso' which would replace the 2 index in the list (jefferson) with el paso

#tuples are similar to list BUT they CANNOT be changed once created ( items cannot be added or removed)
#but other than that they work similar to lists counties_tuple-=("Arapahoe","Denver","Jefferson")
#len(counties_tuple) the out put would be 3

#dictionary is an object that store a collection of data. it has a key, value or key-value pairs
#dictionaries use {} teh syntax is {key:value}
# 2 rules 1. values in dictionary can be obj of any type: int, float, str, boolean values, datetime values and list
#2. keys must be immutable objects like int, floating-point decimals, or strings. Keys cannot be lists or any other type of mutable object.
counties_dict={"Arapahoe":369237,"Denver":413229,"Jefferson":432438}

#to get all teh keys and values printed to the screen you can use the .items() method
#counties_dict.items()
# this would be the out put dict_items([('Arapahoe', 422829), ('Denver', 463353), ('Jefferson', 432438)])

#to only get the keys use .keys() method
#counties_dict.keys()
# this would be the output dict_keys(['Arapahoe', 'Denver', 'Jefferson'])

#counties_dict.values() would only give the values
# out put--dict_values([422829, 463353, 432438])

#to get a specific value use .get()
# counties_dict.get('Denver')
#output 463353
# or you can ounties_dict['Arapahoe'] would also ogive you the value attached to this key

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#to get key vaule pairs 
#for key, value in dictionary_name.items():
#    print(key, value)

# the first variable declared in teh for loop is assigned to the keys
#teh second variable is assigned to teh values
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
#nest loop to get the values
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)