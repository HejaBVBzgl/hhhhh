# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from models import Book, Author
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelForm
class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = "__all__"
		
def add_book(request):
	form = BookForm()
	if request.method == 'POST':
		form = BookForm(request.POST)
        if form.is_valid():
			form.save()
			return HttpResponse("success!")
	else:
		form = BookForm()
	return render(request, "add_book.html",{"form":form})
	
@csrf_exempt
def main_book(request):
	if request.method == 'POST':
		if 'delete' in request.POST:
			isbn = request.POST['delete']
			book = Book.objects.get(ISBN = isbn)
			book.delete()
	books = Book.objects.all()
	return render(request, "main_book.html",{'books':books})
	
def more(request,i):
	isbn = i
	book = Book.objects.get(ISBN = isbn)
	return render(request, "more.html",{'book':book})
	
def lookfor(request):
	if request.method == "GET":
		if 'hh' in request.GET and request.GET['hh']:
			name = request.GET['hh']
			z = Author.objects.filter(name = name)
			if z:
				author = Author.objects.get(name = name)
				books = author.book_set.all()
				return render(request,"lookfor.html",{'Author':author,'books':books})
		return render(request,"lookfor.html")
	return render(request,"lookfor.html")
	
def addauthor(request):
        form = AuthorForm()
	if request.method == 'POST':
		form = AuthorForm(request.POST)
        if form.is_valid():
			form.save()
			return HttpResponseRedirect('/main_book')
	else:
		form = AuthorForm()
	return render(request, "addauthor.html",{"form":form})
	
def back(request):
	return HttpResponse("success!")
	
def back(request):
	return HttpResponse("success!")
	
def back(request):
	return HttpResponse("success!")