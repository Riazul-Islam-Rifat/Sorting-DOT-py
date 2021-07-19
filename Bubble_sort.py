# Here an unsorted list will be given and we will sort it using bubble sort algorithm.
# We will create ascending order.
given_list =[3,2,1,6,5,4]

for items in range(0,len(given_list)-1):
    for item in range(0, len(given_list) - 1):
        if ( given_list[item]>given_list[item+1] ) :
            given_list[item],given_list[item+1]=given_list[item+1],given_list[item] # swap the values

print('The sorted list is -->',given_list)

