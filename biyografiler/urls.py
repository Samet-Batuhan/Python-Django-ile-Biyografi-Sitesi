from django.urls import path
from . import views

#http://127.0.0.1:8000/
#http://127.0.0.1:8000/home                             --> Öne Çıkan Kişiler
#http://127.0.0.1:8000/sairler                          --> Şairler,Yazarlar,Sporcular
#http://127.0.0.1:8000/sairler/necip-fazil-kisakürek    --> Özel Sayfalar


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("home/<int:id>", views.kisidetay, name="kisidetay"),
    path("sairler", views.sairler, name="sairler"),
    path("sairler/<int:id>", views.sairdetay, name="sairdetay"),
    path("muzisyenler", views.muzisyenler, name="muzisyenler"),
    path("muzisyenler/<int:id>", views.muzisyendetay, name="muzisyendetay"),
    path("sporcular", views.sporcular, name="sporcular"),
    path("sporcular/<int:id>", views.sporcudetay, name="sporcudetay"),
    path("hakkinda", views.hakkinda, name="hakkinda"),
    path("oyuncular", views.oyuncular, name="oyuncular"),
    path("oyuncular/<int:id>", views.oyuncudetay, name="oyuncudetay"),
    path("tarihciler", views.tarihciler, name="tarihciler"),
    path("tarihciler/<int:id>", views.tarihcidetay, name="tarihcidetay"),
] 