from django.urls import path,include
from SERVER1  import views

urlpatterns = [
    path("",views.index,name="home"),
    path("notice/",views.notice,name="notice"),
    path("blog/",views.blog,name="blog"),
    path("events/",views.events,name="events"),
    path("about/",views.about,name="about"),
    path("login_page/",views.login_page,name="login_page"),
    path("logout_page/",views.logout_page,name="logout_page"),
   
    path("classes_to_mark/",views.classes_to_mark,name="Select class to mark"),
    path("classes_to_query/",views.classes_to_query,name="Select class to query"),

    path("class_1_page/",views.class_1_page,name="class_1_attendance"),
    path("class_2_page/",views.class_2_page,name="class_2_attendance"),
    path("class_3_page/",views.class_3_page,name="class_3_attendance"),
    path("class_4_page/",views.class_4_page,name="class_4_attendance"),
    path("class_5_page/",views.class_5_page,name="class_5_attendance"),
    path("class_6_page/",views.class_6_page,name="class_6_attendance"),
    path("class_7_page/",views.class_7_page,name="class_7_attendance"),
    path("class_8_page/",views.class_8_page,name="class_8_attendance"),
    path("class_9_page/",views.class_9_page,name="class_9_attendance"),
    path("class_10_page/",views.class_10_page,name="class_10_attendance"),


    path("class_1_attendance_query/",views.class_1_attendance_query,name="class_1_attendance_query"),
    path("class_2_attendance_query/",views.class_2_attendance_query,name="class_2_attendance_query"),
    path("class_3_attendance_query/",views.class_3_attendance_query,name="class_3_attendance_query"),
    path("class_4_attendance_query/",views.class_4_attendance_query,name="class_4_attendance_query"),
    path("class_5_attendance_query/",views.class_5_attendance_query,name="class_5_attendance_query"),
    path("class_6_attendance_query/",views.class_6_attendance_query,name="class_6_attendance_query"),
    path("class_7_attendance_query/",views.class_7_attendance_query,name="class_7_attendance_query"),
    path("class_8_attendance_query/",views.class_8_attendance_query,name="class_8_attendance_query"),
    path("class_9_attendance_query/",views.class_9_attendance_query,name="class_9_attendance_query"),
    path("class_10_attendance_query/",views.class_10_attendance_query,name="class_10_attendance_query"),


    path("attendance_query_ledger_1/",views.attendance_query_ledger_1,name="attendance_query_ledger_1"),
    path("attendance_query_ledger_2/",views.attendance_query_ledger_2,name="attendance_query_ledger_2"),
    path("attendance_query_ledger_3/",views.attendance_query_ledger_3,name="attendance_query_ledger_3"),
    path("attendance_query_ledger_4/",views.attendance_query_ledger_4,name="attendance_query_ledger_4"),
    path("attendance_query_ledger_5/",views.attendance_query_ledger_5,name="attendance_query_ledger_5"),
    path("attendance_query_ledger_6/",views.attendance_query_ledger_6,name="attendance_query_ledger_6"),
    path("attendance_query_ledger_7/",views.attendance_query_ledger_7,name="attendance_query_ledger_7"),
    
    
    path("attendance_query_ledger_8/",views.attendance_query_ledger_8,name="attendance_query_ledger_8"),
    path("attendance_query_ledger_9/",views.attendance_query_ledger_9,name="attendance_query_ledger_9"),
    path("attendance_query_ledger_10/",views.attendance_query_ledger_10,name="attendance_query_ledger_10"),
]