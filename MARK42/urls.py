"""MARK42 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("SERVER1.urls")),
    path("notice/",include("SERVER1.urls")),
    path("events/",include("SERVER1.urls")),
    path("about/",include("SERVER1.urls")),
    path("login_page/",include("SERVER1.urls")),
    path("logout_page/",include("SERVER1.urls")),
    
    path("blog_delete/",include("SERVER1.urls")),
    path("blog_sample/",include("SERVER1.urls")),

#for the attendence class to choose[To mark]
    path("classes_to_mark/",include("SERVER1.urls")),

#for the attendence class to choose[To query]
    path("classes_to_query/",include("SERVER1.urls")),


# for class 1 attendance
    path("class_1_page/",include("SERVER1.urls")),


# for class 2 attendance
    path("class_2_page/",include("SERVER1.urls")),



# for class 3 attendance
    path("class_3_page/",include("SERVER1.urls")),


# for class 4 attendance
    path("class_4_page/",include("SERVER1.urls")),



# for class 5 attendance
    path("class_5_page/",include("SERVER1.urls")),


# for class 6 attendance
    path("class_6_page/",include("SERVER1.urls")),




# for class 7 attendance
    path("class_7_page/",include("SERVER1.urls")),


# for class 8 attendance
    path("class_8_page/",include("SERVER1.urls")),




# for class 9 attendance
    path("class_9_page/",include("SERVER1.urls")),


# for class 10 attendance
    path("class_10_page/",include("SERVER1.urls")),








#for the template to query the attendance
    path("class_1_attendance_query/",include("SERVER1.urls")),
    path("class_2_attendance_query/",include("SERVER1.urls")),
    path("class_3_attendance_query/",include("SERVER1.urls")),
    path("class_4_attendance_query/",include("SERVER1.urls")),
    path("class_5_attendance_query/",include("SERVER1.urls")),
    path("class_6_attendance_query/",include("SERVER1.urls")),
    path("class_7_attendance_query/",include("SERVER1.urls")),
    path("class_8_attendance_query/",include("SERVER1.urls")),
    path("class_9_attendance_query/",include("SERVER1.urls")),
    path("class_10_attendance_query/",include("SERVER1.urls")),


#for the template to query the attendance_ledger

    path("attendance_query_ledger_1/",include("SERVER1.urls")),
    path("attendance_query_ledger_2/",include("SERVER1.urls")),
    path("attendance_query_ledger_3/",include("SERVER1.urls")),
    path("attendance_query_ledger_4/",include("SERVER1.urls")),
    path("attendance_query_ledger_5/",include("SERVER1.urls")),
    path("attendance_query_ledger_6/",include("SERVER1.urls")),
    path("attendance_query_ledger_7/",include("SERVER1.urls")),


    path("attendance_query_ledger_8/",include("SERVER1.urls")),
    path("attendance_query_ledger_9/",include("SERVER1.urls")),
    path("attendance_query_ledger_10/",include("SERVER1.urls")),

]
