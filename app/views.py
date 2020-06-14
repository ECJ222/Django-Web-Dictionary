from django.shortcuts import render,redirect
from PyDictionary import PyDictionary
from .forms import search
# Create your views here.
def index(request):
	try:
		if request.method == 'POST':
			name=request.POST['name']
			es=PyDictionary()
			meaning=es.meaning(name)
			phrase=list(meaning)[0]
			definition=meaning[list(meaning)[0]]
			print(phrase)
			print(definition)
			context={'phrase':phrase,'definition':definition,'name':name}
		else:
			context={}
		return render(request,'index.html',context)
	except Exception:
		unkwown={'Exception':Exception()}
		return render(request,'index.html',unkwown)
