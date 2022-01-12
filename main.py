try:
  import tkinter as tk
  from math import *
  import re
except: ImportError


class main:
  def __init__(self,master):
    self.master = master
    self.master.title('Calculator')

    #self.var = tk.BooleanVar(value=False)

#creation

    self.frm_0 = tk.Frame(self.master,width=200,height=50)
    self.frm_1 = tk.Frame(self.master,width=200,height=50)
    self.frm_2 = tk.Frame(self.master,width=200,height=50)
    self.frm_3 = tk.Frame(self.master,width=200,height=50)
    self.frm_4 = tk.Frame(self.master,width=200,height=50)
    self.frm_5 = tk.Frame(self.master,width=200,height=50)

    self.lbl_1 = tk.Label(self.frm_0,relief=tk.SUNKEN,width=20,bd=3,bg='light green',anchor='e')
    
    self.btn_0 = tk.Button(self.frm_5,text='0',relief=tk.RAISED,width=3,bd=3)
    self.btn_1 = tk.Button(self.frm_4,text='1',relief=tk.RAISED,width=3,bd=3)
    self.btn_2 = tk.Button(self.frm_4,text='2',relief=tk.RAISED,width=3,bd=3)
    self.btn_3 = tk.Button(self.frm_4,text='3',relief=tk.RAISED,width=3,bd=3)
    self.btn_4 = tk.Button(self.frm_3,text='4',relief=tk.RAISED,width=3,bd=3)
    self.btn_5 = tk.Button(self.frm_3,text='5',relief=tk.RAISED,width=3,bd=3)
    self.btn_6 = tk.Button(self.frm_3,text='6',relief=tk.RAISED,width=3,bd=3)
    self.btn_7 = tk.Button(self.frm_2,text='7',relief=tk.RAISED,width=3,bd=3)
    self.btn_8 = tk.Button(self.frm_2,text='8',relief=tk.RAISED,width=3,bd=3)
    self.btn_9 = tk.Button(self.frm_2,text='9',relief=tk.RAISED,width=3,bd=3)
    self.btn_dot = tk.Button(self.frm_5,text='.',relief=tk.RAISED,width=3,bd=3)
    self.btn_equall = tk.Button(self.frm_5,text='=',relief=tk.RAISED,width=3,bd=3)
    self.btn_add = tk.Button(self.frm_5,text='+',relief=tk.RAISED,width=3,bd=3)
    self.btn_minus = tk.Button(self.frm_4,text='-',relief=tk.RAISED,width=3,bd=3)
    self.btn_times = tk.Button(self.frm_3,text='\N{multiplication sign}',relief=tk.RAISED,width=3,bd=3)
    self.btn_divide = tk.Button(self.frm_2,text='/',relief=tk.RAISED,width=3,bd=3)
    self.btn_clear = tk.Button(self.frm_1,text='AC',relief=tk.RAISED,width=3,bd=3)
    self.btn_percent = tk.Button(self.frm_1,text='%',relief=tk.RAISED,width=3,bd=3)
    self.btn_sqrt = tk.Button(self.frm_1,text='√',relief=tk.RAISED,width=3,bd=3)
    self.btn_off = tk.Button(self.frm_1,text='Off',relief=tk.RAISED,width=3,bd=3)
    self.btn_back = tk.Button(self.frm_0,text='⌫',relief=tk.RAISED,width=1,bd=3)

#binding

    self.master.bind('<ButtonRelease-1>', lambda z: self.__dropError__())

    self.btn_0.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'0'))
    self.btn_1.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'1'))
    self.btn_2.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'2'))
    self.btn_3.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'3'))
    self.btn_4.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'4'))
    self.btn_5.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'5'))
    self.btn_6.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'6'))
    self.btn_7.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'7'))
    self.btn_8.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'8'))
    self.btn_9.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'9'))
    self.btn_dot.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'.'))

    self.btn_equall.bind('<Button-1>',lambda z: self.__evalError__())
    #self.btn_equall.bind('<Button-1>',lambda z: self.var.set(True), add="+")

    
    self.btn_add.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'+'))
    self.btn_minus.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'-'))
    self.btn_times.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'*'))
    self.btn_divide.bind('<Button-1>',lambda z: self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'/'))
    self.btn_clear.bind('<Button-1>',lambda z: self.lbl_1.configure(text=''))
    self.btn_percent.bind('<Button-1>',lambda z: self.__percentError__())
    self.btn_sqrt.bind('<Button-1>',lambda z: self.__sqrtError__())
    self.btn_off.bind('<Button-1>', lambda z:self.__onoff__(self.btn_off.cget('text')))
    self.btn_back.bind('<Button-1>', lambda z: self.lbl_1.configure(text=self.lbl_1.cget('text')[0:-1]))



