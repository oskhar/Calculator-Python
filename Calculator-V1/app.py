from tkinter import *
from math import *
import sys

def Rms7(a,b,n):
	hasil= (1/2)*n*(2*a+(n-1)*b)
	return hasil

def Rms6(a,b,n):
	hasil= a+(n-1)*b
	return hasil

def Rms5(a,Un):
	hasil = (1/2)*(a+Un)
	return hasil

def Rms4(a,b,Un):
	hasil=((a-b-Un)/b)*-1
	return hasil

def Rms3(a,b,Sn):
	n=0
	while True:
		n+=1
		hasil=n
		perbandingan=Rms7(a=a,b=b,n=n)
		if perbandingan==Sn:
			break
	return hasil

def Rms2(b,n,Un):
	hasil=(((n-1)*b)-Un)*-1
	return hasil

def Rms1(a,r,n):
	hasil = a*(r**n-1)
	return hasil

def Rms2(a,r,n):
	hasil = (a*(r**n-1))/r-1
	return hasil

def Mtr1(Transpos):
	l_Transpos=len(Transpos)
	for i in range(1):
		MatrixBox.delete(1.0,END)
	semi_hasil=[]
	semi_hasil.append("[")

	if l_Transpos==4:
		gg=[0,2,1,3]
		k=0
		for i in gg:
			k+=1
			semi_hasil.append(Transpos[i])
			if k==2:
				semi_hasil.append("]\n[")
	elif l_Transpos==9:
		gg=[0,3,6,1,4,7,2,5,8]
		k=0
		kk=0
		for i in gg:
			k+=1
			semi_hasil.append(Transpos[i])
			if k==3 and kk<2:
				k=0
				kk+=1
				semi_hasil.append("]\n[")

	semi_hasil.append("]")
	hasil=""
	for i in semi_hasil:
		hasil+=str(i)+" "
	return hasil

def Mtr2(Invers):
	# Invers=str(Invers)
	# Invers=list(Invers)
	l_Invers=len(Invers)
	for i in range(1):
		MatrixBox.delete(1.0,END)
	if l_Invers==4:
		semi_hasil1=int(Invers[0])*int(Invers[3])
		semi_hasil2=int(Invers[1])*int(Invers[2])
		hasil=semi_hasil1-semi_hasil2
	elif l_Invers==9:
		gg1=[4,5,3]
		gg2=[8,6,7]
		semi_hasil1=0
		for i in range(3):
			semi_hasil1+=int(Invers[i])*int(Invers[gg1[i]])*int(Invers[gg2[i]])
		gg1=[5,3,4]
		gg2=[7,8,6]
		semi_hasil2=0
		for i in range(3):
			semi_hasil2+=int(Invers[i])*int(Invers[gg1[i]])*int(Invers[gg2[i]])
		hasil=semi_hasil1-semi_hasil2
	for i in range(1):
	    MatrixBox.insert(END, 1/hasil)

	return ""

def Mtr3(Determinan):
	# Determinan=str(Determinan)
	# Determinan=list(Determinan)
	l_Determinan=len(Determinan)
	for i in range(1):
		MatrixBox.delete(1.0,END)
	if l_Determinan==4:
		semi_hasil1=int(Determinan[0])*int(Determinan[3])
		semi_hasil2=int(Determinan[1])*int(Determinan[2])
		hasil=semi_hasil1-semi_hasil2
	elif l_Determinan==9:
		gg1=[4,5,3]
		gg2=[8,6,7]
		semi_hasil1=0
		for i in range(3):
			semi_hasil1+=int(Determinan[i])*int(Determinan[gg1[i]])*int(Determinan[gg2[i]])
		gg1=[5,3,4]
		gg2=[7,8,6]
		semi_hasil2=0
		for i in range(3):
			semi_hasil2+=int(Determinan[i])*int(Determinan[gg1[i]])*int(Determinan[gg2[i]])
		hasil=semi_hasil1-semi_hasil2
	for i in range(1):
	    MatrixBox.insert(END, str(hasil))

	return ""

