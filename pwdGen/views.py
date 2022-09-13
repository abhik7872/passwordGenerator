from django.shortcuts import render

data = [
    {
        'for': 'facebook',
        'password': '13@fdSgg89W',
    },
    {
        'for': 'netflix',
        'password': '434@%#hjgAfgh',
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': data,
    }
    return render(request, 'pwd/home.html', context)