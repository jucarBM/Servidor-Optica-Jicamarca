"""Users Home"""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [

    # Management
    path(
        route='signin',
        view=views.signin,
        name='signin'
    ),
    path(
        route='signup',
        view=views.signup,
        name='signup'
    )
]