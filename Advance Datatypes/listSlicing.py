# li[Start:len:step]
#li[::]by default it take li[0:len:1]
li = [10,20,30,40,50]
print(li[::])#[10, 20, 30, 40, 50]
print(li[::2])# [10, 30, 50]
print(li[1::])# [20, 30, 40, 50]
print(li[:3:])# [10, 20, 30]
print(li[1:4:2]) # [20, 40]

