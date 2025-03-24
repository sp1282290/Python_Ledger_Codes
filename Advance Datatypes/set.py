s1 = {10,20,20,True, 'code'}
print(s1,type(s1))

s1.add(500)
print(s1) #(True,10,20,'code)
s1.remove(500)
print(s1)#{True, 10, 20, 'code'}

st1 = {1,2,3}
st2={3,4,5}
newset = st1.union(st2)
print(newset)#{1,2,3,4,5}
'''
1. In set we can store Homogeneous as well hetrogeneous type of Data.
2. Set is an unorderd collection of data because set generates the output in random order. It does not maintain order of intersection in output.
3. Set cannnot stores duplicate values.
4.Set is mutable means once we declare set , we can modify it.
'''