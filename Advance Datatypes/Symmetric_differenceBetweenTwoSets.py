list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))
new_list = list1.symmetric_difference(list2)
list=sorted(new_list)
print("Symmetric difference of elements:", list)