from django.urls import path
from gestion import views


urlpatterns = [


    # MEDIAS

    path('medias/', views.listmedia, name='listmedia'),
    path('medias/addmedia/', views.addmedia, name='addmedia'),
    path('medias/updatemedia/<cat>/', views.updatemedia, name='updatemedia'),
    path('medias/deletemedia/<cat>/', views.deletemedia, name='deletemedia'),


    # ITEMS

    path('medias/<cat>/list/', views.listitem, name='listitem'),
    path('medias/<cat>/additem/', views.additem, name='additem'),
    path('medias/<cat>/updateitem/<int:id>/', views.updateitem, name='updateitem'),
    path('medias/<cat>/deleteitem/<int:id>/', views.deleteitem, name='deleteitem'),
    path('medias/<cat>/lenditem/<int:id>/', views.lenditem, name='lenditem'),
]