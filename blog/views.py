from django.shortcuts import render

def post_list(request): #takes the request and retuns it value it gets from another function render that will render our template
    return render(request, 'blog/post_list.html', {})

# Create your views here.
