
# -*- coding: utf-8 -*-

from django.urls import include, path


urlpatterns = [
    path('api/', include(router.urls)),  # DEPRECATED, used by mobile v0.2.0
]
