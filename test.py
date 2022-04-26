import os
import sys
import datetime
from tkinter import ttk
from tkinter import *
from tkinter import messagebox




root = Tk()


root["bg"] = "#fafafa"
root.title("tool key")
root.geometry("300x80")
root.resizable(width = True, height = True)


##variables used = j,o,i,k,r,r1,e,g,
##y,y1,u,u1,h,dt_str,dt,s,tt,w,x1,x2,b,a,count1,count2


j = -1  
o = -1  
i = -1  
k = -1


sp = []


#### if files not one directory.
#### a = batch_100.txt n = batch_200.txt

##for adress,dirs,files in os.walk("C:\\"):   
##    for b in files:
##        full_path = os.path.join(adress, b)
##        sp.append(full_path)
##        
##
##
##for x1 in sp:
##    if "batch_100.txt" in x1:
##        a = x1
##
##
##for x2 in sp:
##    if "batch_200.txt" in x2:
##        n = x2       


r = open("batch_100.txt")
y = r.read().splitlines()
r.close()


r = open("batch_100.txt")
y1 = r.readlines()
r.close()


e = open("batch_200.txt") 
u = e.read().splitlines()        
e.close()


e = open("batch_200.txt") 
u1 = e.readlines()       
e.close()


dt = datetime.now()
dt_str = dt.strftime("%d-%m-%Y  %H:%M:%S")
s = os.getenv("username")


r1 = open("used_key.txt", "w", encoding = "utf-8")
r1.close()

    
tt = "All keys in this file are used!!!"
count1 = True
count2 = True

def close_prog():
        root.destroy()
        
def okButton_click():
        global i,o,j,k,count1,count2
        
        if count1 == True and i == 13:
                count1 = False
                messagebox.showinfo(title = "ERROR", \
                                    message = tt)
        elif count2 == True and o == 36:
                count2 = False
                messagebox.showinfo(title = "ERROR", \
                                    message = tt)
        
        elif comboExample.get() == ("batch_100.txt"):
                i += 1
                g = y[i]
                w = g + " - " + s + " - " + dt_str + "\n"
                
                r1 = open("used_key.txt", "a",\
                          encoding = "utf-8")
                r1.writelines(w + "\n")
                r1.close()
                r1 = open("used_key.txt", "r", \
                          encoding = "utf-8")
                m = r1.read()
                r1.close()
                r1 = open("used_key.txt", "w", \
                          encoding = "utf-8")
                r1.writelines(m)
                r1.close()
                Output.delete(1.0, END)
                Output.insert(END, g)
                r = open("batch_100.txt", "w")
                j += 1
                y1[j] = ""
                r.writelines(y1)
                r.close()
                
                
        elif comboExample.get() == ("batch_200.txt"):
                o += 1
                h = u[o]
                w = h + " - " + s + " - " + dt_str + "\n"
                
                r1 = open("used_key.txt", "a",\
                          encoding = "utf-8")
                r1.writelines(w + "\n")
                r1.close()
                r1 = open("used_key.txt", "r", \
                          encoding = "utf-8")
                m = r1.read()
                r1.close()
                r1 = open("used_key.txt", "w", \
                          encoding = "utf-8")
                r1.writelines(m)
                r1.close()
                Output.delete(1.0, END)
                Output.insert(END, h)
                e = open("batch_200.txt", "w")
                k += 1
                u1[k] = ""
                e.writelines(u1)
                e.close()

               
        elif comboExample.get() == (""):
             messagebox.showinfo(title = "ERROR", \
                                 message = "please, select File!!!")


lb_1 = Label(root, text = " Key Batch: ", bg = "#fafafa")


closeButton = Button(root, text = "     Cancel     ", command = close_prog)


okButton = Button(root, text = "     Get key     ", \
                  command = okButton_click)


comboExample = ttk.Combobox(root, width = 30,   
                            values=[
                                    "batch_100.txt", 
                                    "batch_200.txt"])


Output = Text(root, bg = "white", width = 34, height = 1)


lb_1.place(x = 9, y = 0)
comboExample.place( x = 80, y = 0)
okButton.place(x = 80, y = 23)
closeButton.place(x = 162, y = 23)
Output.place(x = 9, y = 55)


root.mainloop()
