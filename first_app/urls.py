from django.conf.urls import url
from first_app import views

urlpatterns=[
    url(r'^$',views.form_name_view,name='form_name_view'),
]