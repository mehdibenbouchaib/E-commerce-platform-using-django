from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from accounts.views import signup, logout_user, login_user
from store.views import index, product_detail, cart,  add_to_cart, delete_cart

from shop import settings

urlpatterns = [
                  path('', index, name='index'),
                  path('admin/', admin.site.urls),
                  path('signup/', signup, name="signup"),
                  path('logout/', logout_user, name="logout"),
                  path('login/', login_user, name="login"),
                  path('cart/', cart, name="cart"),
                  path('cart/delete/', delete_cart, name="delete-cart"),
                  path('product/<str:slug>', product_detail, name="product"),
                  path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
