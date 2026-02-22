from django.urls import path
from gold_app import views


app_name = 'gold_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('blog', views.blog, name='blog'),
    path('detail', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path("quote/", views.get_quote, name="quote"),

]