def Mtr4(Tambah1,Tambah2):
	# Tambah1=str(Tambah1).replace("[",'').replace("]",'')
	# Tambah2=str(Tambah2).replace("[",'').replace("]",'')
	# Tambah1=list(Tambah1)
	l_Tambah=len(Tambah1)
	semi_hasil=[]
	semi_hasil.append("[")
	for i in range(1):
		MatrixBox.delete(1.0,END)

	if l_Tambah==4:
		k=0
		for i in range(l_Tambah):
			k+=1
			semi_hasil.append(int(Tambah1[i])+int(Tambah2[i]))
			if k==2:
				semi_hasil.append("]\n[")

	elif l_Tambah==9:
		k=0
		kk=0
		for i in range(l_Tambah):
			k+=1
			semi_hasil.append(int(Tambah1[i])+int(Tambah2[i]))
			if k==3 and kk<2:
				k=0
				kk+=1
				semi_hasil.append("]\n[")

	semi_hasil.append("]")
	for i in semi_hasil:
		if i=="\n":
		    MatrixBox.insert(END, i)
		else:
			MatrixBox.insert(END, str(i)+" ")
	return ""
# [ 2 6 4 -2 ] 

def Mtr5(Kurang1,Kurang2):
	# Kurang1=str(Kurang1).replace("[",'').replace("]",'')
	# Kurang2=str(Kurang2).replace("[",'').replace("]",'')
	# Kurang1=list(Kurang1)
	l_Kurang=len(Kurang1)
	semi_hasil=[]
	semi_hasil.append("[")
	for i in range(1):
		MatrixBox.delete(1.0,END)

	if l_Kurang==4:
		k=0
		for i in range(l_Kurang):
			k+=1
			semi_hasil.append(int(Kurang1[i])-int(Kurang2[i]))
			if k==2:
				semi_hasil.append("]\n[")

	elif l_Kurang==9:
		k=0
		kk=0
		for i in range(l_Kurang):
			k+=1
			semi_hasil.append(int(Kurang1[i])-int(Kurang2[i]))
			if k==3 and kk<2:
				k=0
				kk+=1
				semi_hasil.append("]\n[")

	semi_hasil.append("]")
	for i in semi_hasil:
		if i=="\n":
		    MatrixBox.insert(END, i)
		else:
			MatrixBox.insert(END, str(i)+" ")
	return ""

def Mtr6(Kali1,Kali2):
	# Kali1=str(Kali1).replace("[",'').replace("]",'')
	# Kali2=str(Kali2).replace("[",'').replace("]",'')
	# Kali1=list(Kali1)
	# Kali2=list(Kali2)
	semi_hasil=[]
	semi_hasil.append("[")
	for i in range(1):
		MatrixBox.delete(1.0,END)
	if len(Kali1)==4:
		gg1=[0,2]
		gg2=[1,3]
		for k in range(2):
			hasil1=0
			hasil2=0
			for i in range(2):
				f=i+2
				if k==1:
					hasil1+=int(Kali1[f])*int(Kali2[gg1[i]])
					hasil2+=int(Kali1[f])*int(Kali2[gg2[i]])
				else:
					hasil1+=int(Kali1[i])*int(Kali2[gg1[i]])
					hasil2+=int(Kali1[i])*int(Kali2[gg2[i]])
			semi_hasil.append(hasil1)
			semi_hasil.append(hasil2)
			if k!=1:
				semi_hasil.append("]\n[")

	if len(Kali1)==2:
		gg1=[0,1]
		hasil=Kali1[0]*Kali2[0]+Kali1[1]*Kali2[1]
		semi_hasil.append(hasil)
		semi_hasil.append("]\n[")
		hasil=Kali1[0]*Kali2[2]+Kali1[1]*Kali2[3]
		semi_hasil.append(hasil)

	semi_hasil.append("]")
	for i in semi_hasil:
			MatrixBox.insert(END, str(i)+" ")
	return ""


