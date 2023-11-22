import datetime
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from main.models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
# Create your views here.

@login_required(login_url='/login')
def show_main(request):

    items = Item.objects.filter(user=request.user)
    context = {
        'user' : request.user.username,
        #'role': 'Stealth Assasin',
        'items': items,
        'last_login' : request.COOKIES['last_login'],
    }
    
    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount_button(request, item_id):
    item = get_object_or_404(Item, pk=item_id) #Mengakses item yang ingin dimodifikasi
    item.user = request.user; 
    if item.amount > 0:
        item.amount += 1
        item.save()
    return redirect('main:show_main')

def reduce_amount_button(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.user = request.user;
    if item.amount > 1:
        item.amount -= 1
        item.save()
    else:
        item.delete();
    return redirect('main:show_main')

def edit_item(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def remove_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.user = request.user;
    item.delete()
    return redirect('main:show_main')

    
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_item_json(request):
    item = Item.objects.filter(user=request.user)
    item.user = request.user
    return HttpResponse(serializers.serialize('json', item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get("name")
        description = request.POST.get("description")
        category = request.POST.get("category")
        amount = request.POST.get("amount")


        new_item = Item(user = user,name=name,description=description, category=category, amount=amount)
        new_item.user = request.user
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def remove_item_button(request, item_id):
    if request.method == 'DELETE':
        item = Item.objects.get(pk=item_id)
        item.user = request.user
        item.delete()
        return HttpResponse(b"REMOVED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            description = data["description"],
            category = data["category"],
            amount = int(data["amount"]),
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)