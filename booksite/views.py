from django.shortcuts import render
from .models import Tale 

def tale_list(request):
	tale_list = Tale.objects.all()


	return render(request, 'booksite/index.html', {'tale_list' : tale_list})


def create_book(request, tale_id):
	tale=Tale.objects.get(id=tale_id)
	return render(request, 'booksite/create_book.html', {"tale":tale})

