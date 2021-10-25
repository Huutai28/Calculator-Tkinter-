from tkinter import *
from tkinter import messagebox

root =Tk()
root.title('Máy tính')
root.geometry('520x390')
root.resizable(False, False)

f = ('Time',14)

lnum1 =Label(root,text='Số thứ nhất',font=f)
lnum1.place(x=70,y=50)
lnum2 =Label(root,text='Số thứ hai',font=f)
lnum2.place(x=70,y=120)
lnum3 =Label(root,text='Kết quả',font=f)
lnum3.place(x=70,y=300)

num1= Entry(root,font=f)
num1.place(x=220,y=50)
num2= Entry(root,font=f)
num2.place(x=220,y=120)
num3= Entry(root,font=f)
num3.place(x=220,y=300)
def validate():
    #kiem tra rong
    if num1.get() == "":
        messagebox.showinfo("Thông Báo", "Chỗ này phải nhập")
        num1.focus()
        return False
    if num2.get() == "":
        messagebox.showinfo("Thông Báo", "Chỗ này phải nhập")
        num2.focus()
        return False
    #kiem tra la so
    try:
        int(num1.get())
        int(num2.get())
    except ValueError:
        messagebox.showinfo("Thông Báo","Nhập vào phải là số")
        return False

def add():
    #gọi validate, neu validate có loi se dung tinh toan
    if validate() == False:
        return
    #xóa ket qua cua phep tinh truoc do
    num3.delete(0,END)
    #lau gia tri so2 so2
    n1 = num1.get()
    n2 = num2.get()
    #thuc hien phep tính
    n3 = int(n1) + int(n2)
    #in ket qua
    print(n3)
    num3.insert(0, n3)

def minus():
    if validate() == False:
        return
    num3.delete(0,END)
    n1 = num1.get()
    n2 = num2.get()
    n3 = int(n1) - int(n2)
    print(n3)
    num3.insert(0, n3)

def multip():
    if validate() == False:
        return
    num3.delete(0,END)
    n1 = num1.get()
    n2 = num2.get()
    n3 = int(n1) * int(n2)
    print(n3)
    num3.insert(0, n3)

def divide():
    if validate() == False:
        return
    num3.delete(0,END)
    n1 = num1.get()
    n2 = num2.get()
    #validate khong chia so 0
    if num2.get() == "0":
        messagebox.showinfo("Thông Báo", "Không chia số 0")
        num2.focus()
        return
    n3 = int(n1) / int(n2)
    print(n3)
    num3.insert(0, n3)

add_btn = Button(
    root,text='Cộng',font=f,relief=SOLID,command=add
)
add_btn.place(x=70,y=210)
minus_btn = Button(
    root,text='Trừ',font=f,relief=SOLID,command=minus
)
minus_btn.place(x=180,y=210)
multip_btn = Button(
    root,text='Nhân',font=f,relief=SOLID,command=multip
)
multip_btn.place(x=280,y=210)
divide_btn = Button(
    root,text='Chia',font=f,relief=SOLID,command=divide
)
divide_btn.place(x=380,y=210)

root.mainloop()