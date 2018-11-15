astring = 'Hello'
another_string = ", World!"
print(astring+another_string)

print(another_string[2:-1]) #2 is slicing, only taking the sentence starting from position 2, after the double dot, its -1 taking from the last letter

t = (1, 'one', 'un')
a,b,c = t #assigning different variables to a tuple
print(a)

                            
t= [1, 'one', 'un'] #this is a list, a more powerful tuple
t.append('uno') #you can modify the list later, making it better than tuple
print(t)
t.insert(1,'0') #inserting 0 at position 1
print(t)
#print(len(a)), length function

t[2:]=['food', 'beer'] #sliced the original list, replacing all elements starting at position 2
print(t)

a=[1,2,3,4,5]
b=a[:-2] #after he double dot to slice from the end
print(b)

b=a[1::-1]
print(b)
