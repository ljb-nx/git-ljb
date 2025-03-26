#!/usr/bin/python
# # coding:utf-8

# ���ļ�
try:
    fo = open("C���Ծ������100��.txt", "r+")
except IOError:
    print "ע�⣺û�д��ļ���"
print "�ļ���Ϊ: ", fo.name

str1 = fo.read()
# print "��ȡ���ַ���: %s" % (str1)

y_len = len(str1) #str1������
i = 0
start_str = "��"  #��ʼ��
end_str = "�������"  #��ֹ��

'''
print start_str,end_str

char1 = str1[i:i+2]
print char1
'''

#fo1 = open("python���Գ���.txt", "a+")

for i in range(0,y_len):
    char1 = str1[i:i+2]
    
    if (char1 == start_str):
        start_weizhi = str1.find(start_str,i)
        end_weizhi = str1.find(end_str,start_weizhi + 2)
        print str1[start_weizhi:end_weizhi - 2]
        #fo1.write(str1[start_weizhi:end_weizhi - 2] + "\n")
        
        continue

# �ر��ļ�
fo.close()
#fo1.close()

