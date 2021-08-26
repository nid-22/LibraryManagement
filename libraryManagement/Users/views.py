from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from Users.forms import registerForm,userUpdateForm
from Users.models import Users
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['Username']
        password = request.POST['password']
        if email is None or password is None:            
            messages.error(request,'Please enter email and password')
            return redirect('login')
        user = authenticate(username=email, password=password)
        try:
            django_login(request,user)
        except Exception as e:
            print(e)
        if not user:
            messages.error(request,'Invalid Credentials')
            return redirect('login')
        # t,_ = Token.objects.get_or_create(user=user)
        # t.delete()
        # token, _ = Token.objects.get_or_create(user=user)
        
        # roleid = user.RoleID
        
            # messages.error(request,msg)            
            # request.session['token']=token   #saving token in session        
            # request.session['userRoleID'] = userRoleID
        return redirect('home')
    else:
        return render(request, 'Users/login.html')

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'home.html')

@login_required
def register(request):
    if request.method =='POST':
        form = registerForm(request.POST)
        if form.is_valid():
            user = form.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            return redirect('register')
        else:
            print(form.errors)
    form = registerForm()       
    return render(request,'Users/addUser.html',{'form':form})

@login_required
def logout(request):
    django_logout(request)
    return redirect('login')

@login_required
def viewUsers(request):
    users = Users.objects.all()
    print('users', users)
    return render(request,'Users/viewUsers.html',{'users':users})

@login_required
def deleteUsers(request,id):
    try:
        u=Users.objects.get(id=id)
        u.delete()  #or user.is_active = False  or user.is_deleted = 0 if data is not to be deleted
    except ObjectDoesNotExist:
        print('')
    return redirect('viewUsers')

@login_required
def updateUsers(request,id):
    e = Users.objects.get(id=id)
    if request.method == 'POST':
        form = userUpdateForm(request.POST,request.FILES, instance=e)
        if form.is_valid():
            form.save()
            return redirect('viewUsers')
        else:
            print(form.errors)
    form = userUpdateForm(instance=e)
    return render(request, 'Users/updateUser.html',{'form':form})