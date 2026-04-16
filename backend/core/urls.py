from django.urls import path
from prompts import views

urlpatterns = [
    path('prompts/', views.get_prompts),
    path('prompts/', views.create_prompt),
    path('prompts/<int:id>/', views.get_prompt_detail),
]
