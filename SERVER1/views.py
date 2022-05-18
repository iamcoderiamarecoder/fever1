
#this project might have been started on 2021-01-21

from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import authenticate,login,logout

from .decorators import authenticated_user,allowed_user

from django.contrib.auth.models import User,Group

import datetime

from .models import class_1,class_1_student
from .models import class_2,class_2_student
from .models import class_3,class_3_student
from .models import class_4,class_4_student
from .models import class_5,class_5_student
from .models import class_6,class_6_student
from .models import class_7,class_7_student
from .models import class_8,class_8_student
from .models import class_9,class_9_student
from .models import class_10,class_10_student

from .models import Notice_Database
from .models import About
from .models import Blog

# Create your views here.
#we have use some global variables at first i made each global variable for each function like roll_no9="",roll_no10=""
#but for date iam making one global variable and altering it from every function

query_date="" #[you might be wondering why  are even taking the date in ledger ,its for to get(name) ]

def index(request):
   
    return render(request,"index.html")

def notice(request):
    notice_from_db= Notice_Database.objects.all()

    param= {"notice":notice_from_db}


    return render(request,"notice.html",param)


def blog_sample(request):
    if request.method == "POST":
        content= request.POST.get("whatsonyourmind")
        writer= str(request.user)
        b_date= str(datetime.datetime.today())  #for making date in right format
        if writer != "AnonymousUser":
            blog_add=Blog(date=b_date,writer=writer,content=content)
            blog_add.save()
     
    blog_info = Blog.objects.all()
    
    param = {"blog_info":blog_info}
    return render(request,"blog_sample.html",param)


def blog_delete(request):
    if request.method == "POST":

        user=str(request.user)
        id=request.POST.get("id")
        
        writer=Blog.objects.get(id=id)
        if user == str(writer):
            print(user)
            writer.delete()
        
    return redirect("/blog_sample")

@authenticated_user
def events(request):
    return render(request,"events.html")


def about(request):
    about_obj = About.objects.all()
    first_obj=about_obj[0]
    title=first_obj.title
    about_desc= first_obj.about_desc
    param= {"title":title ,"about_desc":about_desc}
    return render(request,"about.html",param)


@allowed_user(allowed_roles=["teachers","admin"])
def classes_to_mark(request):
    return render(request,"classes_to_mark.html")

@allowed_user(allowed_roles=["teachers","admin"])
def classes_to_query(request):
    return render(request,"classes_to_query.html")

@authenticated_user#[this is a custom decorator that stops logged in user to go to login page]
def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username,password=password)
        

        if user != None:
            login(request,user)
            print("worked")
            return redirect("/")
        else:
            return redirect("/login_page")

        print(password)
        print(email)
    return render(request,"login.html")


def logout_page(request):
    
    logout(request)
    print("logut sussesful")
    return redirect("/")





#===============================class_1_attendance_query======================================================
roll_no1=""
@allowed_user(allowed_roles=["class_teacher_1", "admin"])
def class_1_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")   
            global query_date      
            query_date =request.POST.get("query_date","")
            global roll_no1
            roll_no1 = request.POST.get("roll_no","")

            query_process=class_1.objects.get(roll_no=roll_no1,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no1,"class":query_class}
            return render(request,"class_1_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_1_attendance_query.html")



#---------------------class 1 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_1", "admin"])
def attendance_query_ledger_1(request):
        all_objects= class_1.objects.filter(roll_no=roll_no1)


        name= class_1.objects.get(roll_no = roll_no1,date=query_date)
        present_days= class_1.objects.filter(roll_no=roll_no1,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_1.objects.filter(roll_no=roll_no1,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)

#-----------------------------------------------------





#===============================class_2_attendance_query======================================================
roll_no2=""
@allowed_user(allowed_roles=["class_teacher_2", "admin"])
def class_2_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "") 
            global query_date        
            query_date =request.POST.get("query_date","")
            global roll_no2
            roll_no2 = request.POST.get("roll_no","")

            query_process=class_2.objects.get(roll_no=roll_no2,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no2,"class":query_class}
            return render(request,"class_2_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_2_attendance_query.html")


