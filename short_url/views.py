from django.shortcuts import render
import pyshorteners
import validators

# Create your views here.
def short_url(request):
    try:
      if request.method == 'POST':
          urls = request.POST.get('urls')
          if validators.url(urls)==True:
            shortener = pyshorteners.Shortener()
            shorted_url = shortener.tinyurl.short(urls)
            return render(request, 'short_url.html',{"shorted_url":shorted_url})
          else:
            return render(request, 'invalid_url.html',{"invalid_url_msg":"Please type a valid url!"})   
      else:
        return render(request, 'index.html',{})
    except Exception:
        return render(request, 'no_connection.html',{'no_connection':'Please connect to internet!'})
