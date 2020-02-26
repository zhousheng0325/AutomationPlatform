from django.urls import path
from .views import InterfaceModuleView, InterfaceView, KeysView, InterfaceGetCaseView, InterfacExecuteResult

urlpatterns = [
     path('modules/',InterfaceModuleView.as_view({'get':'list','post':'create'})),
     path('modules/<int:pk>/',InterfaceModuleView.as_view({'put':'update'})),
     path('interfaces/',InterfaceView.as_view({'get':'list','post':'create','delete': 'delete'})),
     path('interfaces/<int:pk>/', InterfaceView.as_view({'get':'retrieve','put': 'update'})),
     path('interfaces/case/<int:pk>/',InterfaceGetCaseView.as_view()),
     path('keys/',KeysView.as_view({'get':'list'})),
     path('interfaces/execute/',InterfacExecuteResult.as_view())
]