from tkinter import *

##  App ENC  ##
def ENC():
  
  enc = Tk()
  enc.geometry('550x550')
  enc.title('ENCRYPCHEN')
  enc.config(background='#2d8f10')
  enc.iconbitmap("image/logo2.ico")
  title = Label(enc, text='APP ENCCRYPTO', font=('Courier',15), bg='black',fg='white')
  title.pack(fill=X)

  def Del():
    En1.delete('0',END)
    Ent1.delete('0',END)
    anssert.delete('0',END)

  def ok(enent=None):
    pas = En1.get()
    pao = Ent1.get()
    if pas:
        message = pas
        mode = pao.upper()
        key = 108
        LETTERS = 'QAZWSXEDCRFVTGBYHNUJMIKIKOLP3786492501adbcefghjklmnopqrstuvwxyz:ضصثقفغ╗عهخحجدطكمنتالبيسشئءؤرلاىةوزظ-+*/.,_/!@#$%^&?؟t�Ð'
        translated = ''
        for sympol in message:
            num = LETTERS.find(sympol)
            if mode == 'E': num += key
            if mode == 'D': num -= key
            if num >= len(LETTERS): num -= len(LETTERS)
            elif num < 1: num = num + len(LETTERS)
            translated += LETTERS[num]
        anssert.insert(END,translated)

  lab1 = Label(enc, text='Enter Message:  ⬇', font=('Impact',23), bg='#2d8f10',fg='white')
  lab1.place(x=10, y=60)
  En1 = Entry(enc, justify=CENTER, font=('Imact',25),bd=3,relief=RIDGE,width=29,bg='white',fg='black')
  En1.place(x=10, y=120)
  lab2 = Label(enc, text='Enter Mode:  ➡', font=('Impact',23), bg='#2d8f10',fg='white')
  lab2.place(x=10, y=182)
  Ent1 = Entry(enc, justify=CENTER, font=('Impact',25),bd=3,relief=RIDGE,width=13,bg='white',fg='black')
  Ent1.place(x=298, y=184)
  lab3 = Label(enc, text='You The Message: ', font=('Impact',23), bg='#2d8f10',fg='black')
  lab3.place(x=10, y=260)
  Bt1 = Button(enc, text='✔', fg='#F7F9F9', bg='green',bd=5, font=('Impact',23),command=ok)
  Bt1.place(x=440, y=250, width=100, height=50)
  Bt2 = Button(enc, text='❌', fg='#F7F9F9', bg='red',bd=5, font=('Impact',23),command=Del)
  Bt2.place(x=325, y=250, width=100, height=50)
  anssert = Entry(enc, justify=LEFT, font=('Imact',25),bd=5,relief=RIDGE,width=29,bg='white',fg='black')
  anssert.place(x=10, y=309,height=150)
  enc.mainloop()

##  App GPS  ##
def GPS():
  
  enc = Tk()
  enc.geometry('550x550')
  enc.title('GPS NUMBER')
  enc.config(background='#e7af37')
  enc.iconbitmap("image/logo2.ico")
  title = Label(enc, text='APP GPS', font=('Courier',15), bg='black',fg='white')
  title.pack(fill=X)

  def Del():
    En1.delete('0',END)
    Ent1.delete('0',END)
    anssert.delete('0',END)

  def ok(enent=None):
    pas = En1.get()
    pao = Ent1.get()
    if pas:
        import phonenumbers
        from phonenumbers import carrier, geocoder, timezone
        Number = pas
        phone_numbers = phonenumbers.parse('+2'+Number)
        anssert.insert(END,f"{(geocoder.description_for_number(phone_numbers, 'en'))}/")
        anssert.insert(END,f"{carrier.name_for_number(phone_numbers, 'en')}/")
        anssert.insert(END,timezone.time_zones_for_geographical_number(phone_numbers))

    if pao:
        import geocoder
        our_ip = geocoder.ip("me")
        anssert.insert(END,our_ip)

  lab1 = Label(enc, text='Enter Number:  ⬇', font=('Impact',23), bg='#e7af37',fg='white')
  lab1.place(x=10, y=60)
  En1 = Entry(enc, justify=CENTER, font=('Impact',25),bd=3,relief=RIDGE,width=29,bg='white',fg='black')
  En1.place(x=10, y=120)
  lab2 = Label(enc, text='Enter IP:  ➡', font=('Impact',23), bg='#e7af37',fg='white')
  lab2.place(x=10, y=182)
  Ent1 = Entry(enc, justify=CENTER, font=('Imact',25),bd=3,relief=RIDGE,width=15,bg='white',fg='black')
  Ent1.place(x=263, y=184)
  lab3 = Label(enc, text='Locetion Number: ', font=('Impact',23), bg='#e7af37',fg='black')
  lab3.place(x=10, y=260)
  Bt1 = Button(enc, text='✔', fg='#F7F9F9', bg='green',bd=5, font=('Impact',23),command=ok)
  Bt1.place(x=440, y=250, width=100, height=50)
  Bt2 = Button(enc, text='❌', fg='#F7F9F9', bg='red',bd=5, font=('Impact',23),command=Del)
  Bt2.place(x=325, y=250, width=100, height=50)
  anssert = Entry(enc, justify=LEFT, font=('Imact',25),bd=5,relief=RIDGE,width=29,bg='white',fg='black')
  anssert.place(x=10, y=309,height=150)
  enc.mainloop()

##  APPS  ##
def Control():
  pro = Tk()
  pro.geometry('550x450')
  pro.title('Apps')
  pro.config(background='#5801c9')
  pro.iconbitmap(r"image/logo2.ico")
  title = Label(pro, text='APPS ALSALAM', font=('Courier',15), bg='black',fg='white')
  title.pack(fill=X)
  def ok(enent=None):
      nam = En1.get()
      if nam == 'enc' or nam == 'تشفير': ENC()
      if nam == 'gps' or nam == 'رقم': GPS()
      else:   
        Error = Label(pro,text='Error Kebord!',fg='red', bg='#5801c9', font=('Courier',18))
        Error.place(x=100,y=200)
  lb1 = Label(pro, text=' You Want [GPS Numbers] or [Encrypchen] ', font=('Impact',23), bg='black',fg='white')
  lb1.place(x=10, y=60)
  lb2 = Label(pro, text='💻 Enter What You Want: ', font=('Impact',23), bg='#5801c9',fg='white')
  lb2.place(x=10, y=149)
  lb3 = Label(pro, text='🤔', font=('Impact',53), bg='#5801c9',fg='#ff553e')
  lb3.place(x=360, y=114)
  En1 = Entry(pro, justify=CENTER, font=('Imact',25),bd=4,relief=RIDGE,width=23,bg='white',fg='black')
  En1.place(x=10, y=240)
  Bt6 = Button(pro, text='✔', fg='#F7F9F9', bg='green',bd=5, font=('Impact',23),command=ok)
  Bt6.place(x=460, y=238, width=80, height=50)
  photo = PhotoImage(file="E:\my files\yousef programing\APPS\APP\image\logo155.png")
  panal = Label(pro, image=photo)
  panal.place(x=-2, y=300)
  pro.mainloop()

if __name__ == '__main__':
  Control()
