from django.shortcuts import render
from django.http import HttpResponse

def index(request):
          context = {
                    "title": "Trigger python logic"
          }
          
          return render(request, "home/index.html", context)
def simple_function(request):
          print("\nThis a simple function\n")
          return HttpResponse("""<html><script>window.location.replace('/');</script></html>""")