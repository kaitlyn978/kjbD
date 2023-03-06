from tkinter import*
import random 
root=Tk()
root.title("Guess the Password")
root.geometry("500x500")
entry1=Entry(root)
guessp=Label(root)
generatedp=Label(root)

a3=[[['S','K','h','a','W','P','f','l'],["Money","Ricky","Queen","Lemon","Ruby"],['$','@','#','!']]]


def generatep():
     en=entry1.get()
     guessp["text"]="Guessed Password:"+en

def randomp():
    r1=random.randint(0,7)
    r2=random.randint(0,4)
    r3=random.randint(0,3)
    l1=a3[0][0][r1]
    l2=a3[0][1][r2]
    l3=a3[0][2][r3]
    generatedp["text"]=l1+""+l2+""+l3
m=Button(root,text="guessed password",command=generatep)    
j=Button(root,text="new password",command=randomp)
entry1.place(relx=0.5,rely=0.4,anchor=CENTER)
m.place(relx=0.5,rely=0.5,anchor=CENTER)
guessp.place(relx=0.5,rely=0.6,anchor=CENTER)
j.place(relx=0.5,rely=0.7,anchor=CENTER) 
generatedp.place(relx=0.5,rely=0.8,anchor=CENTER)  
root.mainloop()
    
    #B670C1
   #7DFAC2
   #EE93C0
   #4178E0
   #02BDD0
   #E9D856
   #42FB7C
   #F88BE0
   #F47990
   #A6A8F0
   #26692A
   #66DCFB
   #76A8EF
   #1ABF7F
   #3D93D5
   #C0EAD8
   #9C62B4
   #065ABE
   #09DAC5
   #53FAAB
   #17F8E1
   #48F17B
   #1FCA94
   #DEF057
   #000597
   #F66C88
    
    
       
     
     
     
 