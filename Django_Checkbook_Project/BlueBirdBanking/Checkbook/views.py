from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# This function renders the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # Retrieve Transaction Form
    #  Check if method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # If the form is submitted, retrieve which account the user wants to view
        return balance(request, pk)  # call balance function to render that account's Balance Sheet
    content = {'form': form}  # Pass content to the template in a dictionary
    #  Adds content of form to page
    return render(request, 'checkbook/index.html', content)


# This function renders the home page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieve the Account form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check to see if submitted form is valid and if so, saves the form
            form.save()  # saves new account
            return redirect('index')  # returns user back to the home page
    content = {'form': form}  # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# This function renders the home page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # Retrieve the requested account by using its primary key
    transactions = Transaction.Transactions.filter(account=pk)  # Retrieve all of that account's transactions
    current_total = account.initial_deposit  # Create account total variable, starting with initial deposit value
    table_contents = {}  # Create a dictionary into which transaction information will be placed
    for t in transactions:  # Loop through transactions and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # If transaction is a deposit, add that amount to balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
        else:
            current_total -= t.amount  # If transaction is a withdrawal, subtract that amount from balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
    # Pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function renders the home page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # retrieve the Transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check to see if submitted form is valid and if so, saves the form
            pk = request.POST['account']  # Retrieve which account the transaction was for
            form.save()  # saves new account
            return balance(request, pk)  # renders balance of the account's Balance Sheet
    content = {'form': form}  # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)
