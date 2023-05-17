from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Merchandise
from .forms import MerchandiseForm
from .filters import MerchandiseFilter
from django.shortcuts import redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.views import View

# Create your views here.
def merchandise(request):
    f = MerchandiseFilter(request.GET, queryset=Merchandise.objects.all())
    context = {
        'merchandise': f,
    }
    
    return render(request, 'merchandise/merchandise.html', context)

@login_required
def merchandise_detail(request, merchandise_id):
    merchandise = get_object_or_404(Merchandise, pk=merchandise_id)
    
    context = {
        'merchandise': merchandise,
    }
    return render(request, 'merchandise/merchandise_detail.html', context)
