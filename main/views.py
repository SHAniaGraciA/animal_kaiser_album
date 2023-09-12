from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'char_name' : 'Bonaparte',
        'role': 'Stealth Assasin',
        'items': [
            {
                'name': 'Smoke Bomb',
                'description': 'Use it to easily dissapear from enemy sight ',
                'category': 'Throwable',
                'amount': 5,
                
            },
            {
                'name': 'Bandage',
                'description': 'Use it to heal your wound and recover 35 HP',
                'category': 'Consumable',
                'amount': 3,
        
            },
            {
                'name': 'Money',
                'description': 'Use it to fulfill your needs without rob & kill',
                'category': 'Tradeable',
                'amount': 900,
            },
            {
                'name': 'Golden Chest',
                'description': 'Open it to get some rewards after completing mission',
                'category': 'Other',
                'amount': 10,
            },
            
        ]
    }
    

    return render(request, "main.html", context)