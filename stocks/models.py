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
    week52High = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    week52Low = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    primary_exchange = models.CharField(max_length=10, null=True)
    company_name = models.CharField(max_length=96)
    ytd_change = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    pe_ratio = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    market_cap = models.CharField(max_length=128, null=True)
    logo = models.URLField(max_length=256, null=True)

    def __str__(self):
        return self.ticker

    def lookup(self):
        print(settings.IEX_TOKEN)
        stock = LibStock(self.ticker, token=settings.IEX_TOKEN)
        print(stock.get_logo())
        stock_attributes = stock.get_quote()
        print(stock_attributes)
        self.last_value = stock_attributes['latestPrice']
        self.company_name = stock_attributes['companyName']
        self.week52Low = stock_attributes['week52Low']
        self.week52High = stock_attributes['week52High']
        self.primary_exchange = stock_attributes['primaryExchange']
        self.pe_ratio = stock_attributes['peRatio']
        self.market_cap = stock_attributes['marketCap']
        self.ytd_change = stock_attributes['ytdChange']
        logo_link = stock.get_logo()
        self.logo = logo_link['url']

    def get_absolute_url(self):
        return reverse('stocks:for_user', kwargs={'username': self.user.username})

    class Meta:
        ordering = ['ticker']
