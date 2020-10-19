from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from braces.views import SelectRelatedMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from . import models

User = get_user_model()


class UserStocks(generic.ListView):
    model = models.Stock
    template_name = 'stocks/user_stock_list.html'

    def get_queryset(self):
        try:
            self.stock_user = User.objects.prefetch_related('stocks').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.stock_user.stocks.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stock_user'] = self.stock_user
        return context


class CreateStock(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('ticker',)
    model = models.Stock

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.lookup()
        return super().form_valid(form)


class DeleteStock(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Stock
    select_related = ('user',)

    def get_success_url(self):
        return reverse_lazy('stocks:for_user', kwargs={"username": self.object.user.__str__()})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Stock deleted')
        return super().delete(*args, **kwargs)


class StockDetail(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
    model = models.Stock
    select_related = ('user',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


# class StockUpdate(LoginRequiredMixin, SelectRelatedMixin):
#     model = models.Stock
#     select_related = ('user', )
#     fields = ('ticker',)
#
#     def get_success_url(self):
#         return reverse_lazy('stocks:for_user', kwargs={"username": self.object.user.__str__()})

def stockupdate(request, username, pk):

    stock = get_object_or_404(models.Stock, id=pk)
    stock.lookup()
    stock.save()
    # form = models.Stock(request.POST or None, instance=stock)
    return redirect('stocks:for_user', username=stock.user.__str__())
