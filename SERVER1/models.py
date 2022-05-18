from django.db import models
from datetime import datetime




# Create your models here.
#==========================================Attendance system database started====================================

# class1 student database
class class_1_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name

# class2 student database
class class_2_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name



# class3 student database
class class_3_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name




# class4 student database
class class_4_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name




# class5 student database
class class_5_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name


# class6 student database
class class_6_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name


# class7 student database
class class_7_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name



# class8 student database
class class_8_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name



#class_9 student database

class class_9_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name



#class_10 student database

class class_10_student(models.Model):
    roll_number = models.CharField(default="",max_length=30,unique=True)
    Students_name = models.CharField(default="",max_length=25)

    def __str__(self):
        return self.Students_name
#class10 attendance database



#class 1 attandance database table

class class_1(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name




#class 2 attandance database table

class class_2(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name






#class 3 attandance database table

class class_3(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name








#class 4 attandance database table

class class_4(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name





#class 5 attandance database table

class class_5(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name








#class 6  attandance database table

class class_6(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name







#class 7 attandance database table

class class_7(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name






#class 8 attandance database table

class class_8(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name



    



#class 9 attandance database table

class class_9(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name



class class_10(models.Model):
    date = models.DateField(default= "")
    roll_no = models.IntegerField(default= 0)
    student_name = models.CharField(max_length=25, default="")
    attendance_choices = models.TextChoices("attendance_choices", "Absent❌ Present✓" )
    attendance = models.CharField(blank=False, choices=attendance_choices.choices,max_length=10)
    
    def __str__(self):
        return self.student_name

#==========================================Attendance system database Ended====================================



#Database for notice 

class Notice_Database(models.Model):
    date = models.DateField(default= "")
    Notice_title = models.CharField(max_length=50, default="")
    Notice_desc = models.TextField(default="")
    author= models.CharField(max_length=25,default="")
    
    def __str__(self):
        return self.Notice_title




class About(models.Model):
    title = models.CharField(max_length=25)
    about_desc = models.TextField(default="")

    def __str__(self):
        return self.title+ " ----- "+self.about_desc[0:]
    





class Blog(models.Model):
    id= models.AutoField(primary_key=True)
    date = models.DateTimeField()

    
    writer =models.CharField(max_length=60)
    content= models.TextField(default="")


    def __str__(self):
        return self.writer

        
    class Meta:
        ordering = ['-date',]
