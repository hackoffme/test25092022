from django.views.generic import ListView
from django.db.models import Sum
from parse_doc.models import Orders


class OrdersView(ListView):
    model = Orders
    context_object_name = 'order_list'
    template_name = 'singlpage/list.html'

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        ret['total'] = Orders.objects.aggregate(Sum('price'))['price__sum']
        ret['values'] = [[str(item.delivery_time), int(item.price)]
                         for item in Orders.objects.all()]
        return ret
