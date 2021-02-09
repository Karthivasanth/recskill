from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages
import time
from .models import logindb, usercu,userinfo,courses,Cjob,help,japp
from operator import and_, or_
user = None
# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,'hello.html',{'home':'http://127.0.0.1:8000/login','register':'http://127.0.0.1:8000/register','rec':'http://127.0.0.1:8000/recskill'})

def log_view(request,*args,**kwargs):
    return render(request,'login.html')

def check(request):
    global user
    if request.method == 'POST':
        name = request.POST['name']
        pas = request.POST['pass']
        role = logindb.getrole(name,pas)
        x=logindb.auth(name,pas)
        if x is None:
            messages.warning(request, 'Username/Password does not match')
            print("Login Failed")
            return redirect('/')
        else:
            # messages.success(request, 'Login Success! Welcome')
            print("Login Successfull")
            user = name
            if role == 's':
                return redirect('/stu_dashboard')
            else:
                return redirect('/compdash')

    return render(request,'output.html',{'name':name , 'pass':pas})

def register(request):
    return render(request,'register.html')

def create(request):
    global user
    if request.method == 'POST':
        uname = request.POST['uname']
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        mail = request.POST['mailid']
        password = request.POST['pass']
        role = 's'
        print("-"*50)
        print(password)
        print("-"*50)
        a = logindb.checkname(uname)
        if a == None:
            x=logindb(username=uname,firstname=firstname,lastname=lastname,email=mail,password=password,role=role)
            x.save()
            user = uname
            print("User Created")
            messages.success(request, 'User Created successfully!')
            time.sleep(3)
            return redirect('/stu_det')
        else:
            print("Username Exists")
            messages.warning(request, 'User Already Exists! Use Different Username')
            time.sleep(3)
            return redirect('/register')

def getuser(request):
    if request.method=='POST':
      dob = request.POST['dob']
      cname = request.POST['cname']
      dept = request.POST['dept']
      csem = request.POST['currsem']
      yoj = request.POST['yoj']
      sl = request.POST.getlist('checks[]')
      il = request.POST.getlist('checks2[]')
      uname = user
      y=userinfo(uname=uname,Dob=dob,cname=cname,Department=dept,sem=csem,yroj=yoj,skilllist=sl,aoilist=il)
      y.save()
      return redirect('/stu_dashboard')

def createc(request):
    if request.method == 'POST':
        cname = request.POST['uname']
        caddres = request.POST['fname']
        mail = request.POST['mailid']
        password = request.POST['pass']
        role = 'c'
        print("-"*50)
        print(password)
        print("-"*50)
        a = logindb.checkname(cname)
        if a == None:
            x=logindb(username=cname,firstname=caddres,email=mail,password=password,role=role)
            x.save()
            print("User Created")
            messages.success(request, 'User for Company Created successfully!')
            time.sleep(3)
            return redirect('/')
        else:
            print("Username Exists")
            messages.warning(request, 'User Already Exists! Use Different Userame')
            time.sleep(3)
            return redirect('/company')


    

    
def rec(request):
    return render(request,'index.html',{'register':'http://127.0.0.1:8000/register','company':'http://127.0.0.1:8000/company'})

def company(request):
     return render(request,'company.html')

def stu_dashboard(request):
    global user
    use = user
    skillarr = userinfo.objects.filter(uname = use).values_list('skilllist',flat=True)
    sk=skillarr[0]
    data = courses.objects.filter(skill__in=sk).values()
    return render(request , "stu_dashboard.html",{'name':user,'c': data})



def stu_pro(request):
    global user 
    use = user
    u_info = userinfo.objects.filter(uname = use).values()
    us_info = u_info[0]
    name_info = logindb.objects.filter(username = use).values()
    ninfo = name_info[0]
    skillarr = userinfo.objects.filter(uname = use).values_list('skilllist',flat=True)
    sk=skillarr[0]
    aoiarr = userinfo.objects.filter(uname = use).values_list('aoilist',flat=True)
    aoi = aoiarr[0]
    crsarr = usercu.objects.filter(uname = use).values_list('c_id',flat=True)
    crs_id = crsarr
    c_data = courses.objects.filter(c_id__in=crs_id).values()
    return render(request , "stu_pro.html",{'skar':sk,'aoiar': aoi,'carr' : c_data,'user' : us_info,'name' : ninfo})

def stu_noti(request):
    global user 
    use = user
    jobarr = japp.objects.filter(usename = use).filter(sts='applied').values_list('j_id',flat=True)
    crs_id = jobarr
    c_data = Cjob.objects.filter(j_id__in=crs_id).values()
    jobarr2 = japp.objects.filter(usename = use).filter(sts='selected').values_list('j_id',flat=True)
    crs_id2 = jobarr2
    c_data2 = Cjob.objects.filter(j_id__in=crs_id2).values()
    return render(request , "stu_noti.html",{'arr' : c_data,'arr2': c_data2})

def stu_det(request):
    return render(request , "stu_det.html")

def ava_company(request):
    global user 
    use = user
    jobarr = Cjob.objects.all()
    return render(request , "ava_company.html",{'arr' : jobarr})

def jobapply(request,jid):
    global user
    use = user
    if request.method == 'POST':
        tkn = str(jid) + user
        res = japp.checks(tkn)
        if res == None:
            ins = japp(j_id = jid,sts = 'applied',usename=use,uemail = logindb.getemail(use),token = tkn)
            ins.save()
            messages.success(request, 'Updated')
            time.sleep(3)
            return redirect("/ava_company")
        messages.warning(request, 'U have applied to this job already!')
        time.sleep(3)
        return redirect('/ava_company')

