from django.urls import path ,include
from .import views
urlpatterns = [
    path('', views.main),
    path('regist', views.regist),
    path('login', views.login),
    path('logout', views.logout),
    path('dashbord', views.dashbord),
    path('addtree',views.addtree),
    path('forplantree',views.forplantree),
    path('mytree',views.mytree),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('details/<int:id>',views.details),
    path('addvistor/<int:id>',views.addvistor),









    # path('loggedin',views.loggedin),
    # path('delfav/<int:id>',views.delfav),
    # path('addtofavsho/<int:id>',views.addtofavsho),
    # path('bookshow/<int:id>',views.bookshow),
    # path('addtofav/<int:id>',views.addtofav),
    # path('favoritbook', views.favoritbook),
    # path('books', views.books),
    # path('edit',views.edit),
    # path('goback',views.goback),
    # path('showall',views.showall),
    # path('gotobooks',views.gotobooks)

]
