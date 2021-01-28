# coding:utf-8
# 找到年龄最大的人，并输出。

list1 = []
person = {"li":18,"wang":50,"zhang":20,"sun":22}

print(person)
print(person["li"])


m = 'li'
for key in person.keys():
    if person[m] < person[key]:
        m = key
print ("年龄最大的人:",end="")
print ('%s,%d' % (m,person[m]))

list1 = list(person.values())
print(list1)
for i in range(len(list1)):
   print(list1[i],end=' ')
