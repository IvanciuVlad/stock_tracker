from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from iexfinance.stocks import Stock as LibStock
from django.conf import settings
User = get_user_model()


class Stock(models.Model):
    user = models.ForeignKey(User, related_name='stocks', on_delete=models.DO_NOTHING, null=True, blank=True,)
    ticker = models.CharField(max_length=4)
    last_value = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    company_name = models.CharField(max_length=96)

    def __str__(self):
        return self.ticker

    def lookup(self):
        print(settings.IEX_TOKEN)
        stock = LibStock(self.ticker, token=settings.IEX_TOKEN)
        stock_attributes = stock.get_quote()
        print(stock_attributes)
        self.last_value = stock_attributes['latestPrice']
        self.company_name = stock_attributes['companyName']

    def get_absolute_url(self):
        return reverse('stocks:for_user', kwargs={'username': self.user.username})

    class Meta:
        ordering = ['ticker']
