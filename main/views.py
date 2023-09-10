from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Bonaparte',
        'class': 'Stealth Assasin'
    }

    return render(request, "main.html", context)