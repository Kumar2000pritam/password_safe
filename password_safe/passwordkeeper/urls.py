from django.urls import path
from .views import index_view, add_view, decrypt_password,delete_password

urlpatterns = [
    path('', index_view,name="index_view"),
    path('add_view', add_view),
    path('decrypt/<int:id>', decrypt_password, name='decrypt_password'),
    path('delete_password/<int:id>', delete_password, name='delete_password'),
]
