from django.shortcuts import render_to_response, redirect, HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib.auth import logout as auth_logout, login as auth_login, authenticate
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from forms import RegistrationForm, LoginForm

def login(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    username = password = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                print "valid"
                return HttpResponseRedirect('/login')
            else:
                print "not active"
                return HttpResponseRedirect('/login')
        else:
            print "Invalid login details"
            return HttpResponse("Invalid login details supplied.")
    args = {}
    args['form'] = LoginForm()
    print "did jack"
    return render_to_response('accounts/login.html', args, context_instance=context)

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/login')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            auth_login(request, new_user)
            return HttpResponseRedirect('/login')
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    return render_to_response('accounts/register.html', args)

@login_required
def register_success(request):
    return render_to_response('accounts/register_success.html')
