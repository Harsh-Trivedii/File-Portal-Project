from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from fileapp.models import UploadedFile
from fileapp.forms import FileUploadForm
from django.db.models import Q
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            print('Registration successful')
            return redirect(login_user)
    context={
        'form':form,
    }
    return render(request,'registration/register.html',context)

def login_user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            print('Login Successful')
            return redirect(home_view)
    context={
        'form':form,
    }
    return render(request,'registration/login.html',context)

def logout_user(request):
    logout(request)
    return redirect(login_user)


@login_required
def home_view(request):
    return render(request,'fileapp/home.html')

@login_required
def file_upload(request):
    form=FileUploadForm()
    if request.method=='POST':
        form=FileUploadForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file=form.save(commit=False)
            uploaded_file.user=request.user
            uploaded_file.save()
            uploaded_file.shared_with.set(form.cleaned_data['shared_with'])
            return redirect(file_list)
    form.fields['shared_with'].queryset = User.objects.exclude(
        Q(pk=request.user.pk) | Q(is_superuser=True)
    )
    context={
        'form':form,
    }
    return render(request,'fileapp/fileupload.html',context)


@login_required
def file_list(request):
    filelist=UploadedFile.objects.filter(user=request.user)
    context={
        'filelist':filelist,
    }
    return render(request,'fileapp/filelist.html',context)
