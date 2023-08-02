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