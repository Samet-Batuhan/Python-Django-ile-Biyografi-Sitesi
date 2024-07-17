from django.shortcuts import render
from .forms import AddLinkForm
from .models import Category,OneCikan,Sair,Muzisyen,Sporcu,Oyuncu,Tarihci,Link


def home(request):
    data = {
        "kisiler" : OneCikan.objects.all(),
    }
    return render(request, "index.html",data)

def sairler(request):
    data = {
        "sairler" : Sair.objects.all(),
    }
    return render(request, "sairler.html",data)

def muzisyenler(request):
    data = {
        "muzisyenler" : Muzisyen.objects.all(),
    }
    return render(request, "muzisyenler.html",data)

def sporcular(request):
    data = {
        "sporcular" : Sporcu.objects.all(),
    }
    return render(request, "sporcular.html",data)
    
def oyuncular(request):
    data = {
        "oyuncular" : Oyuncu.objects.all(),
    }
    return render(request, "oyuncular.html",data)

def tarihciler(request):
    data = {
        "tarihciler" : Tarihci.objects.all(),
    }
    return render(request, "tarihciler.html",data)
    
def hakkinda(request):
    data = {
        "hakkinda": hakkinda,
    }
    return render(request, "hakkinda.html",data)

    
    
def kisidetay(request,id):
    data = {
        "kisi": OneCikan.objects.get(id=id)
    }
    return render(request, "kisidetay.html",data)

def sairdetay(request,id):
    data = {
        "sair": Sair.objects.get(id=id)
    }
    return render(request, "sairdetay.html",data)
   
def muzisyendetay(request,id):
    data = {
        "muzisyen": Muzisyen.objects.get(id=id)
    }
    return render(request, "muzisyendetay.html",data)

def sporcudetay(request,id):
    data = {
        "sporcu": Sporcu.objects.get(id=id)
    }
    return render(request, "sporcudetay.html",data)

def oyuncudetay(request,id):
    data = {
        "oyuncu": Oyuncu.objects.get(id=id)
    }
    return render(request, "oyuncudetay.html",data)

def tarihcidetay(request,id):
    data = {
        "tarihci": Tarihci.objects.get(id=id)
    }
    return render(request, "tarihcidetay.html",data)





def home_view(request):
    no_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Ups ... couldn't get the name or the price"
        except:
            error = "Ups ... someting went wrong"

    form = AddLinkForm()

    qs = Link.objects.all()
    items_no = qs.count()

    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        'qs' : qs,
        'items_no' : items_no,
        'no_discounted' : no_discounted,
        'form' : form,
        'error' : error,

    }

    return render(request, 'links/main.html', context)
