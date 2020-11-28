from django.shortcuts import render

posts = [
    {
        'author': 'VaibhavPotdar',
        'title': 'Blog 1',
        'content': 'First Post',
        'posted_date': 'November 20, 2020'
    },
    {
        'author': 'Admin',
        'title': 'Blog 2',
        'content': 'Second Post',
        'posted_date': 'November 28, 2020'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