def Mtr7(Only_Kali1,Only_Kali2):
	# Only_Kali1=str(Only_Kali1).replace("[",'').replace("]",'')
	# Only_Kali1=list(Only_Kali1)
	l_Only_Kali=len(Only_Kali1)
	semi_hasil=[]
	semi_hasil.append("[")
	for i in range(1):
		MatrixBox.delete(1.0,END)

	gg=0
	kk=0
	if l_Only_Kali==4:
		for i in Only_Kali1:
			gg+=1
			hasil=int(i)*int(Only_Kali2)
			semi_hasil.append(hasil)
			if gg==2:
				semi_hasil.append("]\n[")
	elif l_Only_Kali==9:
		for i in Only_Kali1:
			gg+=1
			hasil=int(i)*int(Only_Kali2)
			semi_hasil.append(hasil)
			if gg==3 and kk<2:
				kk+=1
				gg=0
				semi_hasil.append("]\n[")

	semi_hasil.append("]")
	for i in semi_hasil:
			MatrixBox.insert(END, str(i)+" ")
	return ""

# def Mtr8():

# def Mtr9():



def kbk(angka):
	angka=str(angka)
	list_angka=list(angka)
	pj=0
	zz=0
	len_angka=len(list_angka)
	if len_angka>6:
		list_angka1=[]
		for i in range(4):
			list_angka1.append(list_angka[i])
		zz=1
		len_angka=len(list_angka1)
	sisa_pembagian=0
	if len_angka>3:
		sisa_pembagian=len_angka%3
	angka_depan=0
	gg=0
	if sisa_pembagian>0:
		angka_depan=""
		for i in range(sisa_pembagian):
			angka_depan+=str(list_angka[i])
		angka_depan=int(angka_depan)
		gg=1
	else:
		angka_depan=angka
		gg=0
	i=0
	while True:
		i+=1
		prl=i*i*i
		if prl>int(angka_depan):
			break
		angka_yang_mendekati = prl
		a=i
	nilai_a=a
	sisa_hasil=int(angka_depan) - angka_yang_mendekati
	if gg==1:
		for i in range(sisa_pembagian):
			del list_angka[0]
	c=str(sisa_hasil)
	if sisa_hasil==0:
		c=""
	if gg==1:
		for i in list_angka:
			c+=str(i)
	elif gg!=1:
		c+="000"
		pj=1
	c=int(c)
	b=0
	if zz==1:
		c=""
		for i in range(sisa_pembagian):
			del list_angka1[0]
		for i in list_angka1:
			c+=str(i)
	if int(c)<300*((a)**2)*b + 30*a*(b)**2 + b**3:
		i=0
		while True:
			i+=1
			prl=i*i*i
			if prl>c:
				break
			angka_yang_mendekati = prl
			a=i
		sisa_hasil=int(c) - angka_yang_mendekati
		c=str(sisa_hasil)
		if sisa_hasil==0:
			c=""
		else:
			c+="000"
			pj=0
	c=int(c)
	index_perbandingan=0
	nilai_b=0
	if sisa_hasil!=0 or zz==1 or gg==1:
		b=0
		while True:
			b+=1
			hasil = 300*((a)**2)*b + 30*a*(b)**2 + b**3
			if hasil>c:
				break
			index_perbandingan=hasil
			nilai_b=b
		sisa=int(c)-int(index_perbandingan)
		if gg==1:
			hasil=str(nilai_a)+str(nilai_b)
			pj=0
		elif pj==1:
			hasil=str(nilai_a)+"."+str(nilai_b)
			pj=1
		else:
			hasil=str(nilai_a)+"."+str(nilai_b)
			pj=1
		if pj==1:
			hasil=str(nilai_a)+"."+str(nilai_b)
			pj=1
		if zz==1:
			pj=1
			c=""
			a=int(hasil)
			c=str(sisa)
			index_perbandingan=0
			for i in range(3):
				c+=list_angka[i+3]
		else:
			c=str(sisa)+"000"
		if sisa!=0 or zz==1:
			b=0
			while True:
				b+=1
				semi_hasil = 300*((a)**2)*b + 30*a*(b)**2 + b**3
				if semi_hasil>int(c):
					break
				index_perbandingan=semi_hasil
				nilai_b=b
			sisa=int(c)-int(index_perbandingan)
			if pj==1:
				hasil+=str(nilai_b)
			else:
				hasil+="."+str(nilai_b)

		return hasil
	else:
		return a


