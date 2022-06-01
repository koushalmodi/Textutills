from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    spaceremove=request.POST.get('spaceremove', 'off')
    newlineremove=request.POST.get('newlineremove', 'off')
    capfirst=request.POST.get('capfirst', 'off')
    punc = '''++_)(*&^%$#@!-=+|}{\][":';/.,?><'''
    analyzed = ""
    for char in djtext:
        if char not in punc:
            analyzed = analyzed + char
        analyzedlength = len(analyzed)
        for char in analyzed:
            if char == " ":
                analyzedlength = analyzedlength - 1
    if removepunc == 'on':
        analyzed=""
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char
        param = {'purpose': 'removepunc','analyzed_text': analyzed,'analyzed_text2': analyzedlength}
        djtext=analyzed
        #return render(request, 'analyze.html', param)

    if spaceremove=='on':
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" "and [index+1]):
                analyzed=analyzed+char
        param = {'purpose': 'spaceremove', 'analyzed_text': analyzed, 'analyzed_text2': analyzedlength}
        djtext=analyzed
        #return render(request, 'analyze.html', param)
    if newlineremove=='on':
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed+char
        param = {'purpose': 'newlineremove', 'analyzed_text': analyzed , 'analyzed_text2': analyzedlength}
        djtext = analyzed
        #return render(request, 'analyze.html', param)
    if capfirst == "on":
        str1=djtext[0].upper()
        analyzed=str1+djtext[1:]

        param = {'purpose': 'capfirst', 'analyzed_text': analyzed, 'analyzed_text2': analyzedlength}
        djtext=analyzed
        #return render(request, 'analyze.html', param)

    if(capfirst!="on" and newlineremove!="on" and spaceremove!="on" and removepunc!="on"):
        errer={'ERRER!': 'ERRER!'}
        return render(request,'error.html',errer)
    return render(request, 'analyze.html', param)





