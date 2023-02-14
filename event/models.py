from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

'''
# Expense Object Manager
class ExpenseManger(models.Manager):
    ## return a list of last ten expenses from all categories
    def last_ten(self, user):
        return self.filter(user=user, deleted=False).order_by('-pk')[:10:1]
    ## full list of user expenses
    def user_expenses(self, user):
        return self.filter(user=user, deleted=False).order_by('-pk')
    ## summary of CURRENT month expenses by categpry_type
    def categories_summary(self, user):
        current_month = datetime.now().month
        month_expenses = self.filter(user=user, date__month=current_month, deleted=False).values('category_type__name' , 'category_type__icon', 'category_type__color').annotate(total=Sum('amount')).order_by('-total')
        summary = month_expenses
        return summary
    ## summary of LAST month expenses by categpry_type
    def categories_summary_last(self, user):
        last_month = datetime.now().month - 1
        last_expenses = self.filter(user=user, date__month=last_month, deleted=False).values('category_type__name' , 'category_type__icon', 'category_type__color').annotate(total=Sum('amount')).order_by('-total')
        summary = last_expenses
        return summary
    ## summary of CURRENT month expenses by payment method
    def payments_summary(self, user):       
        current_month = datetime.now().month
        summary = self.filter(user=user, date__month=current_month, deleted=False).values('payment__name').annotate(total=Sum('amount')).order_by('-total')
        return summary
    ## summary of Last month expenses by payment method
    def payments_summary_last(self, user):
        last_month = datetime.now().month - 1
        summary = self.filter(user=user, date__month=last_month, deleted=False).values('payment__name').annotate(total=Sum('amount')).order_by('-total')
        return summary


# Expense object
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=True, )
    amount = models.PositiveIntegerField()
    currency = models.CharField('Currency', max_length=3, choices = [('EGP', 'EGP'), ('USD', 'USD'), ('EUR', 'EUR'), ('AED', 'AED')])
    deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_type = models.ForeignKey(Category_type, null=True, blank=True, on_delete=models.CASCADE)
    note = models.CharField(max_length=140, null=True, blank=True)
    payment = models.ForeignKey(Payment, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField('Type', max_length=12, choices = [('S', 'Subsription'), ('I', 'Installment'), ('E', "Expense")], default='E')
    objects = ExpenseManger()
    def __str__(self):
        return f"{self.category} , {self.amount}"

# ExpenseForm
class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'currency', 'category', 'note', 'deleted', 'payment')
'''