from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from profileapp.forms import UserProfileSearchForm
from fileapp.models import UploadedFile
# Create your views here.

def userprofileview(request, username):
    user = get_object_or_404(User, username=username)
    uploaded_files = UploadedFile.objects.filter(user=user)
    shared_files=user.shared_files.all()
    context = {
        'user_profile': user,
        'uploaded_files': uploaded_files,
        'shared_files':shared_files,
    }
    
    return render(request, 'profileapp/userprofile.html', context)

def user_search(request):
    form=UserProfileSearchForm(request.GET)
    results=None
    if form.is_valid():
        search_query=form.cleaned_data['search_query']
        results=User.objects.filter(username__icontains=search_query).exclude(is_superuser=True)
    context={
        'form':form,
        'results':results,
    }
    return render(request,'profileapp/user_search.html',context)


