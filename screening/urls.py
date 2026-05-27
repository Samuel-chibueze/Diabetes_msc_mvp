from django.urls import path

from .views import (
    home,
    result,
    history,
    patient_detail,
    metrics,
    about
)

urlpatterns = [

    path(
        '',
        home,
        name='home'
    ),

    path(
        'result/<int:patient_id>/',
        result,
        name='result'
    ),

    path(
        'history/',
        history,
        name='history'
    ),

    path(
        'patient/<int:patient_id>/',
        patient_detail,
        name='patient_detail'
    ),

    path(
        'metrics/',
        metrics,
        name='metrics'
    ),

    path(
        'about/',
        about,
        name='about'
    ),
]