gg=1
root=Tk()
root.title("kalkulator")
root.geometry("680x320")
root.configure(bg='#00FFFF')
def retrieve_input():
	inputValue=textBox.get("1.0","end-1c")
	inputValue=str(inputValue)
	zzz=0
	b=""
	if "Mtr" in inputValue:
		zzz=1
		b=inputValue
	textBox.delete(1.0,END)
	if zzz!=1:
		for i in inputValue:
			if i=="x":
				b+="*"
			elif i=="^":
				b+="**"
			elif i=="~":
				b+="%"
			elif i=="%":
				b+="/100"
			elif i=="π":
				b+=" 3.141592654 "
			elif i=="÷":
				b+="/"
			else:
				b+=str(i)
	try:
		a=eval(b)
	except ZeroDivisionError:
		a="Infinity!!!"
	if zzz==1:
		MatrixBox.insert(END, a)
	else:
		textBox.insert(END, a)

def run(inputValue):
	inputValue=str(inputValue)
	zzz=0
	b=""
	if "Mtr" in inputValue:
		zzz=1
		b=inputValue
	textBox.delete(1.0,END)
	if zzz!=1:
		for i in inputValue:
			if i=="x":
				b+="*"
			elif i=="^":
				b+="**"
			elif i=="~":
				b+="%"
			elif i=="%":
				b+="/100"
			elif i=="π":
				b+=" 3.141592654 "
			elif i=="÷":
				b+="/"
			else:
				b+=str(i)
	try:
		a=eval(b)
	except ZeroDivisionError:
		a="Infinity!!!"
	if zzz==1:
		MatrixBox.insert(END, a)
	else:
		textBox.insert(END, a)

def delete():
    inputValue=textBox.get("1.0","end-1c")
    textBox.delete(1.0,END)
    ls=list(inputValue)
    ln=len(ls)
    del ls[ln-1]
    a=""
    for i in ls:
    	a+=str(i)
    textBox.insert(END, a)
	
def clear():
    textBox.delete(1.0,END)

def realtime():
	gg=1
	while True:
		Inpt=textBox.get("1.0","end-1c")
		Inpt=str(Inpt)
		if "\n" in Inpt:
			Inpt.replace('\n','')
			run(Inpt)
		# try:
		# 	Inpt=int(Inpt)
		# except:
		# 	try:
		# 		Inpt=float(Inpt)
		# 	except:
		# 		try:
		# 			Inpt=eval(Inpt)
		# 		except:
		# 		    textBox.delete(1.0,END)
		if gg==0:
			break
	sys.exit()

def tambah():
    textBox.insert(INSERT,"+")

def kurang():
    textBox.insert(INSERT,"-")

def kali():
    textBox.insert(INSERT,"x")

def bagi():
    textBox.insert(INSERT,"÷")

def kuadrat():
	textBox.insert(INSERT,"^2")

def akar_kuadrat():
	textBox.insert(INSERT,"sqrt()")
	pyautogui.hotkey("Left")

def akar_kubik():
	textBox.insert(INSERT,"kbk()")
	pyautogui.hotkey("Left")

def x0():
	textBox.insert(INSERT,"0")

def x1():
	textBox.insert(INSERT,"1")

def x2():
	textBox.insert(INSERT,"2")

def x3():
	textBox.insert(INSERT,"3")

def x4():
	textBox.insert(INSERT,"4")

def x5():
	textBox.insert(INSERT,"5")

def x6():
	textBox.insert(INSERT,"6")

def x7():
	textBox.insert(INSERT,"7")

def x8():
	textBox.insert(INSERT,"8")

def x9():
	textBox.insert(INSERT,"9")

def buka():
	textBox.insert(INSERT,"(")

def tutup():
	textBox.insert(INSERT,")")

def modulus():
	textBox.insert(INSERT,"~")

def division():
	textBox.insert(INSERT,"%")

def kubik():
	textBox.insert(INSERT,"^3")

def c1():
	textBox.insert(INSERT,"cos()")
	pyautogui.hotkey("Left")

def c2():
	textBox.insert(INSERT,"acos()")
	pyautogui.hotkey("Left")

def c3():
	textBox.insert(INSERT,"cosh()")
	pyautogui.hotkey("Left")

def s1():
	textBox.insert(INSERT,"sin()")
	pyautogui.hotkey("Left")

def s2():
	textBox.insert(INSERT,"asin()")
	pyautogui.hotkey("Left")

