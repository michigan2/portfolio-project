from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
	blog = Blog.objects
	return render(request, 'blog/allblogs.html', {'blog': blog})

def detail(request, blog_id):
	# Must specify the model and then primary key (pk)
	detailblog = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blog/detail.html', {'blog': detailblog})