from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from datetime import date
import time
from tkcalendar import *
import smtplib
import csv
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1630x850")
        self.root.title("ATTENDANCE MANAGEMENT")
        self.root.config(background='White')
        photo=PhotoImage(file='R1.png')
        self.root.iconphoto(False,photo)
        login_frame=Frame(self.root,background='#F9EBEA')
        login_frame.place(x=0,y=0,relwidth=1,relheight=.15)##5371f9'

        l1=Label(login_frame,text="ATTENDANCE SYSTEM",background='#F9EBEA',font=('Consolas',44))
        l1.place(x=500,y=10)

        my_img=Image.open('pillai.png')
        resized=my_img.resize((110,100),Image.ANTIALIAS )
        self.img=ImageTk.PhotoImage(resized)
        icon_label=Label(login_frame,image=self.img,background='#F9EBEA')
        icon_label.place(x=5,y=5)
        #---------------student login--------------------------
        s_frame=Frame(self.root,background='#17202A')
        s_frame.place(x=140,y=200,width=598,height=400)
        s_header=Label(self.root,text="\t FOR STUDENTS",bg='#17202A',font=('Dubai Medium',20),fg="White")
        s_header.place(x=190,y=210)
        s_email=Label(self.root,text="EMAIL ID",bg='#17202A',font=('Dubai Medium',16),fg="white")
        s_email.place(x=150,y=350)
        t_passwd=Label(self.root,text="ROLL NO. ",bg='#17202A',font=('Dubai Medium',16),fg="white")
        t_passwd.place(x=150,y=400)
        self.se_email=Entry(self.root,width=30,bg='white',bd=0,font=(14))
        self.se_email.place(x=270,y=350,height=32)
        self.se_passwd=Entry(self.root,width=30,bg='white',bd=0,font=(14))
        self.se_passwd.place(x=270,y=400,height=32)
        #-----------------Login Button------------------------------
        my_img4=Image.open('R7.png')
        resized4=my_img4.resize((160,40),Image.ANTIALIAS )
        self.img4=ImageTk.PhotoImage(resized4)
        s_login=Button(self.root,image=self.img4,bg='#17202A',bd=0,activebackground='#17202A',fg='white',font=(16),cursor='hand2',command=self.student_page)
        s_login.place(x=340,y=500)

        #--------------------teacher login--------------------------------------------
        t_frame=Frame(self.root,background='#AED6F1')#EDBB99''#D35400'-orange
        t_frame.place(x=740,y=200,width=600,height=400)
        t_header=Label(self.root,text="\t FOR TEACHERS ",bg='#AED6F1',font=('Dubai Medium',20),fg="White")
        t_header.place(x=800,y=210)
        t_email=Label(self.root,text="EMAIL ID",bg='#AED6F1',font=('Dubai Medium',16))
        t_email.place(x=755,y=350)
        t_passwd=Label(self.root,text="PASSWORD ",bg='#AED6F1',font=('Dubai Medium',16))
        t_passwd.place(x=755,y=400)
        self.te_email=Entry(self.root,width=30,bg='white',bd=0,font=(14))
        self.te_email.place(x=900,y=350,height=32)
        self.te_passwd=Entry(self.root,width=30,bg='white',bd=0,font=(14),show="*")
        self.te_passwd.place(x=900,y=400,height=32)
        #--------------login teacher button------------------
        my_img3=Image.open('R5.png')
        resized3=my_img3.resize((160,40),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(resized3)
        t_login=Button(self.root,image=self.img3,bg='#AED6F1',bd=0,activebackground='#AED6F1',font=(16),cursor='hand2',command=self.teacher_functions)
        t_login.place(x=900,y=500)
        #-------------signup teacher button-------------------------------
        my_img2=Image.open('R2.png')
        resized2=my_img2.resize((160,40),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(resized2)
        t_signup=Button(self.root,image=self.img2,bg='#AED6F1',bd=0,activebackground='#AED6F1',font=(16),cursor='hand2',command=self.sign_up)
        t_signup.place(x=1080,y=500)
        
        #-------------------forgot passwd--------------------------
        t_fpasswd=Button(self.root,text="Forgot Password ? ",bg='#AED6F1',border=0,cursor='hand2',command=self.frgt_passwd,activebackground='#AED6F1',activeforeground='blue')
        t_fpasswd.place(x=1000,y=550)

    def student_page(self):
        if "_" not in self.se_passwd.get():
            messagebox.showerror("ERROR","Wrong Password")
        else:
            if self.se_email.get()=="" or self.se_passwd.get()=="":
                messagebox.showerror("ERROR","enter all Details",parent=self.root)
            else:
                passwd=(self.se_passwd.get().split("_"))
                self.export_to_excel(passwd[0])
                mycursor.execute("SELECT name,roll_no,sub1_per,sub2_per,sub3_per,sub4_per,sub5_per,sub6_per,total_per FROM student_table WHERE email=%s and class=%s and roll_no=%s",(self.se_email.get(),passwd[0],passwd[1],))
                result=mycursor.fetchone()
                if result==None:
                    messagebox.showerror("ERROR","Wrong Password or Email",parent=self.root)
                else:
                    
                    self.root9=Toplevel()
                    self.root9.geometry("1630x850")
                    self.root9.focus_force()
                    self.root9.overrideredirect(True)
                    self.root9.grab_set()
                    self.root9.config(bg="White")
                    icon_photo2=PhotoImage(file='R1.png')
                    self.root9.iconphoto(False,icon_photo2)
                    login_frame1=Frame(self.root9,background='#F9EBEA')
                    login_frame1.place(x=0,y=0,relwidth=1,relheight=.15)##5371f9'

                    l1=Label(login_frame1,text=result[0],background='#F9EBEA',font=('Consolas',44))
                    l1.place(x=500,y=20)

                    my_img50=Image.open('pillai.png')
                    resized50=my_img50.resize((110,100),Image.ANTIALIAS )
                    self.img50=ImageTk.PhotoImage(resized50)
                    icon_label=Label(login_frame1,image=self.img50,background='#F9EBEA')
                    icon_label.place(x=5,y=5)

                    my_img46=Image.open('R57.png')
                    resized46=my_img46.resize((160,70),Image.ANTIALIAS )
                    self.img46=ImageTk.PhotoImage(resized46)
                    logout_button=Button(self.root9,image=self.img46,border=0,background="white",activebackground="White",activeforeground="White",command=self.logout)
                    logout_button.place(x=1200,y=680)

                    fram=Frame(self.root9,bg="WHITE")
                    fram.place(x=100,y=130,relwidth=.5,relheight=.5)
                    label1=Label(fram,text="Name",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=0,column=0,padx=20)
                    label1=Label(fram,text="Roll No",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=1,column=0,padx=20)
                    label1=Label(fram,text="DLCA",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=2,column=0,padx=20)
                    label1=Label(fram,text="DSGT",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=3,column=0,padx=20)
                    label1=Label(fram,text="CG",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=4,column=0,padx=20)
                    label1=Label(fram,text="DS",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=5,column=0,padx=20)
                    label1=Label(fram,text="OOPJ",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=6,column=0,padx=20)
                    label1=Label(fram,text="EM3",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=7,column=0,padx=20)
                    label1=Label(fram,text="TOTAL ",bg='White',font=('Dubai Medium',16))
                    label1.grid(row=8,column=0,padx=20)
                    for row in range(9):
                        #for column in range(1):
                        label=Label(fram,text=result[row],fg="black",bg='White',font=('Dubai Medium',16))
                        label.grid(row=row,column=1,sticky="nsew",padx=10,pady=5)
                        #fram.grid_columnconfigure(1,weight=1)
                        fram.grid_rowconfigure(row,weight=1)

    def logout(self):
        ans=messagebox.askyesno("logout","Do you Wanna Logout",parent=self.root9)
        if ans==True:
            time.sleep(.5)
            self.root9.destroy()
            self.se_passwd.delete(0,END)
            self.se_email.delete(0,END)


    def frgt_passwd(self):
        mycursor.execute("SELECT * FROM teacher WHERE email=%s",(self.te_email.get(),))
        keyans=mycursor.fetchone()
        if keyans==None:
            messagebox.showerror("ERROR","Email Id Does NoT Exist")
        else:
            
            self.root2=Toplevel()
            self.root2.geometry("600x400+500+200")
            self.root2.focus_force()
            self.root2.grab_set()
            self.root2.config(bg="White")
            icon_photo2=PhotoImage(file='R1.png')
            self.root2.iconphoto(False,icon_photo2)

            f_email=Label(self.root2,text="Email Id",bg='White',font=('Dubai Medium',16))
            f_email.place(x=20,y=50)

            f_sec_que=Label(self.root2,text="Question",bg='White',font=('Dubai Medium',16))
            f_sec_que.place(x=20,y=110)

            f_sec_que=Label(self.root2,text="Answer",bg='White',font=('Dubai Medium',16))
            f_sec_que.place(x=20,y=170)
            f1_sec=Label(self.root2,text="New Password",bg='White',font=('Dubai Medium',16))
            f1_sec.place(x=20,y=230)
            f2_sec=Label(self.root2,text="Confirm Password",bg='White',font=('Dubai Medium',16))
            f2_sec.place(x=20,y=290)
            
            #--------------entry boxes-----------------------------------------
            self.f_email_entry=Entry(self.root2,width=30,bg='#AED6F1',bd=0,font=(14))
            self.f_email_entry.place(x=200,y=50,height=32)

            f_que_entry=Entry(self.root2,width=30,bg='#AED6F1',bd=0,font=(14))
            f_que_entry.place(x=200,y=110,height=32)

            self.f_ans_entry=Entry(self.root2,width=30,bg='#AED6F1',bd=0,font=(14))
            self.f_ans_entry.place(x=200,y=170,height=32)

            self.f_pass_entry=Entry(self.root2,width=30,bg='#AED6F1',bd=0,font=(14),show='*')
            self.f_pass_entry.place(x=200,y=230,height=32)

            self.fc_pass_entry=Entry(self.root2,width=30,bg='#AED6F1',bd=0,font=(14),show='*')
            self.fc_pass_entry.place(x=200,y=290,height=32)

            get_passwd=Button(self.root2,text="Save",command=self.get_pass)
            get_passwd.place(x=230,y=350)

            self.f_email_entry.insert(0,keyans[1])
            self.f_email_entry.config(state=DISABLED)
            f_que_entry.insert(0,keyans[2])
            f_que_entry.config(state=DISABLED)

    def get_pass(self):
        mycursor.execute("SELECT * FROM teacher WHERE email=%s and security_ans=%s",(self.te_email.get(),self.f_ans_entry.get()))
        keyans=mycursor.fetchone()
        if keyans==None:
            messagebox.showerror("ERROR","Incorrect Answer",parent=self.root2)
            self.f_ans_entry.delete(0,END)
            self.fc_pass_entry.delete(0,END)
            self.f_pass_entry.delete(0,END)
        elif self.fc_pass_entry=="" or self.f_pass_entry=="":
            messagebox.showerror("ERROR","ENTER ALL CREDENTIALS",parent=self.root2)
        else:
            if self.f_pass_entry.get()!=self.fc_pass_entry.get():
                messagebox.showerror("ERROR","password Dont match",parent=self.root2)
                self.fc_pass_entry.delete(0,END)
            else:
                mycursor.execute("UPDATE teacher SET passwd=%s,c_passwd=%s WHERE email=%s",(self.f_pass_entry.get(),self.f_pass_entry.get(),keyans[1]))
                mydb.commit()
                messagebox.showinfo("SAVED","Password Change Successfully",parent=self.root2)
                self.root2.destroy()
                


    def sign_up(self):
        self.root1=Toplevel()
        self.root1.title("REGISTER")
        self.root1.geometry("1620x850")
        self.root1.focus_force()
        self.root1.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root1.iconphoto(False,icon_photo)
        self.root1.config(background="white")

        register_frame=Frame(self.root1,background='#F9EBEA')
        register_frame.place(x=0,y=0,relwidth=1,relheight=.15)

        l2=Label(register_frame,text="REGISTER",background='#F9EBEA',font=('Consolas',44))
        l2.place(x=670,y=20)
        my_img1=Image.open('R1.png')
        resized1=my_img1.resize((110,100),Image.ANTIALIAS )
        self.img1=ImageTk.PhotoImage(resized1)
        icon_label1=Label(register_frame,image=self.img1,background='#F9EBEA')
        icon_label1.place(x=10,y=5)

        name_label=Label(self.root1,text="Name",bg="White",font=('Dubai Medium',16))
        name_label.place(x=150,y=200)

        email_label=Label(self.root1,text="Email Id",bg="White",font=('Dubai Medium',16))
        email_label.place(x=150,y=250)

        security_question=Label(self.root1,text="Security Question",bg="White",font=('Dubai Medium',16))
        security_question.place(x=150,y=300)

        security_ans=Label(self.root1,text="Security Answer",bg="White",font=('Dubai Medium',16))
        security_ans.place(x=150,y=350)

        passwd_label=Label(self.root1,text="Password",bg="White",font=('Dubai Medium',16))
        passwd_label.place(x=150,y=400)

        c_passwd_label=Label(self.root1,text="Confirm Password",bg="White",font=('Dubai Medium',16))
        c_passwd_label.place(x=150,y=450)

        self.name_entry=Entry(self.root1,bg='#AED6F1',bd=0,font=(14),width=35)
        self.name_entry.place(x=375,y=200)

        self.email_entry=Entry(self.root1,bg='#AED6F1',bd=0,font=(14),width=35)
        self.email_entry.place(x=375,y=250)

        self.security_que_entry=ttk.Combobox(self.root1,values=('select a question','First job','Fav book',"Birth City","Pet's Name"),font=(13),state='readonly',width=33)
        self.security_que_entry.place(x=375,y=300,height=30)
        self.security_que_entry.current(0)

        self.security_ans_entry=Entry(self.root1,bg='#AED6F1',bd=0,font=(14),width=35)
        self.security_ans_entry.place(x=375,y=350)

        self.passwd_entry=Entry(self.root1,show='*',bg='#AED6F1',bd=0,font=(14),width=35)
        self.passwd_entry.place(x=375,y=400)

        self.c_passwd_entry=Entry(self.root1,show='*',bg='#AED6F1',bd=0,font=(14),width=35)
        self.c_passwd_entry.place(x=375,y=450)

        self.var_name=IntVar()
        check=Checkbutton(self.root1,text="Do you agree to",variable=self.var_name,onvalue=1,offvalue=0,activebackground='White',background="White",font=('Dubai Medium',16))
        check.place(x=375,y=500)
        #--------------------Buttons------------------------
        t_and_c=Button(self.root1,text="Terms and condition ",font=("Dubai Medium",16),bg="White",border=0,cursor='hand2',activebackground='White',activeforeground='blue')
        t_and_c.place(x=550,y=500)
        my_img5=Image.open('R8.png')
        resized5=my_img5.resize((140,50),Image.ANTIALIAS )
        self.img5=ImageTk.PhotoImage(resized5)
        register_button=Button(self.root1,image=self.img5,bg="white",bd=0,activebackground="white",command=self.get_values_teacher)
        register_button.place(x=300,y=580)

    
    def get_values_teacher(self):

        if self.name_entry.get()=="" or self.email_entry.get()=="" or self.security_que_entry.get()=="select a question" or self.security_ans_entry.get()=="" or self.passwd_entry.get()=="" or self.c_passwd_entry.get()=="":
            messagebox.showerror("ERROR","ENTER ALL CREDENTIALS",parent=self.root1)
        elif self.passwd_entry.get()!=self.c_passwd_entry.get():
            messagebox.showerror("ERROR","PASSWORD DO NOT MATCH",parent=self.root1)
        elif self.var_name.get()==0:
            messagebox.showerror("ERROR","PLEASE ,AGREE TO TERMS AND CONDITION",parent=self.root1)
        else:
            mycursor.execute("SELECT * FROM teacher  WHERE email=%s",(self.email_entry.get(),))
            email_id=mycursor.fetchone()
            if email_id!=None:
                messagebox.showerror("ERROR","EMAIL ID ALREADY EXISTS",parent=self.root1)
            else:
                sql_formula_1="INSERT INTO teacher(name,email,security_que,security_ans,passwd,c_passwd) VALUES(%s,%s,%s,%s,%s,%s)"
                keys=(self.name_entry.get(),self.email_entry.get(),self.security_que_entry.get(),self.security_ans_entry.get(),self.passwd_entry.get(),self.c_passwd_entry.get())
                mycursor.execute(sql_formula_1,keys)
                mydb.commit()
                messagebox.showinfo("SUCCESS","REGISTRATION SUCCESFULL",parent=self.root1)
                self.clear()
                self.root1.destroy()

    def clear(self):
        self.name_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.security_que_entry.set('select any question')
        self.security_ans_entry.delete(0,END)
        self.passwd_entry.delete(0,END)
        self.c_passwd_entry.delete(0,END)
        self.var_name.set(0)

    def teacher_functions(self):
        mycursor.execute("SELECT email,passwd FROM teacher WHERE email=%s and passwd=%s",(self.te_email.get(),self.te_passwd.get()))
        logincode=mycursor.fetchone()
        if logincode==None:
            messagebox.showerror("ERROR","Invalid Email Id Or Password",parent=self.root)
            self.te_passwd.delete(0,END)
        else:
            self.te_email.delete(0,END)
            self.te_passwd.delete(0,END)
            self.root3=Toplevel()
            self.root3.title("CLASSES")
            self.root3.geometry("1620x850")
            self.root3.focus_force()
            self.root3.grab_set()
            icon_photo=PhotoImage(file='R1.png')
            self.root3.iconphoto(False,icon_photo)
            self.root3.config(background="white")

            t_home_frame=Frame(self.root3,background='#F9EBEA')
            t_home_frame.place(x=0,y=0,relwidth=1,relheight=.15)

            l3=Label(t_home_frame,text="TEACHER",background='#F9EBEA',font=('Consolas',44))
            l3.place(x=670,y=20)
            
            #--------------------buttons-----------------------
            my_img8=Image.open('R32.png')
            resized8=my_img8.resize((500,100),Image.ANTIALIAS )
            self.img8=ImageTk.PhotoImage(resized8)
            create_class=Button(self.root3,image=self.img8,bd=0,activebackground="white",bg="white",cursor="hand2",command=self.create_new_class)
            create_class.place(x=200,y=300)
            my_img9=Image.open('R33.png')
            resized9=my_img9.resize((500,100),Image.ANTIALIAS )
            self.img9=ImageTk.PhotoImage(resized9)
            select_class=Button(self.root3,image=self.img9,bd=0,activebackground="white",bg="white",cursor="hand2",command=self.select_class)
            select_class.place(x=200,y=450)

        

    
    def select_class(self):
        self.root5=Toplevel()
        self.root5.title("SELECT CLASS")
        self.root5.geometry("500x400+800+200")
        self.root5.focus_force()
        self.root5.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root5.iconphoto(False,icon_photo)
        self.root5.config(background="white")

        select_class_header_frame=Frame(self.root5,background='#F9EBEA')
        select_class_header_frame.place(x=0,y=0,relwidth=1,relheight=.15)

        l3=Label(select_class_header_frame,text="SELECT CLASS",background='#F9EBEA',font=('Consolas',20))
        l3.place(x=160,y=10)

        select_class_frame=Frame(self.root5)
        select_class_scrollbar=Scrollbar(select_class_frame,orient=VERTICAL)
        self.list_box=Listbox(select_class_frame,bg="pink",width=40,yscrollcommand=select_class_scrollbar.set)
        select_class_scrollbar.config(command=self.list_box.yview)
        select_class_scrollbar.pack(side=RIGHT,fill=Y)
        sql_formula_3="SELECT class_name FROM class"
        mycursor.execute(sql_formula_3)
        result=mycursor.fetchall()
        for r in result:
            self.list_box.insert(END,r)
        
        
        select_class_frame.place(x=130,y=100)
        self.list_box.pack()

        my_img7=Image.open('R43.png')
        resized7=my_img7.resize((140,50),Image.ANTIALIAS )
        self.img7=ImageTk.PhotoImage(resized7)
        select_button=Button(self.root5,image=self.img7,bg="white",activebackground="white",cursor='hand2',bd=0,command=self.select_class_again)
        select_button.place(x=100,y=300)

        my_img44=Image.open('R44.png')
        resized44=my_img44.resize((140,50),Image.ANTIALIAS )
        self.img44=ImageTk.PhotoImage(resized44)
        delete_button=Button(self.root5,image=self.img44,bg="white",activebackground="white",cursor='hand2',bd=0,command=self.delete_class)
        delete_button.place(x=300,y=300)
        
    def delete_class(self):
        if self.list_box.get(ANCHOR)=="":
            messagebox.showerror("ERROR","SELECT A CLASS",parent=self.root5)
        else:
            self.root14=Toplevel()
            self.root14.geometry("500x400+800+200")
            self.root14.focus_force()
            self.root14.grab_set()
            icon_photo=PhotoImage(file='R1.png')
            self.root14.iconphoto(False,icon_photo)
            self.root14.config(background="white")
            self.root14.title("DELETE")
            fram=Frame(self.root14,background='#F9EBEA')
            fram.place(relwidth=1,relheight=.15)
            fram_text=Label(fram,text="Delete Class",font=('Consolas',28),background='#F9EBEA')
            fram_text.place(x=140,y=15)

            cc_label=Label(self.root14,text="CC :",bg="White",font=("Dubai MEdium",15))
            cc_label.place(x=50,y=100)
            self.cc_entry=Entry(self.root14,width=20,bg='#F9EBEA',font=('Dubai Medium',16))
            self.cc_entry.place(x=100,y=100,height=30)

            button=Button(self.root14,text="Confirm DELETE",command=self.con_delete)
            button.place(x=100,y=200)
    
    def con_delete(self):
        c_del=''.join(self.list_box.get(ANCHOR))
        #print(c_del)
        #print(self.cc_entry.get())
        mycursor.execute("SELECT * FROM class WHERE class_name=%s and cc=%s",(c_del,self.cc_entry.get()))
        te_login=mycursor.fetchone()
        if te_login==None:
            messagebox.showerror("ERROR","Incorrct Class Cordinator's Name",parent=self.root14)
        else:
            mycursor.execute("DELETE FROM student_table WHERE class=%s",(c_del,))
            mydb.commit()
            mycursor.execute("DELETE FROM class WHERE class_name=%s",(c_del,))
            mydb.commit()
            ans=messagebox.showinfo("DELETED","Successfully Deleted",parent=self.root14)
            if ans=='ok':
                time.sleep(.5)
                self.root14.destroy()
                self.root5.destroy()



            

    def select_class_again(self):
        if self.list_box.get(ANCHOR)=="":
            messagebox.showerror("ERROR","SELECT A CLASS",parent=self.root5)
        else:
            sql_formula_4="SELECT * FROM class WHERE class_name=%s"
            keys4=(self.list_box.get(ANCHOR))
            mycursor.execute(sql_formula_4,keys4)
            result2=mycursor.fetchall()
            for rows in result2:
                if rows[1]=='COMPUTER ENGINEERING' and rows[2]=="III":
                    self.ce3()
                if rows[1]=='INFORMATION TECHNOLOGY' and rows[2]=="III":
                    self.it3()
    
    def it3(self):
        classname="CLASS "+str(self.list_box.get(ANCHOR))
        self.root6=Toplevel()
        self.root6.title(classname)
        self.root6.geometry("1630x850")
        self.root6.focus_force()
        self.root6.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root6.iconphoto(False,icon_photo)
        self.root6.config(background="white")

        

    def ce3(self):
        ans=''.join(self.list_box.get(ANCHOR))
        classname="CLASS "+ans 
        self.root6=Toplevel()
        self.root6.title(classname)
        self.root6.geometry("1630x850")
        self.root6.focus_force()
        self.root6.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root6.iconphoto(False,icon_photo)
        self.root6.config(background="white")
        #---------------header frame-----------------------
        t_class_frame=Frame(self.root6,background='#F9EBEA')
        t_class_frame.place(x=0,y=0,relwidth=1,relheight=.15)

        l3=Label(t_class_frame,text="SELECT SUBJECT",background='#F9EBEA',font=('Consolas',44))
        l3.place(x=600,y=20)

        #---------------------buttons for subjects----------------------------
        my_img10=Image.open('R29.png')
        resized10=my_img10.resize((180,180),Image.ANTIALIAS )
        self.img10=ImageTk.PhotoImage(resized10)
        dlca_button=Button(self.root6,image=self.img10,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.call_function('dlca',ans))
        dlca_button.place(x=180,y=190)

        my_img11=Image.open('R27.png')
        resized11=my_img11.resize((180,180),Image.ANTIALIAS )
        self.img11=ImageTk.PhotoImage(resized11)
        dsgt_button=Button(self.root6,image=self.img11,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.call_function('dsgt',ans))
        dsgt_button.place(x=700,y=190)

        my_img12=Image.open('R26.png')
        resized12=my_img12.resize((180,180),Image.ANTIALIAS )
        self.img12=ImageTk.PhotoImage(resized12)
        cg_button=Button(self.root6,image=self.img12,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.call_function('cg',ans))
        cg_button.place(x=1200,y=190)

        my_img13=Image.open('R30.png')
        resized13=my_img13.resize((180,180),Image.ANTIALIAS )
        self.img13=ImageTk.PhotoImage(resized13)
        ds_button=Button(self.root6,image=self.img13,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.call_function('ds',ans))
        ds_button.place(x=180,y=400)

        my_img14=Image.open('R31.png')
        resized14=my_img14.resize((180,180),Image.ANTIALIAS )
        self.img14=ImageTk.PhotoImage(resized14)
        oopj_button=Button(self.root6,image=self.img14,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.call_function('oopj',ans))
        oopj_button.place(x=700,y=400)

        my_img15=Image.open('R25.png')
        resized15=my_img15.resize((180,180),Image.ANTIALIAS )
        self.img15=ImageTk.PhotoImage(resized15)    
        em3_button=Button(self.root6,image=self.img15,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.call_function('ceem3',ans))
        em3_button.place(x=1200,y=400) 

        my_img16=Image.open('R34.png')#R20.png')
        resized16=my_img16.resize((300,80),Image.ANTIALIAS )
        self.img16=ImageTk.PhotoImage(resized16)
        classname3=''.join(self.list_box.get(ANCHOR))
        add_students_button=Button(self.root6,image=self.img16,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.add_students(classname3))
        add_students_button.place(x=650,y=640)

        my_img41=Image.open('R41.png')#R20.png')
        resized41=my_img41.resize((250,50),Image.ANTIALIAS )
        self.img41=ImageTk.PhotoImage(resized41)
        export_button=Button(self.root6,image=self.img41,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda: self.export(classname3))
        export_button.place(x=1100,y=640)

        my_img40=Image.open('R42.png')#R20.png')
        resized40=my_img40.resize((250,50),Image.ANTIALIAS )
        self.img40=ImageTk.PhotoImage(resized40)
        send_mail_button=Button(self.root6,image=self.img40,bg="white",cursor='hand2',bd=0,activebackground="white",command=lambda :self.send_mail_func(classname3))
        send_mail_button.place(y=640,x=260)

    def call_function(self,result,classname2):
        self.root7=Toplevel()
        self.root7.geometry("1630x850")
        self.root7.focus_force()
        self.root7.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root7.iconphoto(False,icon_photo)
        self.root7.config(background="white")
    
        if result=='dlca':
            self.root7.title("Digital logic and computer architechture")
            self.page_functions(result,classname2)
        if result=='dsgt':
            self.root7.title("D.S.G.T")
            self.page_functions(result,classname2)
        if result=='cg':
            self.root7.title("Computer Graphics")
            self.page_functions(result,classname2)
        if result=='ds':
            self.root7.title("Data Structure")
            self.page_functions(result,classname2)
        if result=='oopj':
            self.root7.title("Object oriented programming with java")
            self.page_functions(result,classname2)
        if result=='ceem3':
            self.root7.title("Applied Mathematics 3")
            self.page_functions(result,classname2)

         #---------------header frame-----------------------
        t_class_frame=Frame(self.root7,background='#F9EBEA')
        t_class_frame.place(x=0,y=0,relwidth=1,relheight=.15)
        l3=Label(t_class_frame,text="MARK ATTENENDANCE",background='#F9EBEA',font=('Consolas',44))
        l3.place(x=570,y=20)
        info_frame=Frame(self.root7,background='#F9EBEA')
        info_frame.place(x=0,y=140,relwidth=1,relheight=.03)

        info_label=Label(info_frame,text="Enter Roll no. Space Seperated",background='#F9EBEA',font=('Consolas',14))
        info_label.place(x=600,y=0)


    def page_functions(self,result,classname2):
        frame2=Frame(self.root7,background='#AED6F1')
        frame2.place(x=100,y=200,relheight=.6,relwidth=.4)

        self.date_entry=Entry(self.root7,width=12,font=('Consolas',14),bd=0)
        self.date_entry.place(x=510,y=220,height=24)

        date_label=Label(self.root7,text="Date : ",background='#AED6F1',font=('Consolas',12))
        date_label.place(x=430,y=220)

        my_img19=Image.open('R35.png')
        resized19=my_img19.resize((22,22),Image.ANTIALIAS )
        self.img19=ImageTk.PhotoImage(resized19)
        date_button=Button(self.root7,image=self.img19,bg="White",bd=0,cursor='hand2',command=self.get_today)
        date_button.place(x=630,y=220)

        date1_label=Label(self.root7,text="Enter Roll number ",background='#AED6F1',font=('Consolas',13))
        date1_label.place(x=230,y=320)
        self.entry=Entry(self.root7,width=30,bg="White",font=('Consolas',14),bd=0)
        self.entry.place(x=230,y=350,height=24)


        my_img38=Image.open('R38.png')
        resized38=my_img38.resize((130,50),Image.ANTIALIAS )
        self.img38=ImageTk.PhotoImage(resized38)    
        add_button=Button(self.root7,image=self.img38,bg='#AED6F1',bd=0,cursor='hand2',activebackground='#AED6F1',command=lambda :self.add_attendece(result,classname2))
        add_button.place(x=260,y=550)

        my_img47=Image.open('R47.png')
        resized47=my_img47.resize((150,50),Image.ANTIALIAS )
        self.img47=ImageTk.PhotoImage(resized47)   
        add_all_button=Button(self.root7,image=self.img47,bg='#AED6F1',bd=0,cursor='hand2',activebackground='#AED6F1',command=lambda :self.save_it(result,classname2))
        add_all_button.place(x=420,y=550) 

        #add_button=Button(self.root7,text="Save",command=lambda :self.save_it(result,classname2))
        #add_button.place(x=400,y=450)
        
        frame1=Frame(self.root7,background='#AED6F1')
        frame1.place(x=750,y=200,relheight=.6,relwidth=.4)

        tabs=ttk.Notebook(self.root7)
        tabs.place(x=800,y=250)

        self.fram1=Frame(tabs,width=500,height=350,bg="White")
        self.fram2=Frame(tabs,width=500,height=350,bg="White")

        self.fram1.pack(fill="both",expand=1)
        self.fram2.pack(fill="both",expand=1)

        tabs.add(self.fram1,text=" Search By Roll No.")
        tabs.add(self.fram2,text="Sort By percentage")

        self.fram1_entry=Entry(self.fram1,width=35,bd=0,bg='#AED6F1')
        self.fram1_entry.place(x=130,y=20,height=24)
        button=Button(self.fram1,text="Enter",command=lambda: self.search_by_roll(result,classname2))
        button.place(x=350,y=20)

        label_fram1=Label(self.fram1,text="No. Days Absent",bg="White")
        label_fram1.place(x=60,y=300)

        label_fram1=Label(self.fram1,text="No. Days Present",bg="White")
        label_fram1.place(x=290,y=300)
        

        self.fram1_entry1=Entry(self.fram1,width=5,bd=0,bg='#AED6F1')
        self.fram1_entry1.place(x=160,y=300,height=24)
        self.fram1_entry2=Entry(self.fram1,width=5,bd=0,bg='#AED6F1')
        self.fram1_entry2.place(x=390,y=300,height=24)

        
        select_class_frame=Frame(self.fram1)
        select_class_scrollbar=Scrollbar(select_class_frame,orient=VERTICAL)
        self.date_box=Listbox(select_class_frame,bg="White",bd=2,width=60,yscrollcommand=select_class_scrollbar.set)
        select_class_scrollbar.config(command=self.date_box.yview)
        select_class_scrollbar.pack(side=RIGHT,fill=Y)

        select_class_frame.place(x=70,y=100)
        self.date_box.pack()

        self.fram2_entry=Entry(self.fram2,width=35,bd=0,bg='#AED6F1')
        self.fram2_entry.place(x=130,y=20,height=24)
        button=Button(self.fram2,text="Enter",command=lambda :self.cutoff_marks(result,classname2))
        button.place(x=350,y=20)

        select_class_frame2=Frame(self.fram2)
        select_class_scrollbar=Scrollbar(select_class_frame2,orient=VERTICAL)
        self.date_box1=Listbox(select_class_frame2,bg="White",bd=2,width=60,yscrollcommand=select_class_scrollbar.set)
        select_class_scrollbar.config(command=self.date_box1.yview)
        select_class_scrollbar.pack(side=RIGHT,fill=Y)

        select_class_frame2.place(x=70,y=100)
        self.date_box1.pack()

    def send_mail_func(self,classname3):
        self.root13=Toplevel()
        self.root13.geometry("530x500+170+175")
        self.root13.focus_force()
        self.root13.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root13.iconphoto(False,icon_photo)
        self.root13.config(background="white")
        self.root13.title("Mail Settings")
        self.export_to_excel(classname3)
        fram=Frame(self.root13,background='#F9EBEA')
        fram.place(relwidth=1,relheight=.15)
        
        fram_text=Label(fram,text="Email",font=('Consolas',28),background='#F9EBEA')
        fram_text.place(x=190,y=20)

        info_text_fram=Label(self.root13,background='#F9EBEA')
        info_text_fram.place(x=0,y=80,relheight=.08,relwidth=1)

        info_text_label=Label(info_text_fram,text="Turn On less Secure apps",font=('Consolas',14),background='#F9EBEA')
        info_text_label.place(x=140,y=5)

        emailid_label=Label(self.root13,text="Email",bg="White",font=('Consolas',14))
        emailid_label.place(x=0,y=130)

        emailpass_label=Label(self.root13,text="Password",bg="White",font=('Consolas',14))
        emailpass_label.place(x=0,y=190)

        cutoff_label=Label(self.root13,text="Cut off",bg="White",font=('Consolas',14))
        cutoff_label.place(x=0,y=250)

        self.emailid_entry=Entry(self.root13,width=30,font=('Consolas',14),background='#F9EBEA')
        self.emailid_entry.place(x=100,y=130)

        self.emailpass_entry=Entry(self.root13,width=30,show='*',font=('Consolas',14),background='#F9EBEA')
        self.emailpass_entry.place(x=100,y=190)

        self.cutoff_entry=Entry(self.root13,width=10,font=('Consolas',14),background='#F9EBEA')
        self.cutoff_entry.place(x=100,y=250)

        emailid_button=Button(self.root13,text="send",command=lambda: self.final_send(classname3))
        emailid_button.place(x=80,y=320)

        info_label=Label(self.root13,text="Wait Until POP up Appears",bg="white")
        info_label.place(x=100,y=380)

    def final_send(self,classname3):
        if(self.emailid_entry.get()=="" or self.emailpass_entry.get()=="" or self.cutoff_entry.get()==""):
            messagebox.showerror("ERROR","Enter All credentials",parent=self.root13)
        else:
            
            
            mycursor.execute("SELECT email FROM student_table WHERE class=%s and total_per <%s",(classname3,self.cutoff_entry.get(),))
            result=mycursor.fetchall()
            try :
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(self.emailid_entry.get(),self.emailpass_entry.get())
                msg="Dear Student,\nYour attendance is less than "+self.cutoff_entry.get()+" Kindly pay heed to the same and maintain the required attendence.\n\nRegards,\nPillai College of Engineering"
                subject="** Attendance Alert **"
                body="Subject: {}\n\n{}".format(subject,msg)
                for x in result:
                    server.sendmail(self.emailid_entry.get(),x,body)
                server.quit()   
                messagebox.showinfo("SUCCESS","Mail Send Successfully",parent=self.root13)
            except smtplib.SMTPAuthenticationError :
                messagebox.showerror("ERROR","incorrect Email ID or password",parent=self.root13)
        
    def export(self,classname3):
        self.root12=Toplevel()
        self.root12.geometry("230x210+440+275")
        self.root12.focus_force()
        self.root12.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root12.iconphoto(False,icon_photo)
        self.root12.config(background="white")
        self.root12.title("Excel")
        fram=Frame(self.root12,background='#F9EBEA')
        fram.place(relwidth=1,relheight=.15)
        
        fram_text=Label(fram,text="Excel",font=('Consolas',12),background='#F9EBEA')
        fram_text.place(x=90,y=5)

        

        excel_label=Label(self.root12,text="File Name",bg="White")
        excel_label.place(x=0,y=40)
        self.excel_name=Entry(self.root12,widt=25)
        self.excel_name.place(x=70,y=40)

        button_save=Button(self.root12,text="Save",command=lambda : self.export2(classname3))
        button_save.place(x=70,y=90)

    
    def export2(self,classname3):
        if self.excel_name.get()=="":
            messagebox.showerror("ERROR","please Enter a name")
        else:
            self.export_to_excel(classname3)
            mycursor.execute("SELECT roll_no,name,class,sub1_dates,sub2_dates,sub3_dates,sub4_dates,sub5_dates,sub6_dates,sub1_per,sub2_per,sub3_per,sub4_per,sub5_per,sub6_per,total_per FROM student_table WHERE class=%s",(classname3,))
            excel_result=mycursor.fetchall()
            excel_nae="C:\\Users\\robin\\OneDrive\\Desktop\\"+self.excel_name.get()+".csv"
            with open (excel_nae,'w',newline='') as f:
                field_names=['Roll no.','Name','class','DLCA ','DSGT','CG','DS','OOPJ','MATHS','DLCA per','DSGT per','CG per','DS per','OOPJ per','MATHS per','total per']
                thewriter=csv.DictWriter(f,fieldnames=field_names)
                thewriter.writeheader()

                for excel in excel_result:
                    thewriter.writerow({'Roll no.':excel[0],'Name':excel[1],'class':excel[2],'DLCA ':excel[3],'DSGT':excel[4],'CG':excel[5],'DS':excel[6],'OOPJ':excel[7],'MATHS':excel[8],'DLCA per':excel[9],'DSGT per':excel[10],'CG per':excel[11],'DS per':excel[12],'OOPJ per':excel[13],'MATHS per':excel[14],'total per':excel[15]})
                messagebox.showinfo("SUCCESS","Succesfully Saved ",parent=self.root6)
                self.root12.destroy()

    def cutoff_marks(self,result,classname2):
        if int(self.fram2_entry.get()) > 100 :
            messagebox.showerror("ERROR","Enter Valid percentage",parent=self.root7)
        else:
            self.export_to_excel(classname2)
            self.date_box1.delete(0,END)
            if result=='dlca':
                mycursor.execute("SELECT name ,FROM student_table WHERE class=%s and sub1_per <=%s",(classname2,self.fram2_entry.get(),))
                ans=mycursor.fetchall()
                if ans==None:
                    messagebox.showerror("ERROR","Try different Cut off",parent=self.root7)
                else:
                    for i in range(0,len(ans)):
                        ans2=ans[i]
                        ans3=ans2[0]
                        self.date_box1.insert(END,ans3)
            if result=='dsgt':
                mycursor.execute("SELECT name FROM student_table WHERE class=%s and sub2_per <=%s",(classname2,self.fram2_entry.get(),))
                ans=mycursor.fetchall()
                if ans==None:
                    messagebox.showerror("ERROR","Try different Cut off",parent=self.root7)
                else:
                    for i in range(0,len(ans)):
                        ans2=ans[i]
                        ans3=ans2[0]
                        self.date_box1.insert(END,ans3)
            if result=='cg':
                mycursor.execute("SELECT name FROM student_table WHERE class=%s and sub3_per <=%s",(classname2,self.fram2_entry.get(),))
                ans=mycursor.fetchall()
                if ans==None:
                    messagebox.showerror("ERROR","Try different Cut off",parent=self.root7)
                else:
                    for i in range(0,len(ans)):
                        ans2=ans[i]
                        ans3=ans2[0]
                        self.date_box1.insert(END,ans3)
            if result=='ds':
                mycursor.execute("SELECT name FROM student_table WHERE class=%s and sub4_per <=%s",(classname2,self.fram2_entry.get(),))
                ans=mycursor.fetchall()
                if ans==None:
                    messagebox.showerror("ERROR","Try different Cut off",parent=self.root7)
                else:
                    for i in range(0,len(ans)):
                        ans2=ans[i]
                        ans3=ans2[0]
                        self.date_box1.insert(END,ans3)
            if result=='oopj':
                mycursor.execute("SELECT name FROM student_table WHERE class=%s and sub5_per <=%s",(classname2,self.fram2_entry.get(),))
                ans=mycursor.fetchall()
                if ans==None:
                    messagebox.showerror("ERROR","Try different Cut off",parent=self.root7)
                else:
                    for i in range(0,len(ans)):
                        ans2=ans[i]
                        ans3=ans2[0]
                        self.date_box1.insert(END,ans3)
            if result=='ceem3':
                mycursor.execute("SELECT name FROM student_table WHERE class=%s and sub6_per <=%s",(classname2,self.fram2_entry.get(),))
                ans=mycursor.fetchall()
                if ans==None:
                    messagebox.showerror("ERROR","Try different Cut off",parent=self.root7)
                else:
                    for i in range(0,len(ans)):
                        ans2=ans[i]
                        ans3=ans2[0]
                        self.date_box1.insert(END,ans3)

    def get_today(self):
        self.root11=Toplevel()
        self.root11.geometry("230x210+440+275")
        self.root11.focus_force()
        self.root11.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root11.iconphoto(False,icon_photo)
        self.root11.config(background="white")
        self.root11.title("DATE")
        self.date_entry.config(state='normal')
        today=date.today()
        today=str(today)
        self.arr=list(map(int,today.split("-")))
        self.cal=Calendar(self.root11,selectmode="day",year=self.arr[0],month=self.arr[1],day=self.arr[2])
        self.cal.pack()
        get_day=Button(self.root11,text="Get Date",bg="White",command=self.grab_date)
        get_day.pack()

    def grab_date(self):
        self.date_entry.delete(0,END)
        arr2=list(map(int,self.cal.get_date().split("/")))
        if(self.arr[0]>=arr2[2]):
            if (self.arr[1]>=arr2[0]):
                if (self.arr[2]>=arr2[1]):
                    self.date_entry.insert(0,self.cal.get_date())
                else:
                    messagebox.showerror("ERROR","SELECT A VALID DATE",parent=self.root11)
            else:
                messagebox.showerror("ERROR","SELECT A VALID DATE",parent=self.root11)
        else:
            messagebox.showerror("ERROR","SELECT A VALID DATE",parent=self.root11)
                    
                
        print(arr2[0])
        print(arr2[1])
        print(arr2[2])
        print(self.cal.get_date())
       
        
        self.root11.destroy()
        self.date_entry.config(state='readonly')  

    def search_by_roll(self,result,classname2):
        self.date_box.delete(0,END)
        self.fram1_entry1.delete(0,END)
        self.fram1_entry2.delete(0,END)
        mycursor.execute("SELECT * FROM student_table WHERE roll_no=%s and class=%s",(self.fram1_entry.get(),classname2,))
        ans=mycursor.fetchone()
        if ans==None:
            messagebox.showerror("ERROR","Roll no. does not Exist",parent=self.root7)
        else:
            if result=='dlca':
                mycursor.execute("SELECT sub1_dates,sub1_a,sub1_t FROM student_table WHERE roll_no=%s and class=%s",(self.fram1_entry.get(),classname2))
                key=mycursor.fetchone()
                self.fram1_entry1.insert(0,key[1])
                self.fram1_entry2.insert(0,int(key[2])-int(key[1]))
                key1=''.join(key[0])
                key1=list(map(str,key1.split(",")))
                for r in key1:
                   self.date_box.insert(END,r)

            if result=='dsgt':
                mycursor.execute("SELECT sub2_dates,sub2_a,sub2_t FROM student_table WHERE roll_no=%s and class=%s",(self.fram1_entry.get(),classname2))
                key=mycursor.fetchone()
                self.fram1_entry1.insert(0,key[1])
                self.fram1_entry2.insert(0,int(key[2])-int(key[1]))
                key1=''.join(key[0])
                key1=list(map(str,key1.split(",")))
                for r in key1:
                   self.date_box.insert(END,r)

            if result=='cg':
                mycursor.execute("SELECT sub3_dates,sub3_a,sub3_t FROM student_table WHERE roll_no=%s and class=%s",(self.fram1_entry.get(),classname2))
                key=mycursor.fetchone()
                self.fram1_entry1.insert(0,key[1])
                self.fram1_entry2.insert(0,int(key[2])-int(key[1]))
                key1=''.join(key[0])
                key1=list(map(str,key1.split(",")))
                for r in key1:
                   self.date_box.insert(END,r)
            
            if result=='ds':
                mycursor.execute("SELECT sub4_dates,sub4_a,sub4_t FROM student_table WHERE roll_no=%s and class=%s",(self.fram1_entry.get(),classname2))
                key=mycursor.fetchone()
                self.fram1_entry1.insert(0,key[1])
                self.fram1_entry2.insert(0,int(key[2])-int(key[1]))
                key1=''.join(key[0])
                key1=list(map(str,key1.split(",")))
                for r in key1:
                   self.date_box.insert(END,r)
        
            if result=='oopj':
                mycursor.execute("SELECT sub5_dates,sub5_a,sub5_t FROM student_table WHERE roll_no=%s and class=%s",(self.fram1_entry.get(),classname2))
                key=mycursor.fetchone()
                self.fram1_entry1.insert(0,key[1])
                self.fram1_entry2.insert(0,int(key[2])-int(key[1]))
                key1=''.join(key[0])
                key1=list(map(str,key1.split(",")))
                for r in key1:
                   self.date_box.insert(END,r)
        
            if result=='ceem3':
                mycursor.execute("SELECT sub6_dates,sub6_a,sub6_t FROM student_table WHERE roll_no=%s and class=%s",(self.fram1_entry.get(),classname2))
                key=mycursor.fetchone()
                self.fram1_entry1.insert(0,key[1])
                self.fram1_entry2.insert(0,int(key[2])-int(key[1]))
                key1=''.join(key[0])
                key1=list(map(str,key1.split(",")))
                for r in key1:
                   self.date_box.insert(END,r)
     

    def save_it(self,result,classname2):
        if self.date_entry.get() !="":
            if result=='dlca':
                mycursor.execute("SELECT MAX(sub1_t) FROM student_table WHERE class=%s",(classname2,))
                ans=mycursor.fetchall()
                for i in ans:
                    ans1=''.join(i)
                    ans1=int(ans1)+1
                    mycursor.execute("UPDATE student_table SET sub1_t=%s WHERE class =%s",(ans1,classname2,))
                    mydb.commit()
            if result=='dsgt':
                mycursor.execute("SELECT MAX(sub2_t) FROM student_table WHERE class=%s",(classname2,))
                ans=mycursor.fetchall()
                for i in ans:
                    ans1=''.join(i)
                    ans1=int(ans1)+1
                    mycursor.execute("UPDATE student_table SET sub2_t=%s WHERE class =%s",(ans1,classname2,))
                    mydb.commit()
            if result=='cg':
                mycursor.execute("SELECT MAX(sub3_t) FROM student_table WHERE class=%s",(classname2,))
                ans=mycursor.fetchall()
                for i in ans:
                    ans1=''.join(i)
                    ans1=int(ans1)+1
                    mycursor.execute("UPDATE student_table SET sub3_t=%s WHERE class =%s",(ans1,classname2,))
                    mydb.commit()
            if result=='ds':
                mycursor.execute("SELECT MAX(sub4_t) FROM student_table WHERE class=%s",(classname2,))
                ans=mycursor.fetchall()
                for i in ans:
                    ans1=''.join(i)
                    ans1=int(ans1)+1
                    mycursor.execute("UPDATE student_table SET sub4_t=%s WHERE class =%s",(ans1,classname2,))
                    mydb.commit()
            if result=='oopj':
                mycursor.execute("SELECT MAX(sub5_t) FROM student_table WHERE class=%s",(classname2,))
                ans=mycursor.fetchall()
                for i in ans:
                    ans1=''.join(i)
                    ans1=int(ans1)+1
                    mycursor.execute("UPDATE student_table SET sub5_t=%s WHERE class =%s",(ans1,classname2,))
                    mydb.commit()
            if result=='ceem3':
                mycursor.execute("SELECT MAX(sub6_t) FROM student_table WHERE class=%s",(classname2,))
                ans=mycursor.fetchall()
                for i in ans:
                    ans1=''.join(i)
                    ans1=int(ans1)+1
                    mycursor.execute("UPDATE student_table SET sub6_t=%s WHERE class =%s",(ans1,classname2,))
                    mydb.commit()  
            messagebox.showinfo("Succesful","saved succesfully",parent=self.root7)
            try:
                if(self.root10):
                    self.root10.destroy()
            except AttributeError:
                pass
            
        else:
            messagebox.showerror("ERROR"," SELECT DATE",parent=self.root7)
          

    def add_attendece(self,result,classname2):
        if self.date_entry.get()!="":
            arr=list(map(int,self.entry.get().split()))
            error_list=[]
            flag=0
            flag2=0
            flag3=0
            if self.entry.get()=="":
                flag2=1
            if self.entry.get()!="":
                for i in range(len(arr)): 
                    for i1 in range(len(arr)): 
                        if i != i1: 
                            if arr[i] == arr[i1]: 
                                flag = 1
                            else:
                                flag=0
            if flag!=1 :
                for i in arr:
                    mycursor.execute("SELECT * FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                    detail=mycursor.fetchone()
                    if detail==None:
                        error_list.append(i)
                        break
                    else:
                        if result=='dlca':
                            mycursor.execute("SELECT sub1_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                            key=mycursor.fetchone()
                            key=''.join(key)
                            if key.count(self.date_entry.get())==0:
                                mycursor.execute("SELECT sub1_a FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans=mycursor.fetchone()
                                ans1=''.join(ans)
                                ans1=int(ans1)+1
                                mycursor.execute("UPDATE student_table SET sub1_a=%s WHERE roll_no=%s and class =%s",(ans1,i,classname2,))
                                #------------to add dates
                                mycursor.execute("SELECT sub1_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans2=mycursor.fetchone()
                                ans3=''.join(ans2)
                                if(len(ans3)>=331):
                                    ans3='0'
                                if ans3=='0':
                                    ans3=self.date_entry.get()
                                else:
                                    ans3=str(ans3)+","+self.date_entry.get()
                                mycursor.execute("UPDATE student_table SET sub1_dates=%s WHERE roll_no=%s and class =%s",(ans3,i,classname2,))
                                mydb.commit()
                            else:
                                flag3=1
                            
                        if result=='dsgt':
                            mycursor.execute("SELECT sub2_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                            key=mycursor.fetchone()
                            key=''.join(key)
                            if key.count(self.date_entry.get())==0:
                                mycursor.execute("SELECT sub2_a FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans=mycursor.fetchone()
                                ans1=''.join(ans)
                                ans1=int(ans1)+1
                                mycursor.execute("UPDATE student_table SET sub2_a=%s WHERE roll_no=%s and class =%s",(ans1,i,classname2,))
                                #------------to add dates
                                mycursor.execute("SELECT sub2_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans2=mycursor.fetchone()
                                ans3=''.join(ans2)
                                if(len(ans3)>=331):
                                    ans3='0'
                                if ans3=='0':
                                    ans3=self.date_entry.get()
                                else:
                                    ans3=str(ans3)+","+self.date_entry.get()
                                mycursor.execute("UPDATE student_table SET sub2_dates=%s WHERE roll_no=%s and class =%s",(ans3,i,classname2,))
                                mydb.commit()
                                #print(ans1)
                            else:
                                flag3=1
                            

                        if result=='cg':
                            mycursor.execute("SELECT sub3_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                            key=mycursor.fetchone()
                            key=''.join(key)
                            if key.count(self.date_entry.get())==0:
                                mycursor.execute("SELECT sub3_a FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans=mycursor.fetchone()
                                ans1=''.join(ans)
                                ans1=int(ans1)+1
                                mycursor.execute("UPDATE student_table SET sub3_a=%s WHERE roll_no=%s and class =%s",(ans1,i,classname2,))
                                #------------to add dates
                                mycursor.execute("SELECT sub3_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans2=mycursor.fetchone()
                                ans3=''.join(ans2)
                                if(len(ans3)>=331):
                                    ans3='0'
                                if ans3=='0':
                                    ans3=self.date_entry.get()
                                else:
                                    ans3=str(ans3)+","+self.date_entry.get()
                                mycursor.execute("UPDATE student_table SET sub3_dates=%s WHERE roll_no=%s and class =%s",(ans3,i,classname2,))
                                mydb.commit()
                                #print(ans1)
                            else:
                                flag3=1
                            

                        if result=='ds':
                            mycursor.execute("SELECT sub4_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                            key=mycursor.fetchone()
                            key=''.join(key)
                            if key.count(self.date_entry.get())==0:
                                mycursor.execute("SELECT sub4_a FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans=mycursor.fetchone()
                                ans1=''.join(ans)
                                ans1=int(ans1)+1
                                mycursor.execute("UPDATE student_table SET sub4_a=%s WHERE roll_no=%s and class =%s",(ans1,i,classname2,))
                                #------------to add dates
                                mycursor.execute("SELECT sub4_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans2=mycursor.fetchone()
                                ans3=''.join(ans2)
                                if(len(ans3)>=331):
                                    ans3='0'
                                if ans3=='0':
                                    ans3=self.date_entry.get()
                                else:
                                    ans3=str(ans3)+","+self.date_entry.get()
                                mycursor.execute("UPDATE student_table SET sub4_dates=%s WHERE roll_no=%s and class =%s",(ans3,i,classname2,))
                                mydb.commit()
                                #print(ans1)
                            else:
                                flag3=1
                           

                        if result=='oopj':
                            mycursor.execute("SELECT sub5_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                            key=mycursor.fetchone()
                            key=''.join(key)
                            if key.count(self.date_entry.get())==0:
                                mycursor.execute("SELECT sub5_a FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans=mycursor.fetchone()
                                ans1=''.join(ans)
                                ans1=int(ans1)+1
                                mycursor.execute("UPDATE student_table SET sub5_a=%s WHERE roll_no=%s and class =%s",(ans1,i,classname2,))
                                #------------to add dates
                                mycursor.execute("SELECT sub5_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans2=mycursor.fetchone()
                                ans3=''.join(ans2)
                                if(len(ans3)>=331):
                                    ans3='0'
                                if ans3=='0':
                                    ans3=self.date_entry.get()
                                else:
                                    ans3=str(ans3)+","+self.date_entry.get()
                                mycursor.execute("UPDATE student_table SET sub5_dates=%s WHERE roll_no=%s and class =%s",(ans3,i,classname2,))
                                mydb.commit()
                                #print(ans1)
                            else:
                                flag3=1
                           

                        if result=='ceem3':
                            mycursor.execute("SELECT sub6_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                            key=mycursor.fetchone()
                            key=''.join(key)
                            if key.count(self.date_entry.get())==0:
                                mycursor.execute("SELECT sub6_a FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans=mycursor.fetchone()
                                ans1=''.join(ans)
                                ans1=int(ans1)+1
                                mycursor.execute("UPDATE student_table SET sub6_a=%s WHERE roll_no=%s and class =%s",(ans1,i,classname2,))
                                #------------to add dates
                                mycursor.execute("SELECT sub6_dates FROM student_table WHERE roll_no=%s and class=%s",(i,classname2,))
                                ans2=mycursor.fetchone()
                                ans3=''.join(ans2)
                                if(len(ans3)>=331):
                                    ans3='0'
                                if ans3=='0':
                                    ans3=self.date_entry.get()
                                else:
                                    ans3=str(ans3)+","+self.date_entry.get()
                                mycursor.execute("UPDATE student_table SET sub6_dates=%s WHERE roll_no=%s and class =%s",(ans3,i,classname2,))
                                mydb.commit()
                                #print(ans1)
                            else:
                                flag3=1

            self.root10=Toplevel()
            self.root10.geometry("250x150+400+300")
            self.root10.focus_force()
            self.root10.grab_set()
            icon_photo=PhotoImage(file='R1.png')
            self.root10.iconphoto(False,icon_photo)
            self.root10.config(background="white")       

            if(len(error_list)!=0):
                self.root10.title("ERROR")
                key=str(error_list).replace("["," ").replace("]"," ")    
                error_label=Label(self.root10,text="Roll No. "+key+ " does Not Exist\n " ,bg="White")
                error_label.pack(pady=20)

            elif(flag==1):
                self.root10.title("ERROR")
                error_label=Label(self.root10,text="Enter Each roll no only once" ,bg="White")
                error_label.pack(pady=20)
            elif(flag2==1):
                self.root10.title("ERROR")
                error_label=Label(self.root10,text="Enter Roll no. first" ,bg="White")
                error_label.pack(pady=20)
            elif(flag3==1):
                self.root10.title("ERROR")
                error_label=Label(self.root10,text="Already marked absent for the day" ,bg="White")
                error_label.pack(pady=20)
            else:
                self.root10.title("Success")
                error_label=Label(self.root10,text="please click Save Button" ,bg="White")
                error_label.pack(pady=20)

                my_img39=Image.open('R39.png')
                resized39=my_img39.resize((130,50),Image.ANTIALIAS )
                self.img39=ImageTk.PhotoImage(resized39)    
                add_button=Button(self.root10,image=self.img39,bg="WHITE",bd=0,activebackground="White",command=lambda :self.save_it(result,classname2))
                add_button.pack(pady=25)
                
            self.entry.delete(0,END)
        else:
            messagebox.showerror("ERROR","Please Select A Date",parent=self.root7)
        
    #def add_date(self,result,classname2)
    def export_to_excel(self,classname3):
        mycursor.execute("SELECT roll_no FROM student_table WHERE class=%s",(classname3,))
        all_result=mycursor.fetchall()
        for i in range(0,len(all_result)):
            roll=all_result[i]
            mycursor.execute("SELECT * FROM student_table WHERE roll_no=%s and class=%s",(roll[0],classname3,))
            store=mycursor.fetchall()
            store2=store[0]
            try:
                per1=((int(store2[5])-int(store2[4]))/int(store2[5]))*100
                mycursor.execute("UPDATE student_table SET sub1_per=%s WHERE roll_no=%s and class=%s",(per1,roll[0],classname3,))
                self.total_marks(roll[0],classname3)
                mydb.commit()
            except ZeroDivisionError:
                pass

            try:
                per2=((int(store2[8])-int(store2[7]))/int(store2[8]))*100
                mycursor.execute("UPDATE student_table SET sub2_per=%s WHERE roll_no=%s and class=%s",(per2,roll[0],classname3,))
                self.total_marks(roll[0],classname3)
                mydb.commit()
            except ZeroDivisionError:
                pass

            try:
                per3=((int(store2[11])-int(store2[10]))/int(store2[11]))*100
                mycursor.execute("UPDATE student_table SET sub3_per=%s WHERE roll_no=%s and class=%s",(per3,roll[0],classname3,))
                self.total_marks(roll[0],classname3)
                mydb.commit()
            except ZeroDivisionError:
                pass

            try:
                per4=((int(store2[14])-int(store2[13]))/int(store2[14]))*100
                mycursor.execute("UPDATE student_table SET sub4_per=%s WHERE roll_no=%s and class=%s",(per4,roll[0],classname3,))
                self.total_marks(roll[0],classname3)
                mydb.commit()
            except ZeroDivisionError:
                pass

            try:
                per5=((int(store2[17])-int(store2[16]))/int(store2[17]))*100
                mycursor.execute("UPDATE student_table SET sub5_per=%s WHERE roll_no=%s and class=%s",(per5,roll[0],classname3,))
                self.total_marks(roll[0],classname3)
                mydb.commit()
            except ZeroDivisionError:
                pass
                
            try:
                per6=((int(store2[20])-int(store2[19]))/int(store2[20]))*100
                mycursor.execute("UPDATE student_table SET sub6_per=%s WHERE roll_no=%s and class=%s",(per6,roll[0],classname3,))
                self.total_marks(roll[0],classname3)
                mydb.commit()
            except ZeroDivisionError:
                pass

            
            
                
    def total_marks(self,roll,classname3):
        mycursor.execute("SELECT sub1_per,sub2_per,sub3_per,sub4_per,sub5_per,sub6_per FROM student_table WHERE roll_no=%s and class=%s",(roll,classname3,))
        anskey=mycursor.fetchall()
        keys=anskey[0]
        total_score=(keys[0]+keys[1]+keys[2]+keys[3]+keys[4]+keys[5])/6
        mycursor.execute("UPDATE student_table SET total_per=%s WHERE roll_no=%s and class=%s",(total_score,roll,classname3,))
    def add_students(self,classname3):
        self.root8=Toplevel()
        self.root8.title("Add Students")
        self.root8.geometry("1630x850")
        self.root8.focus_force()
        self.root8.grab_set()
        icon_photo=PhotoImage(file='R1.png') 
        self.root8.iconphoto(False,icon_photo)
        self.root8.config(background="white")

        #--------------------title_frame------------------
        add_s_frame=Frame(self.root8,background='#F9EBEA')
        add_s_frame.place(x=0,y=0,relwidth=1,relheight=.15)

        l1=Label(add_s_frame,text="ADD STUDENTS",background='#F9EBEA',font=('Consolas',44))
        l1.place(x=550,y=10)
        #------------------------student detail frame--------------------------------
        manage_s_frame=Frame(self.root8,bg="pink")
        manage_s_frame.place(x=650,y=130,width=860,height=650)

        detail_s_frame=Frame(self.root8,bg="pink",)
        detail_s_frame.place(x=20,y=130,width=570,height=650)

        #------------------adding details---------------------------------
        s_first_name=Label(detail_s_frame,text="Name :",background="pink",foreground="black",font=16)
        s_first_name.grid(row=0,column=0,padx=30,pady=10,sticky=W)
        self.e1=Entry(detail_s_frame,width=40)
        self.e1.grid(row=0,column=1,padx=20,pady=10,sticky=W)
        self.e1.focus()

        s_rollno=Label(detail_s_frame,text="Roll number :",background="pink",foreground="black",font=16)
        s_rollno.grid(row=2,column=0,padx=30,pady=10,sticky=W)
        self.e2=Entry(detail_s_frame,width=40)
        self.e2.grid(row=2,column=1,padx=20,pady=10,sticky=W)
        
        s_email=Label(detail_s_frame,text="Email ID :",background="pink",foreground="black",font=16)
        s_email.grid(row=3,column=0,padx=30,pady=10,sticky=W)
        self.e3=Entry(detail_s_frame,width=40)
        self.e3.grid(row=3,column=1,padx=20,pady=10,sticky=W)

        #s_class=Label(detail_s_frame,text="Class Name :",background="pink",foreground="black",font=16)
        #s_class.grid(row=4,column=0,padx=30,pady=10,sticky=W)
        #self.e4=Entry(detail_s_frame,width=40)
        #self.e4.grid(row=4,column=1,padx=20,pady=10,sticky=W)

        #---------button frame------------------
        btn_frame=Frame(detail_s_frame,bg="pink")
        btn_frame.place(x=10,y=570,width=550,height=50)
        #-------------adding buttons----------
        b1=Button(btn_frame,text="Add",background="pink",cursor='hand2',command=lambda: self.add(classname3))
        b1.grid(row=0,column=0,padx=30,ipadx=20)
        b2=Button(btn_frame,text="Update",background="pink",cursor='hand2',command=lambda: self.update_value(classname3))
        b2.grid(row=0,column=1,padx=30,ipadx=20)
        b3=Button(btn_frame,text="Delete",background="pink",cursor='hand2',command=lambda: self.delete(classname3))
        b3.grid(row=0,column=2,padx=30,ipadx=20)
        b4=Button(btn_frame,text="Clear",background="pink",cursor='hand2',command=self.clear3)
        b4.grid(row=0,column=3,padx=30,ipadx=20)

        #--------------search frame----------------------
        search_frame=Frame(manage_s_frame,bg="Pink")
        search_frame.place(x=10,y=10,width=840,height=50)
        #----------------adding search options-------------
        search_label=Label(search_frame,text="Search By",background="pink",foreground="Black",font=16)
        search_label.grid(row=0,column=0,padx=30,pady=10,sticky=W)
        self.e8=ttk.Combobox(search_frame,width=25,values=('select any one','name','Roll no.'),state='readonly')
        self.e8.grid(row=0,column=1,padx=20,pady=10,sticky=W)
        self.e8.current(0)
        self.e9=Entry(search_frame,width=25)
        self.e9.grid(row=0,column=2,padx=20,pady=10,sticky=W)
        b5=Button(search_frame,text="Search",background="Pink",cursor='hand2',command=lambda: self.search_student(classname3))
        b5.grid(row=0,column=3,padx=30,ipadx=20)
        b6=Button(search_frame,text="Show All",background="Pink",cursor='hand2',command=lambda: self.show_all(classname3))
        b6.grid(row=0,column=4,padx=30,ipadx=20)
        #--------------list frame-------------------------------
        list_frame=Frame(manage_s_frame,bg="white")
        list_frame.place(x=20,y=70,width=820,height=500)

        #--------------------scroll bars---------------------------
        scroll_x=Scrollbar(list_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(list_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(list_frame,columns=('first_name','roll','email'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("first_name",text=" Name")
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("email",text="Email ID")
        #self.student_table.heading("class",text="Div")
        self.student_table['show']='headings'
        self.student_table.column("first_name",width=200)
        self.student_table.column("roll",width=100)
        self.student_table.column("email",width=200)
       # self.student_table.column("class",width=100)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_all(classname3)
        
        self.student_table.pack(fill=BOTH,expand=1)
    def add(self,classname3):
        if(self.e1.get()=="" or self.e2.get()=="" or self.e3.get()=="" ):
            messagebox.showerror("ERROR","enter all details",parent=self.root8)
        else:
            mycursor.execute("SELECT * FROM student_table WHERE roll_no=%s and class=%s",(self.e2.get(),classname3,))
            detail=mycursor.fetchone()
            if detail!=None:
                messagebox.showerror("ERROR","Roll NO. Already Exists",parent=self.root8)
            else:
                sql_formula_5="INSERT INTO student_table(name,roll_no,email,class) VALUES(%s,%s,%s,%s)"
                key5=(self.e1.get(),self.e2.get(),self.e3.get(),classname3)
                mycursor.execute(sql_formula_5,key5)
                mydb.commit()
                self.fetch_all(classname3)
                self.clear3()

    def fetch_all(self,classname3):
        mycursor.execute("SELECT name,roll_no,email FROM student_table WHERE class=%s ORDER BY roll_no",(classname3,))
        rows=mycursor.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)  
        

    def get_cursor(self,event):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.e1.insert(0,row[0])
        self.e2.insert(0,row[1]) 
        self.e3.insert(0,row[2]) 
        #self.e4.insert(0,row[3])  

    def update_value(self,classname3):
        mycursor.execute("UPDATE student_table SET name=%s,email=%s WHERE roll_no=%s and class=%s",(
            self.e1.get(),
            self.e3.get(),
            self.e2.get(),
            classname3,))
        mydb.commit()
        self.fetch_all(classname3)
        self.clear3()

    def delete(self,classname3):
        mycursor.execute("DELETE FROM student_table WHERE roll_no=%s and class=%s",(self.e2.get(),classname3,))
        mydb.commit()
        self.fetch_all(classname3)
        self.clear3()
    
    def search_student(self,classname3):
        sql=""
        selected=self.e8.get()
        if selected=="select any one":
            messagebox.showerror("ERROR","select any one",parent=self.root8)
        if selected=="name":
            sql="SELECT name,roll_no,email FROM student_table WHERE name= %s and class=%s"
        if selected=="Roll no.":
           sql="SELECT name,roll_no,email FROM student_table WHERE roll_no= %s and class=%s"
        searched=self.e9.get()
        name=(searched,classname3)
        result=mycursor.execute(sql,name)
        result=mycursor.fetchall()

        if not result:
            messagebox.showerror("ERROR","RECORD NOT FOUND",parent=self.root8)
        else:
            self.student_table.delete(*self.student_table.get_children())
            for row in result:
                self.student_table.insert('',END,values=row)
        
        self.e8.set("select any one")
        self.e9.delete(0,END)

    def show_all(self,classname3):
        self.fetch_all(classname3)

    def clear3(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)    
        #self.e4.delete(0,END)

    def create_new_class(self):
        self.root4=Toplevel()
        self.root4.title("CREATE NEW CLASS")
        self.root4.geometry("500x400+800+200")
        self.root4.focus_force()
        self.root4.grab_set()
        icon_photo=PhotoImage(file='R1.png')
        self.root4.iconphoto(False,icon_photo)
        self.root4.config(background="white")

        new_class_frame=Frame(self.root4,background='#F9EBEA')
        new_class_frame.place(x=0,y=0,relwidth=1,relheight=.15)
        l3=Label(new_class_frame,text="NEW CLASS",background='#F9EBEA',font=('Consolas',24))
        l3.place(x=170,y=11)

        new_class_name=Label(self.root4,text="CLASS NAME ",font=("Dubai Medium",12),bg="White")
        new_class_name.place(x=10,y=80)
        self.class_name_entry=Entry(self.root4,width=40,font=("Dubai Medium",11),bg='#AED6F1')
        self.class_name_entry.place(x=140,y=80,height=30)

        new_branch_name=Label(self.root4,text="BRANCH ",font=("Dubai Medium",12),bg="White")
        new_branch_name.place(x=10,y=120)
        self.branch_entry=ttk.Combobox(self.root4,values=('select a branch','COMPUTER ENGINEERING','INFORMATION TECHNOLOGY',"MECHANICAL ENGINEERING","AUTOMOBILE ENGINEERING"),font=(11),state='readonly',width=27)
        self.branch_entry.place(x=140,y=120,height=30)
        self.branch_entry.current(0)

        new_sem_name=Label(self.root4,text="SEMESTER ",font=("Dubai Medium",12),bg="White")
        new_sem_name.place(x=10,y=160)
        self.sem_entry=ttk.Combobox(self.root4,values=('select semester',"III","IV","V","VI","VII","VIII"),font=(11),state='readonly',width=27)
        self.sem_entry.place(x=140,y=160,height=30)
        self.sem_entry.current(0)

        new_cc_name=Label(self.root4,text="CC ",font=("Dubai Medium",12),bg="White")
        new_cc_name.place(x=10,y=200)
        self.cc_entry=Entry(self.root4,width=40,font=("Dubai Medium",11),bg='#AED6F1')
        self.cc_entry.place(x=140,y=200,height=30)

        new_suggestion=Label(self.root4,text="Please a enter a unique class name  try CE3A",fg="blue",font=("Dubai Medium",9),bg="White")
        new_suggestion.place(x=100,y=370)
        
        #---------------------buttons--------------------------------
        my_img17=Image.open('R21.png')
        resized17=my_img17.resize((120,40),Image.ANTIALIAS )
        self.img17=ImageTk.PhotoImage(resized17)  
        save_button=Button(self.root4,image=self.img17,bd=0,bg="White",cursor='hand2',activebackground="White",command=self.get_values_new_class)
        save_button.place(x=180,y=300)
    
    def get_values_new_class(self):
        if self.class_name_entry.get()=="" or self.branch_entry.get()=="select a branch" or self.sem_entry.get()=="select semester" or self.cc_entry.get()=="":
            messagebox.showerror("ERROR","ENTER ALL DETAILS",parent=self.root4)
        else:
            mycursor.execute("SELECT * FROM class  WHERE class_name=%s",(self.class_name_entry.get(),))
            class_exist=mycursor.fetchone()
            if class_exist!=None:
                messagebox.showerror("ERROR","CLASS NAME ALREADY EXISTS",parent=self.root4)
            else:
                sql_formula_2="INSERT INTO class(class_name,branch,sem,cc) VALUES(%s,%s,%s,%s)"
                keys2=(self.class_name_entry.get(),self.branch_entry.get(),self.sem_entry.get(),self.cc_entry.get())
                mycursor.execute(sql_formula_2,keys2)
                mydb.commit()
                messagebox.showinfo("SUCCESS","REGISTRATION SUCCESFULL ",parent=self.root4)
                self.clear2()
                self.root4.destroy()

                        
    def clear2(self):
        self.class_name_entry.delete(0,END)
        self.branch_entry.set("select a branch") 
        self.sem_entry.set("select semester")
        self.cc_entry.delete(0,END)

       
        
root=Tk()

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Robin@2001",
    database="attendence"
)
mycursor=mydb.cursor()
obj=Student(root)
root.mainloop()