def s3():
	textBox.insert(INSERT,"sinh()")
	pyautogui.hotkey("Left")

def t1():
	textBox.insert(INSERT,"tan()")
	pyautogui.hotkey("Left")

def t2():
	textBox.insert(INSERT,"atan()")
	pyautogui.hotkey("Left")

def t3():
	textBox.insert(INSERT,"tanh()")
	pyautogui.hotkey("Left")

def l1():
	textBox.insert(INSERT,"log()")
	pyautogui.hotkey("Left")

def l2():
	textBox.insert(INSERT,"π")

def m1():
	textBox.insert(INSERT,"Mtr1([])")
	for i in range(2):
		pyautogui.hotkey("Left")

def m2():
	textBox.insert(INSERT,"Mtr2([])")
	for i in range(2):
		pyautogui.hotkey("Left")

def m3():
	textBox.insert(INSERT,"Mtr3([])")
	for i in range(2):
		pyautogui.hotkey("Left")

def m4():
	textBox.insert(INSERT,"Mtr4([],[])")
	for i in range(5):
		pyautogui.hotkey("Left")

def m5():
	textBox.insert(INSERT,"Mtr5([],[])")
	for i in range(5):
		pyautogui.hotkey("Left")

def m6():
	textBox.insert(INSERT,"Mtr6([],[])")
	for i in range(5):
		pyautogui.hotkey("Left")

def m7():
	textBox.insert(INSERT,"Mtr7([],a)")
	for i in range(4):
		pyautogui.hotkey("Left")

def m8():
	textBox.insert(INSERT,"Mtr8([],[])")
	for i in range(5):
		pyautogui.hotkey("Left")

def m9():
	textBox.insert(INSERT,"Mtr9([],[])")
	for i in range(5):
		pyautogui.hotkey("Left")

def rumus7():
	textBox.insert(INSERT,"Rms7(a=,b=,n=)")
	for i in range(7):
		pyautogui.hotkey("Left")

def rumus6():
	textBox.insert(INSERT,"Rms6(a=,b=,n=)")
	for i in range(7):
		pyautogui.hotkey("Left")

def rumus5():
	textBox.insert(INSERT,"Rms5(a=,Un=)")
	for i in range(5):
		pyautogui.hotkey("Left")

def rumus4():
	textBox.insert(INSERT,"Rms4(a=,b=,Un=)")
	for i in range(8):
		pyautogui.hotkey("Left")

def rumus3():
	textBox.insert(INSERT,"Rms3(a=,b=,Sn=)")
	for i in range(8):
		pyautogui.hotkey("Left")


def rumus2():
	textBox.insert(INSERT,"Rms2(b=,n=,Un=)")
	for i in range(8):
		pyautogui.hotkey("Left")



