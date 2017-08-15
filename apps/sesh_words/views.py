from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
# the index function is called when root is visited
def index(request):
	return render(request, 'sesh_words/index.html')

def add(request):
	request.session['word']=request.POST['word_form']
	print request.session['word']
	context = {
  	"time": strftime("added on %I:%M %p %b %d %Y", localtime())
  	}
  	# print context['time'] USE THE KEY TIME TO GET EXACT time word is added
	return redirect("/")