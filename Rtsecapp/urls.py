from django.conf.urls import url

app_name = 'Rtsecapp'
from views import *
urlpatterns = [
    url(r'login', Login.as_view(), name="login"),
    url(r'arp', Arp.as_view(), name="arp"),
    url(r'dos', Dos.as_view(), name="dos"),
    url(r'com', Command.as_view(), name="com"),
    url(r'cha', Change.as_view(), name="cha"),
    url(r'law', Lawless.as_view(), name="law"),
    url(r'^',Base.as_view(),name='base'),
]