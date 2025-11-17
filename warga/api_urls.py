# warga/api_urls.py
from django.urls import path
from .views import WargaListAPIView, WargaCreateAPIView, WargaDetailAPIView
from rest_framework.routers import DefaultRouter
from .views import WargaViewSet, PengaduanViewSet, LoginViewSet

# Buat sebuah router dan daftarkan ViewSet kita
router = DefaultRouter()
router.register(r'warga', WargaViewSet, basename='warga')
router.register(r'pengaduan', PengaduanViewSet, basename='pengaduan')
router.register('login', LoginViewSet, basename='login')


urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/tambah/', WargaCreateAPIView.as_view(), name='warga-create'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='warga-detail'),
    path('', include(router.urls)),
]
