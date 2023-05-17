from django.shortcuts import render,redirect
from .models import Userprofile
from .forms import UserprofileForm
from django.contrib import messages

# Create your views here.

def indexx(request):
    # add person form
    form = UserprofileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('indexx')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'userprofile/indexx.html', ctx)