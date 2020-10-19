from django.db import models
from django.conf import settings
from iexfinance.stocks import Stock as LibStock


# Create your models here.
class Crypto(models.Model):
    crypto_names = ['Bitcoin USD ', 'EOS USD ', 'Ethereum USD ', 'Ontology USD ', 'Cardano USD ', 'Ripple USD ',
                    'TrueUSD ', 'TRON USD ', 'Litecoin USD ', 'Ethereum Classic USD ', 'MIOTA USD ', 'ICON USD ',
                    'NEO USD ', 'VeChain USD', 'Stellar Lumens USD ', 'Qtum USD ']
    crypto_tickers = ['BTCUSDT', 'EOSUSDT', 'ETHUSDT', 'BNBUSDT', 'ONTUSDT', 'BCCUSDT', 'ADAUSDT', 'XRPUSDT', 'TUSDUSDT',
                      'TRXUSDT', 'LTCUSDT', 'ETCUSDT', 'IOTAUSDT', 'ICXUSDT', 'NEOUSDT', 'VENUSDT', 'XLMUSDT', 'QTUMUSDT']

    def lookup(self):
        for ticker in self.crypto_tickers:
            crypto = LibStock(ticker, token=settings.IEX_TOKEN)
            crypto_attributes = crypto.get_quote()
            print(crypto_attributes)