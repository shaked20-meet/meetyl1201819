#list_1 = [1, 2, 3, 4]
#def make_list1 ():
	#global list_1
	#print(list_1[0], list_1[-1])
#make_list1()
##################################
#num1 = input("Enter 1 number")
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#def list_a():
	#global a
	#global num1
	#for i in (a):
		#b = [] 
		#if i < num1:
			#b.append (i)
	#print(b)
	
#list_a()
###################################
#a = [1, 45, 32, 3]
#b = [1, 2, 3, 4, 5, 45, 32,3]
#def  only_1():
 #	global a
 #	global b
# 	list3 = []
 #	for i in (a):
 #		if i in b:
 #			list3.append(i)
#	print(list3)
#only_1()
#################################
import tkinter as tk
from tkinter import simpledialog
answer = simpledialog.askstring("Input", "Enter a number", parent = tk.Tk())
	