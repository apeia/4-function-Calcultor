try:
  import tkinter as tk
  from tkinter import ttk
  from math import *
  import re
except: ImportError


class main:
  def __init__(self,master):
    self.master = master
    self.master.title('Calculator')

  #vars  

    self.var = tk.BooleanVar(value=False)

  #styles
    self.frm_style = ttk.Style()
    self.frm_style.configure('TFrame',master=self.master,width=200,height=50)

    self.btn_style = ttk.Style()
    self.btn_style.configure('TButton',relief=tk.RAISED,width=5,borderwidth=3,focuscolor='white')

#creation

    
    self.frm_1 = tk.Frame()
    self.frm_2 = tk.Frame()
    self.frm_3 = tk.Frame()
    self.frm_4 = tk.Frame()
    self.frm_5 = tk.Frame()
    self.frm_6 = tk.Frame()
    self.frm_7 = tk.Frame()
    self.frm_8 = tk.Frame()

    self.lbl_1 = tk.Label(self.frm_1,relief=tk.SUNKEN,width=20,bd=3,bg='light green',anchor='e')
    
    self.btn_0 = ttk.Button(self.frm_8,text='0')
    self.btn_1 = ttk.Button(self.frm_7,text='1')
    self.btn_2 = ttk.Button(self.frm_7,text='2')
    self.btn_3 = ttk.Button(self.frm_7,text='3')
    self.btn_4 = ttk.Button(self.frm_6,text='4')
    self.btn_5 = ttk.Button(self.frm_6,text='5')
    self.btn_6 = ttk.Button(self.frm_6,text='6')
    self.btn_7 = ttk.Button(self.frm_5,text='7')
    self.btn_8 = ttk.Button(self.frm_5,text='8')
    self.btn_9 = ttk.Button(self.frm_5,text='9')
    self.btn_dot = ttk.Button(self.frm_8,text='.')
    self.btn_equall = ttk.Button(self.frm_8,text='=')
    self.btn_add = ttk.Button(self.frm_8,text='+')
    self.btn_minus = ttk.Button(self.frm_7,text='-')
    self.btn_times = ttk.Button(self.frm_6,text='\N{multiplication sign}')
    self.btn_divide = ttk.Button(self.frm_5,text='/')
    self.btn_clear = ttk.Button(self.frm_2,text='AC')
    self.btn_percent = ttk.Button(self.frm_2,text='%')
    self.btn_sqrt = ttk.Button(self.frm_2,text='√')
    self.btn_off = ttk.Button(self.frm_2,text='Off')
    self.btn_back = ttk.Button(self.frm_1,text='⌫',width=3)
    #self.btn_ans = ttk.Button(self.frm_4,text='Ans')
    self.btn_lparent = ttk.Button(self.frm_3,text='(')
    self.btn_rparent = ttk.Button(self.frm_3,text=')')
    #self.btn_2nd = ttk.Button(self.frm_3,text='2nd')
    #self.btn_deg = ttk.Button(self.frm_3,text='Deg')
    self.btn_sin = ttk.Button(self.frm_4,text='sin')
    self.btn_cos = ttk.Button(self.frm_4,text='cos')
    self.btn_tan = ttk.Button(self.frm_4,text='tan')

    

#binding


    self.btn_0.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'0')])
    self.btn_1.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'1')])
    self.btn_2.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'2')])
    self.btn_3.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'3')])
    self.btn_4.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'4')])
    self.btn_5.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'5')])
    self.btn_6.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'6')])
    self.btn_7.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'7')])
    self.btn_8.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'8')])
    self.btn_9.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'9')])
    self.btn_dot.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'.')])
    self.btn_equall.bind('<Button-1>',lambda z:[ self.__evalError__(),self.var.set(True)])



    self.btn_add.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'+')])
    self.btn_minus.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'-')])
    self.btn_times.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'*')])
    self.btn_divide.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'/')])
    self.btn_clear.bind('<Button-1>',lambda z: self.lbl_1.configure(text=''))
    self.btn_percent.bind('<Button-1>',lambda z:[self.__dropError__(), self.__percentError__()])
    self.btn_sqrt.bind('<Button-1>',lambda z: [self.__dropError__(),self.__sqrtError__()])
    self.btn_off.bind('<Button-1>', lambda z:self.__onoff__(self.btn_off.cget('text')))
    self.btn_back.bind('<Button-1>', lambda z: [self.__clearEntry__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))[0:-1])])
    self.btn_lparent.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'(')])
    self.btn_rparent.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+')')])
    self.btn_sin.bind('<Button-1>',lambda z: [self.__dropError__(),self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'sin(')])
    self.btn_cos.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'cos(')])
    self.btn_tan.bind('<Button-1>',lambda z:[self.__dropError__(), self.lbl_1.configure(text=str(self.lbl_1.cget('text'))+'tan(')])

    #self.btn_sqrt.bind('<FocusOut>',lambda z: self.__dropError__(),add='+')

    self.btn_back.bind('<FocusOut>', lambda z: self.var.set(False),add='+')


#Gridding 

    self.frm_1.grid(row=0,column=0,sticky='news')
    self.frm_2.grid(row=1,column=0,sticky='news')
    self.frm_3.grid(row=2,column=0,sticky='news')
    self.frm_4.grid(row=3,column=0,sticky='news')
    self.frm_5.grid(row=4,column=0,sticky='news')
    self.frm_6.grid(row=5,column=0,sticky='news')
    self.frm_7.grid(row=6,column=0,sticky='news')
    self.frm_8.grid(row=7,column=0,sticky='news')

    self.lbl_1.grid(row=0,column=0,padx=(15,7),pady=10)

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
    self.btn_back.grid(row=0,column=1,padx=(3,5),pady=10)
    #self.btn_ans.grid(row=0,column=3,padx=(10,5),pady=(0,2))
    #self.btn_2nd.grid(row=0,column=0,padx=(5,0),pady=(0,2))
    self.btn_lparent.grid(row=0,column=1,pady=(0,2))
    self.btn_rparent.grid(row=0,column=2,pady=(0,2))
    #self.btn_deg.grid(row=0,column=3,padx=(10,5),pady=(0,2))
    self.btn_sin.grid(row=0,column=0,padx=(5,0),pady=(0,2))
    self.btn_cos.grid(row=0,column=1,pady=(0,2))
    self.btn_tan.grid(row=0,column=2,pady=(0,2))


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
    e = 'Error: Syntax'
    try:
      x = re.sub(r"((?<=^)|(?<=[^\.\d]))0+(\d+)", r"\1\2", str(self.lbl_1.cget('text')))
      if eval(x) < 10**-99 or eval(x) > 10**99:
        e = 'Error: Overflow'
        raise Exception
      else:
        e = 'Error: Syntax'
      self.lbl_1.configure(text=(eval(x)))

    except:
      
      self.lbl_1.configure(text=e)

  def __sqrtError__(self):
    try:
      self.lbl_1.configure(text=str(sqrt(float(str(self.lbl_1.cget('text'))))))
    except:
      self.lbl_1.configure(text='Error: Syntax')
      self.var.set(True)



  def __percentError__(self):
    try:
      self.lbl_1.configure(text=str(float(str(self.lbl_1.cget('text')))/100))
    except:
      self.lbl_1.configure(text='Error: Syntax')
      self.var.set(True)

  def __dropError__(self):
    print('r')
    if 'Error' in str(self.lbl_1.cget('text')):
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