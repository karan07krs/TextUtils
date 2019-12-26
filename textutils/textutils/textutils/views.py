#file created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext=request.POST.get('ta1', 'default')
    #print(djtext)
    rempunc = request.POST.get("rempunc",'off')
    capfirst = request.POST.get("capfirst", 'off')
    charcount = request.POST.get("charcount", 'off')
    remspace = request.POST.get("remspace", 'off')
    resultstr=''
    new=""+djtext
    oprn=''
    if rempunc == "on":
        oprn = oprn+'Remove punctuations '
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                resultstr = resultstr + char
                new = resultstr
    if capfirst == 'on':
        oprn=oprn+'| Capitalizing first character '
        new = new.capitalize()
    if charcount == 'on':
        oprn=oprn+'| Count characters '
        new = new + "(--->Text Length<---" + str(len(djtext)) + ")"
    if remspace == 'on':
        oprn=oprn+'| Remove spaces'
        print(new)
        new = new.replace(" ", "")
        print(new)
    if rempunc != "on" and capfirst != "on" and charcount != "on" and remspace != "on":
        return render(request, 'index.html')
    params = {'functions_used': oprn, 'result': new}
    #analyze the text
    return render(request, 'analyze.html', params)