textBox=Text(root, height=2, width=65, bg="#001515", fg="#00FFFF", insertbackground='#00FFFF')
textBox.place(x=20,y=0)
MatrixBox=Text(root, height=4, width=13, bg="#001515", fg="#00FFFF", insertbackground='#00FFFF')
MatrixBox.place(x=568,y=-1)
textBox.focus_set()
# textBox.bind("<Tab>", lambda e: focus())
label=Label(root, text="Create\nby Oskhar", bg="#00FFFF", fg="#151515", font=('Helvetica', 10, 'bold'))
label.place(x=590,y=75)
buttonCommit=Button(root, bg='#1E90FF', bd=0, fg='#00FFFF', height=1, width=10, text="-->", command=lambda: retrieve_input())
buttonCommit.place(x=335,y=45)
# buttonCommit.pack()
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="+", command=lambda: tambah())
buttonCommit.place(x=335,y=73)
# buttonCommit.pack()
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="-", command=lambda: kurang())
buttonCommit.place(x=335,y=105)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="x", command=lambda: kali())
buttonCommit.place(x=335,y=135)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="÷", command=lambda: bagi())
buttonCommit.place(x=115,y=135)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="pangkat 2", command=lambda: kuadrat())
buttonCommit.place(x=115,y=255)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="1", command=lambda: x1())
buttonCommit.place(x=5,y=45)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="2", command=lambda: x2())
buttonCommit.place(x=115,y=45)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="3", command=lambda: x3())
buttonCommit.place(x=225,y=45)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="4", command=lambda: x4())
buttonCommit.place(x=5,y=75)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="5", command=lambda: x5())
buttonCommit.place(x=115,y=75)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="6", command=lambda: x6())
buttonCommit.place(x=225,y=75)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="7", command=lambda: x7())
buttonCommit.place(x=5,y=105)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="8", command=lambda: x8())
buttonCommit.place(x=115,y=105)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="9", command=lambda: x9())
buttonCommit.place(x=225,y=105)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="0", command=lambda: x0())
buttonCommit.place(x=5,y=135)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="2√", command=lambda: akar_kuadrat())
buttonCommit.place(x=115,y=285)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="(", command=lambda: buka())
buttonCommit.place(x=335,y=195)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text=")", command=lambda: tutup())
buttonCommit.place(x=335,y=165)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="3√", command=lambda: akar_kubik())
buttonCommit.place(x=225,y=285)
buttonCommit=Button(root, bg='#DC143C', bd=0, fg='#00FFFF', height=1, width=10, text="Delete", command=lambda: delete())
buttonCommit.place(x=335,y=255)
buttonCommit=Button(root, bg='#DC143C', bd=0, fg='#00FFFF', height=1, width=10, text="Clear", command=lambda: clear())
buttonCommit.place(x=335,y=285)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Modulus", command=lambda: modulus())
buttonCommit.place(x=5,y=285)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="%", command=lambda: division())
buttonCommit.place(x=225,y=135)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Pangkat 3", command=lambda: kubik())
buttonCommit.place(x=225,y=255)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="cos", command=lambda: c1())
buttonCommit.place(x=5,y=165)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="cosh", command=lambda: c3())
buttonCommit.place(x=5,y=195)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="acos", command=lambda: c2())
buttonCommit.place(x=5,y=225)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="sin", command=lambda: s1())
buttonCommit.place(x=115,y=165)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="sinh", command=lambda: s3())
buttonCommit.place(x=115,y=195)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="asin", command=lambda: s2())
buttonCommit.place(x=115,y=225)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="tan", command=lambda: t1())
buttonCommit.place(x=225,y=165)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="tanh", command=lambda: t3())
buttonCommit.place(x=225,y=195)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="atan", command=lambda: t2())
buttonCommit.place(x=225,y=225)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="log", command=lambda: l1())
buttonCommit.place(x=5,y=255)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="π", command=lambda: l2())
buttonCommit.place(x=335,y=225)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="2(pl+pt+lt)", command=lambda: rumus1())
buttonCommit.place(x=460,y=45)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="a from Un", command=lambda: rumus2())
buttonCommit.place(x=460,y=75)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="n from Sn", command=lambda: rumus3())
buttonCommit.place(x=460,y=105)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="n from Un", command=lambda: rumus4())
buttonCommit.place(x=460,y=135)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Suku Tengah", command=lambda: rumus5())
buttonCommit.place(x=460,y=165)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Suku ke n", command=lambda: rumus6())
buttonCommit.place(x=460,y=195)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Jumlah Suku", command=lambda: rumus7())
buttonCommit.place(x=460,y=225)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Mtrx + Mtrx", command=lambda: m4())
buttonCommit.place(x=570,y=195)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Mtrx - Mtrx", command=lambda: m5())
buttonCommit.place(x=570,y=225)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="D Matrix", command=lambda: m3())
buttonCommit.place(x=570,y=165)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="I Matrix", command=lambda: m2())
buttonCommit.place(x=570,y=135)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="T Matrix", command=lambda: m1())
buttonCommit.place(x=570,y=105)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Mtrx x Mtrx", command=lambda: m6())
buttonCommit.place(x=570,y=255)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Mtrx x a", command=lambda: m7())
buttonCommit.place(x=570,y=285)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Mtrx ÷ Mtrx", command=lambda: m8())
buttonCommit.place(x=460,y=255)
buttonCommit=Button(root, bg='#151515', bd=0, fg='#00FFFF', height=1, width=10, text="Mtrx=Mtrx=a", command=lambda: m9())
buttonCommit.place(x=460,y=285)

mainloop()
gg=0
sys.exit()
