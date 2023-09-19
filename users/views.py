from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save() #saves the user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulations {username}! Your account has been created! Now you are able to Log in')
            response= redirect('login')
            response.set_cookie('player_id',str(user.id),max_age=None)
            return response
    else:
        form= UserRegisterForm()
    return render(request,'users/register.html',{'form': form})

@login_required
def myprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        
        if u_form.is_valid():
            u_form.save()
            
            messages.success(request, f'Your account has been updated')
            return redirect('myprofile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        
   
    context = {'u_form' : u_form}
    return render(request, 'users/myprofile.html', context)



def home(request):
    return render(request, 'users/home.html')

