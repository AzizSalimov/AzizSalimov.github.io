from django.shortcuts import render

def kirish(request):
    return render(request, "kirish/kirish.html")