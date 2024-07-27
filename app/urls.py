from django.urls import path,include
from app import views

urlpatterns =[
    path('product',views.product),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('search',views.search),
    path('product_details/<pid>',views.product_details),
    path('addtocart/<pid>',views.addtocart),
    path('cart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('remove/<cid>',views.removecart),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('detailsdata',views.detailsdata),
    path('history',views.history),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.success),


    # path('addform',views.addform),
    

]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings .MEDIA_ROOT)
