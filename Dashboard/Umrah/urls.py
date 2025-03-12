from django.urls import path
from . import views  # Ensure views is imported

urlpatterns = [
    path('', views.Index, name='umrah_home'),  # Example route
    # Add your other routes here...
]