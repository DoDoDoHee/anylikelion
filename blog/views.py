from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
from .forms import BlogForms
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

@login_required
def new(request):
    if request.method == 'POST':
        forms = BlogForms(request.POST)

        if forms.is_valid:
            forms.save()
        return redirect('home')

    forms = BlogForms()
    return render(request, 'new.html', {'forms':forms})

def detail(request, blog_id):
    blog_one = get_object_or_404(Blog, id=blog_id)
    return render(request, 'detail.html', {'blog_one':blog_one})

@login_required
def update(request, blog_id):
    blog_update = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        forms = BlogForms(request.POST, instance=blog_update)

        if forms.is_valid:
            forms.save()
        return redirect('home')

    forms = BlogForms(instance=blog_update)
    return render(request, 'new.html', {'forms':forms})

@login_required
def delete(request, blog_id):
    blog_delete = get_object_or_404(Blog, id=blog_id)
    blog_delete.delete()
    return redirect('home')