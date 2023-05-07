from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import get_template
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'newsletter/home.html')