#Gridding 

    self.frm_0.grid(row=0,column=0,sticky='news')
    self.frm_1.grid(row=1,column=0,sticky='news')
    self.frm_2.grid(row=2,column=0,sticky='news')
    self.frm_3.grid(row=3,column=0,sticky='news')
    self.frm_4.grid(row=4,column=0,sticky='news')
    self.frm_5.grid(row=5,column=0,sticky='news')

    self.lbl_1.grid(row=0,column=0,padx=15,pady=10)

    self.btn_0.grid(row=0,column=0,padx=(5,0),pady=(0,2))
    self.btn_1.grid(row=0,column=0,padx=(5,0),pady=(0,2))
    self.btn_2.grid(row=0,column=1,pady=(0,2))
    self.btn_3.grid(row=0,column=2,pady=(0,2))
    self.btn_4.grid(row=0,column=0,padx=(5,0),pady=(0,2))
    self.btn_5.grid(row=0,column=1,pady=(0,2))
    self.btn_6.grid(row=0,column=2,pady=(0,2))
    self.btn_7.grid(row=0,column=0,padx=(5,0),pady=(0,2))
    self.btn_8.grid(row=0,column=1,pady=(0,2))
    self.btn_9.grid(row=0,column=2,pady=(0,2))
    self.btn_dot.grid(row=0,column=1,pady=(0,2))
    self.btn_equall.grid(row=0,column=2,pady=(0,2))
    self.btn_add.grid(row=0,column=3,padx=(10,5),pady=(0,2))
    self.btn_minus.grid(row=0,column=3,padx=(10,5),pady=(0,2))
    self.btn_times.grid(row=0,column=3,padx=(10,5),pady=(0,2))
    self.btn_divide.grid(row=0,column=3,padx=(10,5),pady=(0,2))
    self.btn_off.grid(row=0,column=0,padx=(5,0),pady=(0,2))
    self.btn_sqrt.grid(row=0,column=1,pady=(0,2))
    self.btn_percent.grid(row=0,column=2,pady=(0,2))
    self.btn_clear.grid(row=0,column=3,padx=(10,5),pady=(0,2))
    self.btn_back.grid(row=0,column=1,padx=(0,5),pady=10)
    



# on/off

  def __onoff__(self,x):
    if x == 'Off':
      self.btn_0.configure(state='disabled')
      self.btn_1.configure(state='disabled')
      self.btn_2.configure(state='disabled')
      self.btn_3.configure(state='disabled')
      self.btn_4.configure(state='disabled')
      self.btn_5.configure(state='disabled')
      self.btn_6.configure(state='disabled')
      self.btn_7.configure(state='disabled')
      self.btn_8.configure(state='disabled')
      self.btn_9.configure(state='disabled')
      self.btn_dot.configure(state='disabled')
      self.btn_equall.configure(state='disabled')
      self.btn_add.configure(state='disabled')
      self.btn_minus.configure(state='disabled')
      self.btn_times.configure(state='disabled')
      self.btn_divide.configure(state='disabled')
      self.btn_clear.configure(state='disabled')
      self.btn_percent.configure(state='disabled')
      self.btn_sqrt.configure(state='disabled')
      
      

      self.lbl_1.configure(text='',bg='grey')
      self.btn_off.configure(text='On')

      
    elif x =='On':
      self.btn_0.configure(state='normal')
      self.btn_1.configure(state='normal')
      self.btn_2.configure(state='normal')
      self.btn_3.configure(state='normal')
      self.btn_4.configure(state='normal')
      self.btn_5.configure(state='normal')
      self.btn_6.configure(state='normal')
      self.btn_7.configure(state='normal')
      self.btn_8.configure(state='normal')
      self.btn_9.configure(state='normal')
      self.btn_dot.configure(state='normal')
      self.btn_equall.configure(state='normal')
      self.btn_add.configure(state='normal')
      self.btn_minus.configure(state='normal')
      self.btn_times.configure(state='normal')
      self.btn_divide.configure(state='normal')
      self.btn_clear.configure(state='normal')
      self.btn_percent.configure(state='normal')
      self.btn_sqrt.configure(state='normal')
      

      self.lbl_1.configure(bg='light green')
      self.btn_off.configure(text='Off')

#Debugging

  def __evalError__(self):
    try:
      self.lbl_1.configure(text=eval(re.sub(r"((?<=^)|(?<=[^\.\d]))0+(\d+)", r"\1\2", str(self.lbl_1.cget('text')))))

    except:
      self.lbl_1.configure(text='Error')

  def __sqrtError__(self):
    try:
      self.lbl_1.configure(text=str(sqrt(float(str(self.lbl_1.cget('text'))))))
    except:
      self.lbl_1.configure(text='Error')



  def __percentError__(self):
    try:
      self.lbl_1.configure(text=str(float(str(self.lbl_1.cget('text')))/100))
    except:
      self.lbl_1.configure(text='Error')

  def __dropError__(self):
    if 'Error' == self.lbl_1.cget('text'):
      self.lbl_1.configure(text='')

  def __clearEntry__(self):
    if self.var.get():
      self.lbl_1.configure(text='')
      self.var.set(False)
    




def app():
  root = tk.Tk()
  main(root)
  root.mainloop() 

app()