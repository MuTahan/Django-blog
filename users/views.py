from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create Method for accepting data from the User

def register(request):

    # validate whether the request is POST request or NOT!
    if request.method == 'POST':
        # If yes populate the form with the inputed data
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # this is for the success Page Only and there are know need for app logic
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request , 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form

    }
    return render(request, 'users/profile.html',context)