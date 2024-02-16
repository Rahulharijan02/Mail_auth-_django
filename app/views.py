from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
from django.contrib import messages

from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode


# Create your views here.

@login_required(login_url='login')
def home(request):
    
    return render(request, 'app/base.html')


def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # for sending Email
            current_site = get_current_site(request)
            mail_subject = "For Activate Your Account !!!!"

            message = render_to_string('app/activate_email_message.html',{
                'user':form.cleaned_data['username'],
                'domain': current_site.domain,
                'token': default_token_generator.make_token(user),
                'uid': urlsafe_base64_encode(force_bytes(user.pk))
            })

            to_email = form.cleaned_data['email']
            email = EmailMessage(
                mail_subject,message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Account created Successfully!!!!, Please Check your mail for activate your account.')
            return redirect('login')
        else:
            messages.error(request, 'Account creation failed!!!!. Please check & try again>>.')
    return render(request, 'app/register.html',{
        'form':form
    })


def  activate(request, uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        return render(request, 'app/activation_successful.html')
    else:
        return render(request, 'app/activation-unsuccessful.html')