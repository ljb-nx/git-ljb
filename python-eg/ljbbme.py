#!/usr/bin/python
# coding:cp936 

height=float(input("������ߣ�")) #�������
weight=float(input("�������أ�")) #��������
bmi=weight/(height*height)       #����BMIָ��

#�ж�����Ƿ����
if bmi<18.5:
    #���� 2 ��ͬ���� if ��֧����а����Ĵ��룬�������ͬһ������
    print("BMIָ��Ϊ��"+str(bmi)) #���BMIָ��
    print("���ع���")
if bmi>=18.5 and bmi<24.9:
    print("BMIָ��Ϊ��"+str(bmi)) #���BMIָ��
    print("������Χ��ע�Ᵽ��")
if bmi>=24.9 and bmi<29.9:
    print("BMIָ��Ϊ��"+str(bmi)) #���BMIָ��
    print("���ع���")
if bmi>=29.9:
    print("BMIָ��Ϊ��"+str(bmi)) #���BMIָ��
    print("����")
