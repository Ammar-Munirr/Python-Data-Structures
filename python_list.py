# Basic Syntax for creating Python List is
list_p = [1,2,3,4]
# we can also set data type of a variable as list by:
lis_A = list()

#let's check data types of both variables:
print(type(list_p))
print(type(lis_A))
#output:                <class 'list'>      <class 'list'>

#by using python_list we can store any type of variables like:

temp_list = [1,'hello',True,{'name':'Ali'},(3,5)]
print(temp_list)


# list have many methods by default to manuplate the list elements let's implement them.

#insert    list.insert(ondex,value)


list_p.insert(1,234)
print(list_p)

#python list have also very popular method name pop(), which remove the last element when we don't pass the index to it, we can also assiged the removed element to a variable let's see:

removed_element = list_p.pop()

print(removed_element)
list_p.pop(0)
print(list_p)

# append() method in python list, it is used to add element in the last index of the list

list_p.append(32)
print(list_p)

#extend() method add iteratable elements to the list like adding a list items to a list:
add = ['Hello',1,6,2,'Go']
list_p.extend(add)
print(list_p)

#remove() method in a list is used to remove the first occurrence in a list like:

list_p.remove(2) # it will only remove first element that have value 2.
print(list_p)

#clear() method in a list is used to remove all the elements in a list:
temp_list = [12,4,2,5213,523,'Hello']
temp_list.clear()
print(temp_list)

#count() method will return how many times the passing value is occured:
print(list_p.count(1))

#sort() function will sort the list ASD Order and if you want it to DES order u have to pass reverse=True:

temp = [32,2,1,46,12,88,4,23]
temp.sort()
print(temp)
temp.sort(reverse=True)
print(temp)
#reverse() function will reverse the whole list:
list_p.reverse()
print(list_p)