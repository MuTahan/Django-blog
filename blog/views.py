from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author':'Muhammad',
        'title':'blog post 1',
        'content':'first post content',
        'date_posted':'August 27,2019'
    },
    {

        'author':'Hisham',
        'title':'blog post 2',
        'content':'second post content',
        'date_posted':'August 2,2019'
    }
]

def home(request):
    contex = {
        'posts': posts
    }
    return render(request, 'blog/home.html',contex)

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})