#!/usr/bin/python
# coding:gbk

# ���ļ�
fo = open("C���Ծ������100��һ.txt", "r+")
print "�ļ���Ϊ: ", fo.name

str1 = fo.read()
# print "��ȡ���ַ���: %s" % (str1)

y_len = len(str1)
i = 0
start_str = "��"
end_str = "1.�������"

for i in range(0,y_len):
    char1 = str1[i,i+1]
    print char1
    
# �ر��ļ�
fo.close()
