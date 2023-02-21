from django.db import models


# create Account model
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    # Defines model manager for Accounts
    Accounts = models.Manager()

    # Allows references to a specific account to be returned as owner's name instead of as primary key
    def __str__(self):
        return self.first_name + ' ' + self.last_name


# Choices for a transaction
TransactionTypes = [('Deposit', 'Deposit'), ('Withdrawal', 'Withdrawal')]


# Creates the Transaction Model
class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # defines model manager for Transactions
    Transactions = models.Manager()
