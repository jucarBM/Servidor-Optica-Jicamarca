"""Users Home"""

# Django
from django.urls import path

# View
from home import views


urlpatterns = [

    # Management
    path(
        route='',
        view=views.index,
        name='home'
    )
]

