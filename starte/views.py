from django.shortcuts import render

posts =[
    {
        'author': 'mary',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted':'December 25,2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted':'December 25,2020'
    }
]

def home(request):
    context ={
        'posts':posts
    }
    return render(request, 'home.html',context)
def about(request):
    return render(request, 'about.html', {'title': 'About'})