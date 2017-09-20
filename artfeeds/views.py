from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from pyshorteners import Shortener
from django.core.mail import send_mail
# Create your views here.

def index(request):
    template=loader.get_template("artfeeds/index.html")
    return HttpResponse(template.render())
def urlshort(request):

    return render(request,'artfeeds/urlshort.html')
def shorty(request):
    if request.POST:
        r=request.POST.get("q","")

        try:
            access_token="289702bbf45c1d89567e293d360124eeb2d8b2aa"
            shortener=Shortener('Bitly',bitly_token=access_token)
            a=shortener.short(r)

            data_list={'u':a}
            context={'data_list':data_list}
            return render(request,'artfeeds/shorty.html',context)
            
        except:
        
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def newsletter(request):
    template=loader.get_template("artfeeds/newsletter.html")
    return HttpResponse(template.render())
def newsl(request):
    return HttpResponse("Thanks!")
 
        
def privacy(request):
    template=loader.get_template("artfeeds/privacy.html")
    return HttpResponse(template.render())
def terms(request):
    template=loader.get_template("artfeeds/terms.html")
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template("artfeeds/contact.html")
    return HttpResponse(template.render())

