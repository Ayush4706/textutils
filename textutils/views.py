#I have created this file - Ayush
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Hello Ayush Bhai ")

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')
    if removepunc=='on':
        analyzed=''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
    elif fullcaps=='on':
        analyzed = ''
        analyzed=djtext.upper()
    elif newlineremove=='on':
        analyzed = ''
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed+=char
    elif extraspaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if djtext[index]==' ' and djtext[index+1]==' ':
                pass
            else:
                analyzed+=char
    elif charcount=='on':
        analyzed=0
        for char in djtext:
            analyzed+=1
    else:
        analyzed=djtext
    params = {'purpose':'Removed punctuations','analyzed_text':analyzed}
    return render(request,'analyze.html',params)