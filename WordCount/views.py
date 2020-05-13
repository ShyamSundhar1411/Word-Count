from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'home.html')
def add(request):
    fulltext=request.GET['name']
    print(fulltext)
    a=''
    for i in range(len(fulltext)):
        if fulltext[i]!=' ':
            a+=fulltext[i]
    print(a)
    word=fulltext.split()
    wordd={}
    for wor in word:
        if wor in wordd:
            wordd[wor]+=1
        else:
            wordd[wor]=1
    s=sorted(wordd.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'Totalwords':len(a),'Wordy':len(word),'wordd': s})
def absts(request):
    return render(request,'about.html')
