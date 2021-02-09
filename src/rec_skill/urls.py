"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rec_app import views

urlpatterns = [
    path('',views.rec),
    path('check',views.check),
    path('register/',views.register),
    path('register/create',views.create),
    path('admin/', admin.site.urls),
    path('company/',views.company),
    path('company/createc',views.createc),
    path('stu_dashboard/',views.stu_dashboard,name='stu_dashboard'),
    path('reccm/uc/<int:id>',views.uc),
    path('compdash/',views.compdash,name='compdash'),
    path('reccm/',views.reccm,name='reccm'),
    path('ava_company/',views.ava_company,name='ava_company'),
    path('ava_company/jobapply/<int:jid>',views.jobapply),
    path('skills/',views.skills,name='skills'),
    path('stu_pro/',views.stu_pro,name='stu_pro'),
    path('stu_noti/',views.stu_noti,name='stu_noti'),
    path('stu_det/',views.stu_det,name='stu_det'),
    path('stu_det/getuser',views.getuser),
    path('recruit/',views.recruit,name = 'recruit'),
    path('student_profile/<str:name>/<int:id>',views.stut_pro,name = 'stut_pro'),
    path('compnotification/',views.compnotification,name = 'compnot'),
    path('help/',views.help1,name = 'help&support'),
    path('usersettings/',views.usersettings,name = 'usersettings'),
    path('admincomp/', views.admincomp,name="admincomp"),
    path('admincomp/delete/<int:id>', views.delcomp,name="delcomp"),
    path('studentlist/<int:id>',views.stu_list,name = 'studentlist'),
    path('usersettings/update',views.updateusers,name='updateuser'),
    path('createjob/',views.createjob,name='createjob'),
    path('recruit/search',views.search,name="search"),
    path('sos/',views.pageno,name="pageno"),
    # path('company/',views.company),
    # path('login/',views.log_view),
    # path('login/check',views.check),
    # path('register/recskill/',views.rec),
    # path('recskill/',views.rec),
    # path('recskill/check',views.check),
]