#---------------------class 2 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_2", "admin"])
def attendance_query_ledger_2(request):
        all_objects= class_2.objects.filter(roll_no=roll_no2)

        name= class_2.objects.get(roll_no = roll_no2,date=query_date)
        present_days= class_2.objects.filter(roll_no=roll_no2,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_2.objects.filter(roll_no=roll_no2,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)

#-----------------------------------------------------





#===============================class_3_attendance_query======================================================
roll_no3=""
@allowed_user(allowed_roles=["class_teacher_3", "admin"])
def class_3_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")   
            global query_date      
            query_date =request.POST.get("query_date","")
            global roll_no3
            roll_no3 = request.POST.get("roll_no","")

            query_process=class_3.objects.get(roll_no=roll_no3,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no3,"class":query_class}
            return render(request,"class_3_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_3_attendance_query.html")



#---------------------class 3 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_3", "admin"])
def attendance_query_ledger_3(request):
        all_objects= class_3.objects.filter(roll_no=roll_no3)
     
        name= class_3.objects.get(roll_no = roll_no3,date=query_date)
        present_days= class_3.objects.filter(roll_no=roll_no3,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_3.objects.filter(roll_no=roll_no3,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)

#-----------------------------------------------------





#===============================class_4_attendance_query======================================================
roll_no4=""
@allowed_user(allowed_roles=["class_teacher_4", "admin"])
def class_4_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")
            global query_date         
            query_date =request.POST.get("query_date","")
            global roll_no4
            roll_no4 = request.POST.get("roll_no","")

            query_process=class_4.objects.get(roll_no=roll_no4,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no4,"class":query_class}
            return render(request,"class_4_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_4_attendance_query.html")


#---------------------class 4 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_4", "admin"])
def attendance_query_ledger_4(request):
        all_objects= class_4.objects.filter(roll_no=roll_no4)


        name= class_4.objects.get(roll_no = roll_no4,date=query_date)
        present_days= class_4.objects.filter(roll_no=roll_no4,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_4.objects.filter(roll_no=roll_no4,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)

#-----------------------------------------------------






#===============================class_5_attendance_query======================================================
rollno5=""
@allowed_user(allowed_roles=["class_teacher_5", "admin"])
def class_5_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")
            global query_date      
            query_date =request.POST.get("query_date","")
            global rollno5
            roll_no5 = request.POST.get("roll_no","")

            query_process=class_5.objects.get(roll_no=roll_no5,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no5,"class":query_class}
            return render(request,"class_5_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_5_attendance_query.html")


#---------------------class 5 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_5", "admin"])
def attendance_query_ledger_5(request):
        all_objects= class_5.objects.filter(roll_no=roll_no5)

        name= class_5.objects.get(roll_no = roll_no5,date=query_date)
        present_days= class_5.objects.filter(roll_no=roll_no5,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_5.objects.filter(roll_no=roll_no5,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)

#-----------------------------------------------------




#===============================class_6_attendance_query======================================================
roll_no6 = ""
@allowed_user(allowed_roles=["class_teacher_6", "admin"])
def class_6_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")   
            global query_date
            query_date =request.POST.get("query_date","")
            global roll_no6
            roll_no6 = request.POST.get("roll_no","")

            query_process=class_6.objects.get(roll_no=roll_no6,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no6,"class":query_class}
            return render(request,"class_6_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_6_attendance_query.html")


#---------------------class 6 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_6", "admin"])
def attendance_query_ledger_6(request):
        all_objects= class_6.objects.filter(roll_no=roll_no6)

        name= class_6.objects.get(roll_no = roll_no6,date=query_date)
        present_days= class_6.objects.filter(roll_no=roll_no6,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_6.objects.filter(roll_no=roll_no6,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)
#-----------------------------------------------------






#===============================class_7_attendance_query======================================================
roll_no7=""
@allowed_user(allowed_roles=["class_teacher_7", "admin"])
def class_7_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")  
            global query_date       
            query_date =request.POST.get("query_date","")
            global roll_no7
            roll_no7 = request.POST.get("roll_no","")

            query_process=class_7.objects.get(roll_no=roll_no7,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no7,"class":query_class}
            return render(request,"class_7_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_7_attendance_query.html")


#---------------------class 7 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_7", "admin"])
def attendance_query_ledger_7(request):
        all_objects= class_7.objects.filter(roll_no=roll_no7)
        
        name= class_7.objects.get(roll_no = roll_no7,date=query_date)
        present_days= class_7.objects.filter(roll_no=roll_no7,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_7.objects.filter(roll_no=roll_no7,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)

#-----------------------------------------------------








#===============================class_8_attendance_query======================================================
roll_no8=""
@allowed_user(allowed_roles=["class_teacher_8", "admin"])
def class_8_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")
            global query_date         
            query_date =request.POST.get("query_date","")
            global roll_no8
            roll_no8 = request.POST.get("roll_no","")

            query_process=class_8.objects.get(roll_no=roll_no8,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no8,"class":query_class}
            return render(request,"class_8_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_8_attendance_query.html")




#---------------------class 8 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_8", "admin"])
def attendance_query_ledger_8(request):
        all_objects= class_8.objects.filter(roll_no=roll_no8)


        name= class_8.objects.get(roll_no = roll_no8,date=query_date)
        present_days= class_8.objects.filter(roll_no=roll_no8,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_8.objects.filter(roll_no=roll_no8,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)
#-----------------------------------------------------





#===============================class_9_attendance_query======================================================
roll_no9=""
@allowed_user(allowed_roles=["class_teacher_9", "admin"])
def class_9_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "") 
           # global query_class9     
            global roll_no9 
            global query_date
            query_date =request.POST.get("query_date","")
            roll_no9 = request.POST.get("roll_no","")

            query_process=class_9.objects.get(roll_no=roll_no9,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no9,"class":query_class}
            return render(request,"class_9_attendance_query.html",param) 
            
                                                                                    
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_9_attendance_query.html")
    

#---------------------class 9 ledger-----------------
@allowed_user(allowed_roles=["class_teacher_9", "admin"])
def attendance_query_ledger_9(request):
       
        
        """ IN this down portion we are making the features for attendance ledger
        like name of student present percentage and all other stuff""" 
        
        all_objects= class_9.objects.filter(roll_no=roll_no9)
        
        name= class_9.objects.get(roll_no = roll_no9,date=query_date)
        present_days= class_9.objects.filter(roll_no=roll_no9,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_9.objects.filter(roll_no=roll_no9,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

       
        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)


#-----------------------------------------------------




#===============================class_10_attendance_query======================================================
roll_no10 = ""
@allowed_user(allowed_roles=["class_teacher_10", "admin"])
def class_10_attendance_query(request):
    if request.method == "POST":
        try:
            query_class = request.POST.get("class", "")  
            global query_date       
            query_date =request.POST.get("query_date","")
            global roll_no10
            roll_no10 = request.POST.get("roll_no","")

            query_process=class_10.objects.get(roll_no=roll_no10,date=query_date)                               #{These blocks of codes are for attendance query system
                                                                                                             #they take input and match them with datebase and show them
            name=query_process.student_name                                                                  #as output}
            attendance = query_process.attendance                                             
            
            param = {"name":name,"attendance":attendance,"query_date":query_date,"roll_no":roll_no10,"class":query_class}
            return render(request,"class_10_attendance_query.html",param)                                                                         
        except :
                return HttpResponse("Either you entered date in wrong format .. or it do not exist in database.Please try again")
    return render(request,"class_10_attendance_query.html")




# ---------------------------Class 10 ledger---------------------------
@allowed_user(allowed_roles=["class_teacher_10", "admin"])
def attendance_query_ledger_10(request):
        all_objects= class_10.objects.filter(roll_no=roll_no10)
        name= class_9.objects.get(roll_no = roll_no10,date=query_date)

        present_days= class_10.objects.filter(roll_no=roll_no10,attendance="Present✓")
        present_days = len(present_days)
        absent_days= class_10.objects.filter(roll_no=roll_no10,attendance="Absent❌")
        absent_days = len(absent_days)
        total_days=present_days+absent_days
        present_percent=present_percent=int((present_days/total_days)*100)
        present_percent=str(present_percent)+"%"

        param={"all_objects":all_objects,"present_days":present_days,"name":name, "absent_days":absent_days , "total_days":total_days,"present_percent":present_percent}
        return render(request,"attendance_query_ledger.html",param)
#---------------------------------------------------------------------------------





#===================================================class 1=====================================

@allowed_user(allowed_roles=["class_teacher_1", "admin"])
def class_1_page(request):
    total_students = len(class_1_student.objects.all())
    students= class_1_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_1.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_1_student database   
                             name=class_1_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_1(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_1_student database   
                            name=class_1_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_1(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_1_student.objects.get(roll_number=check)
                        present_data=class_1(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_1.html",param) 






#===================================================class2=======================================================

@allowed_user(allowed_roles=["class_teacher_2", "admin"])
def class_2_page(request):
    total_students = len(class_2_student.objects.all())
    students= class_2_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_2.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_2_student database   
                             name=class_2_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_2(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_2_student database   
                            name=class_2_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_2(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_2_student.objects.get(roll_number=check)
                        present_data=class_2(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_2.html",param) 





#=================================================class3==============================================================
@allowed_user(allowed_roles=["class_teacher_3", "admin"])
def class_3_page(request):
    total_students = len(class_3_student.objects.all())
    students= class_3_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_3.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_3_student database   
                             name=class_3_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_3(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_3_student database   
                            name=class_3_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_3(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_3_student.objects.get(roll_number=check)
                        present_data=class_3(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_3.html",param) 


#================================================class4================================================================
@allowed_user(allowed_roles=["class_teacher_4", "admin"])
def class_4_page(request):
    total_students = len(class_4_student.objects.all())
    students= class_4_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_4.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_4_student database   
                             name=class_4_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_4(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_4_student database   
                            name=class_4_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_4(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_4_student.objects.get(roll_number=check)
                        present_data=class_4(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_4.html",param) 

#================================================class5================================================================
@allowed_user(allowed_roles=["class_teacher_5", "admin"])
def class_5_page(request):
    total_students = len(class_5_student.objects.all())
    students= class_5_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_5.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_5_student database   
                             name=class_5_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_5(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_5_student database   
                            name=class_5_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_5(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_5_student.objects.get(roll_number=check)
                        present_data=class_5(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_5.html",param) 

#===============================================class_6=====================================================================

@allowed_user(allowed_roles=["class_teacher_6", "admin"])
def class_6_page(request):
    total_students = len(class_6_student.objects.all())
    students= class_6_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_6.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_6_student database   
                             name=class_6_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_6(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_6_student database   
                            name=class_6_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_6(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_6_student.objects.get(roll_number=check)
                        present_data=class_6(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_6.html",param) 



#================================================class7===============================================================


@allowed_user(allowed_roles=["class_teacher_7", "admin"])
def class_7_page(request):
    total_students = len(class_7_student.objects.all())
    students= class_7_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_7.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_7_student database   
                             name=class_7_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_7(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_7_student database   
                            name=class_7_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_7(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_7_student.objects.get(roll_number=check)
                        present_data=class_7(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_7.html",param) 


#==============================================class8===================================================================
@allowed_user(allowed_roles=["class_teacher_8", "admin"])
def class_8_page(request):
    total_students = len(class_8_student.objects.all())
    students= class_8_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_8.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_8_student database   
                             name=class_8_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_8(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_8_student database   
                            name=class_8_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_8(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_8_student.objects.get(roll_number=check)
                        present_data=class_8(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_8.html",param) 







    

#================================================class9=================================================================


# this place is mess names are different everywere.
@allowed_user(allowed_roles=["class_teacher_9", "admin"])
def class_9_page(request):                                                    #[2022-01-27] today i created the attendance system.class9 is first system
                                                                              #[2022-01-29]today i made this system totally working , now we can add students from database and mark attendance from site

    total_students = len(class_9_student.objects.all())
    students= class_9_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_9.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_9_student database   
                             name=class_9_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_9(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_9_student database   
                            name=class_9_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_9(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_9_student.objects.get(roll_number=check)
                        present_data=class_9(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_9.html",param) 




#==================================================class_10===================================================

@allowed_user(allowed_roles=["class_teacher_10", "admin"])
def class_10_page(request):
    total_students = len(class_10_student.objects.all())
    students= class_10_student.objects.all()
    param={"students":students}
    
    if request.method =="POST":
       
        for i in range (0,total_students):
            i=str(i+1)
            check=request.POST.get(i,"0")
            form_date=request.POST.get("attendance_date","")
            
            date_validation_check1= (form_date[4:5])                                         #{using this thing for validatating date to prevent django;
            date_validation_check2= (form_date[7:8])                                          # validation error by rising own systemerror exception down there.}

            try:
                if date_validation_check1 != "-" or date_validation_check2 !="-":       #this thing validates the entered date not really but yahh!
                    raise SystemError("date is invalid")

                roll_check = class_10.objects.get(date=form_date,roll_no=check)#[this thing makes error if the is already in database and is handled by the last except block . I caused the error and handled it so that thing do get repeated in databse]
                return HttpResponse("Attendance of date "+form_date+" is already marked")
            except SystemError:
                return HttpResponse("Entered date is in invalid format")#[handles the SystemError exception raised when date is invalid]

            except:
                    if check == i+"False":#[Iam sending [{{roll_number}}+False] from html page when absent radiobutton is marked and taking it here so that we can mark attendance=(absent) here.]
                        a=(check[1]) #[if rollno is of 1 digit then the check[1]takes "F"]
                        b=(check[2]) #[if rollno is of 2 digits then the check[2]takes "F"]
                        if a=="F":
                             x=(check[0])
                             check=x
                             #pulling the name of student from class_10_student database   
                             name=class_10_student.objects.get(roll_number=check)
                             #Adding the details in database
                             absent_data=class_10(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                             absent_data.save()
                      
                        if b=="F":
                            x=(check[0:2])
                            check=x
                            #pulling the name of student from class_10_student database   
                            name=class_10_student.objects.get(roll_number=check)
                            #Adding the details in database
                            absent_data=class_10(roll_no=check,student_name=name,attendance="Absent❌",date=form_date)
                            absent_data.save()





               # Adding the details in database
               
                    else:
                    #[this else block is for adding (attendance=present)]
                        name=class_10_student.objects.get(roll_number=check)
                        present_data=class_10(roll_no=check,student_name=name,attendance="Present✓",date=form_date)
                        present_data.save()
        
    return render(request,"class_10.html",param) 