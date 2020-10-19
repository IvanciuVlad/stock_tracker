from . import models
from django.views import generic


# Create your views here.
class CryptoList(generic.ListView):
    model = models.Crypto
    template_name = 'crypto/currencies_list.html'