def skills(request):
    global user 
    use = user
    skillarr = userinfo.objects.filter(uname = use).values_list('skilllist',flat=True)
    sk=skillarr[0]
    data = courses.objects.filter(skill__in=sk).values()
    return render(request , "skills.html",{'skar':sk,'crs' : data})

def reccm(request):
    global user
    use = user
    skillarr = userinfo.objects.filter(uname = use).values_list('skilllist',flat=True)
    sk=skillarr[0]
    data = courses.objects.filter(skill__in=sk).values()
    data2 = courses.objects.order_by('-rating').values()[:5]
    crsarr = usercu.objects.filter(uname = use).values_list('c_id',flat=True)
    crs_id = crsarr
    c_data = courses.objects.filter(c_id__in=crs_id).values()
    return render(request , "reccm.html",{'c': data,'d':data2,'mc' : c_data})

def uc(request,id):
    global user
    if request.method == 'POST':
        tkn = str(id) + user
        res = usercu.checks(tkn)
        if res == None:
            ins=usercu(c_id = id,sts = 'done',uname=user,token = tkn)
            print(ins)
            ins.save()
            messages.success(request, 'Updated')
            time.sleep(3)
            return redirect("/reccm")
        messages.warning(request, 'U Have done this Course already!')
        time.sleep(3)
        return redirect('/reccm')

#company page

def admincomp(request):
    global user
    showall = help.objects.all()
    return render(request,'admin.html',{"data":showall})
#admin delete complaints
def delcomp(request,id):
    global user
    delcomplaint=help.objects.get(id=id)
    delcomplaint.delete()
    showdata=help.objects.all()
    return render(request,'admin.html',{"data":showdata})

def compdash(request):
    global user
    return render(request,'companydash.html')

#company help
def help1(request):
    global user
    if request.method == 'POST':
          user = request.POST['user']
          title   = request.POST['title']
          desc    = request.POST['desc']
          print(user,title,desc)
          ins = help(user=user,title=title,desc=desc)
          ins.save()
    return render(request,'help.html')

#create job
def createjob(request,*args, **kwargs):
    global user
    if request.method == 'POST':
          u = user
          comp = request.POST['company']
          t = request.POST['title']
          skills_req   = request.POST['skills_req']
          description    = request.POST['description']
          print(u,comp,t,skills_req,description)
          tps = Cjob(userid=u,company=comp,title=t,skills_req=skills_req,description=description)
          tps.save()
    return render(request,'createjob.html' )

    return render(request ,"createjob.html", {} )     




def search(request):
    global user
    if request.method =='POST':
        skill = request.POST['skill'].lower() 
        ins= userinfo.objects.filter(skilllist__contains=[skill]).all()
        context1=[]
        for e in userinfo.objects.filter(skilllist__contains=[skill]).all():
            context1.append(e)
        return render(request,'recruit.html',{"data1":context1})
    else:
        return render(request,'recruit.html')



def recruit(request):
        global user
        return render(request,'recruit.html')
    
def compnotification(request):
    global user
    usearch=Cjob.objects.filter(userid=user).values()
    print(usearch)
    return render(request,'compnotification.html',{"value":usearch})

def stut_pro(request, name=None, id=None):
    print(id)
    if request.method =='POST':
        japp.objects.filter(j_id=id).update(sts = 'selected')
        messages.success(request,'the applicant is selected')
        return redirect('/compnotification')
    if name:
        stss=japp.objects.filter(usename=name).values_list('sts')[0]
        st=stss[0]
        print(name)
        print(st)
        use = name
        u_info = userinfo.objects.filter(uname = use).values()
        us_info = u_info[0]
        name_info = logindb.objects.filter(username = use).values()
        ninfo = name_info[0]
        skillarr = userinfo.objects.filter(uname = use).values_list('skilllist',flat=True)
        sk=skillarr[0]
        aoiarr = userinfo.objects.filter(uname = use).values_list('aoilist',flat=True)
        aoi = aoiarr[0]
        crsarr = usercu.objects.filter(uname = use).values_list('c_id',flat=True)
        crs_id = crsarr
        c_data = courses.objects.filter(c_id__in=crs_id).values()
        if st == 'applied':
            val='accept'
        else: 
            val= 'selected'
        return render(request , "stut_pro.html",{'skar':sk,'aoiar': aoi,'carr' : c_data,'user' :us_info,'name' : ninfo,'value':val})
    return render(request,'stut_pro.html')

def stu_list(request, id=None):
    global user
    if id:
        useride=japp.objects.filter(j_id=id).values()
        print(useride)
    return render(request,'studentlist.html',{"value":useride})

#user settings


def usersettings(request):
    global user
    usearch=logindb.objects.get(username=user)
    return render(request,'settings.html',{"data":usearch})

def updateusers(request):
    global user
    if request.method == 'POST':
            username = request.POST['username']
            firstname = request.POST['firstname']
            email = request.POST['email']
            password = request.POST['password']
            logindb.objects.filter(username=user).update(username=username,firstname=firstname,email=email,password=password)
            username = request.POST['username']
            firstname = request.POST['firstname']
            email = request.POST['email']
            password = request.POST['password']
            user=username
            ins = logindb(username=username,firstname=firstname,email=email,password=password)
            return render(request,'settings.html',{"data":ins})

     

def pageno(request):
    return render(request,'pagenotfound.html')
