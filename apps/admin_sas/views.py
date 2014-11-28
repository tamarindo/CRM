from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext  # para hacer funcionar {% csrf_token %}
from django.contrib.auth.forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

def restringir_login(request):
    if request.user.is_authenticated():
        return True
    else:
        HttpResponseRedirect(reverse_lazy("login"))


def v_logout(request):
    try:
        _user = request.user
        logout(request)
    except Exception, e:
        print e
    return HttpResponseRedirect(reverse_lazy("principal"))

def login(request):
    mensaje=False
    if request.method == 'POST':
        formularioLogin = AuthenticationForm(request.POST)
        if formularioLogin.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario,password=clave)
            if acceso is not None:
                if acceso.is_active:
                    auth_login(request,acceso)
                    return HttpResponseRedirect(reverse_lazy("principal"))
                else:
                    mensaje="Su Usuario No esta Activo"
            else:
                mensaje="Su username o password estan incorrentos, vuelvelo a intentar"
        else:
            mensaje="Su username o password estan incorrentos, vuelvelo a intentar"

    formularioLogin = AuthenticationForm(request.POST)
    if mensaje:
        return render_to_response('login.html',{'mensaje':mensaje,'formulario':formularioLogin},context_instance=RequestContext(request)) 
    else:
        return render_to_response('login.html',{'formulario':formularioLogin},context_instance=RequestContext(request))  


def principal(request):
    if request.user.is_authenticated():
        template = "index.html"
        return render_to_response(template, locals(), context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse_lazy("login"))

def produtos(request):
    restringir_login(request)

    return render_to_response('productos.html',context_instance=RequestContext(request))

def myprodutos(request):
    restringir_login(request)
    return render_to_response('myproductos.html',context_instance=RequestContext(request))

def blog(request):
    restringir_login(request)
    return render_to_response('blog.html',context_instance=RequestContext(request))

def mensajes(request):
    restringir_login(request)
    return render_to_response('mensajes.html',context_instance=RequestContext(request))

def historialpagos(request):
    restringir_login(request)
    return render_to_response('historialpagos.html',context_instance=RequestContext(request))