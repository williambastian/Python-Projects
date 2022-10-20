from django.urls import path
from . import views


urlpatterns = [
    # set url path to home page index.html
    path('', views.home, name='index'),
    # set url path to the Create New Account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # set url path to the Balance Sheet page BalanceSheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    # set url path to the Add New Transaction page AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction')
]