from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
  response = "placeholder to later display all the list of blogs"
  return HttpResponse(response)