from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from producthunt import settings
from products import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', include('products.urls'), name='products'),
    path('accounts/', include('accounts.urls'), name='accounts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
