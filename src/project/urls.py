"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings

from django.conf.urls.static import static

from django.conf.urls import url, include

from django.contrib import admin

from django.views.generic import TemplateView

from django.urls import reverse_lazy

#login
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    )

from items.views import HomeView, ClaimedView

from profiles.views import RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^locations/', include('locations.urls', namespace='locations')),
    url(r'^items/', include('items.urls', namespace='items')),
    url(r'^u/', include('profiles.urls', namespace='profile')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^claimed/$', ClaimedView.as_view(), name='claimed'),


    # login
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^login/$', LoginView.as_view(template_name='registration/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),

    #  # register
    url(r'^register/$', RegisterView.as_view(), name='register'),

    url(r'^password_change/$', PasswordChangeView.as_view(template_name='registration/password_change_form.html'),name='password_change'),
    url(r'^password_change/done/$', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    url(r'^password_reset/$', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)