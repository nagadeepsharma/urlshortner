from django.shortcuts import render, redirect
from django.contrib import messages
from .models import shorturl
import random
import string
import pyshorteners as sh

# Create your views here.
def dashboard(request):
    urls = shorturl.objects.all()
    return render(request, 'dashboard.html', {'urls': urls})

def generate(request):
    if request.method == "POST":
        # generate
        pass
        if request.POST['original'] and request.POST['short']:
            # generate based on user input
            original = request.POST['original']
            short = request.POST['short']
            check = shorturl.objects.filter(short_query=short)
            if not check:
                newurl = shorturl(
                    
                    original_url=original,
                    short_query=short,
                )
                newurl.save()
                return redirect(dashboard)
            else:
                messages.error(request, "Already Exists")
                return redirect(dashboard)
        elif request.POST['original']:
            # generate randomly
            original = request.POST['original']
            generated = False
            while not generated:
                s = sh.Shortener()
                short=s.tinyurl.short(original)
                short=short.replace('https://','')
                check = shorturl.objects.filter(short_query=short)
                if not check:
                    newurl = shorturl(
                        original_url=original,
                        short_query=short,
                    )
                    newurl.save()
                    return redirect(dashboard)
                else:
                    continue
        else:
            messages.error(request, "Empty Fields")
            return redirect(dashboard)
    else:
        return redirect('')


def home(request, query=None):
    print(query)
    if not query or query is None:
        return render(request, 'dashboard.html')
    else:
        try:
            check = shorturl.objects.get(short_query='tinyurl.com/'+query)
            print(check)
            check.visits = check.visits + 1
            check.save()
            url_to_redirect = check.original_url
            return redirect(url_to_redirect)
        except shorturl.DoesNotExist:
            return render(request, 'dashboard.html', {'error': "error"})

# added delete URl
def deleteurl(request):
    if request.method == "POST":
        short = request.POST['delete']
        try:
            check = shorturl.objects.filter(short_query=short)
            check.delete()
            return redirect(dashboard)
        except shorturl.DoesNotExist:
            return redirect(home)
    else:
        return redirect(home)
