from django.contrib import admin
from django.urls import path,include
from sakhi import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', views.registrationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='home'),
    path('contact',views.cont,name='contact'),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('restapi', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
   
]
