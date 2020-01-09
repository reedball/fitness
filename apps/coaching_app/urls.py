from django.conf.urls import url
from . import views


from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [
    url(r'^login_page$', views.login_page),
    url(r'^regprocess$', views.user_process),
    url(r'^registration$', views.registration),
    url(r'^loginprocess$', views.login_process),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^$', views.home_page),
    url(r'^survey$', views.survey),
    url(r'^survey_reply$', views.survey_reply),
    url(r'^my_account$', views.my_account),
    url(r'^users/(?P<user_id>\d+)$', views.user_account),
    url(r'^no$', views.no_survey_reply),
    url(r'^user/update/(?P<userid>\w+)$', views.update),
    url(r'^user/edit/(?P<userid>\w+)$', views.edit_account),
    # url(r'^createpost$', views.createpost),
    url(r'^sampleworkout$', views.sampleworkout),
    url(r'^search', views.search),
    # url(r'^createpost$', views.createpost)
    url(r'^search', views.search),
    url(r'^createpost$', views.create_post),
    url(r'^newpost$', views.new_post),
    url(r'^remove/(?P<post_id>\d+)$', views.delete),
    url(r'^posts/(?P<post_id>\d+)$',views.view),

]

# urlpatterns = [ 
#     path('image_upload', post_image_view, name = 'image_upload'), 
#     path('success', success, name = 'success'),
    # path('post_images', display_hotel_images, name = 'post_images'),
# ] 

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
