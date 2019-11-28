import django_tables2 as tables
from django.urls import reverse
import itertools
from .models import RevenueRecord
from django.utils.safestring import mark_safe
from django.conf.urls import url

class NumberColumn(tables.Column):
    def render(self, value):
        return '{:0.2f}'.format(value)

class DateColumn(tables.Column):
    def render(self, value):
        return mark_safe('<a href="{0}">{0}</a>'.format(value))

class RevenueTable(tables.Table):
    #date = tables.DateTimeColumn(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})
    date = DateColumn(attrs={"th": {"style": "background-color:lightgray"}})
    #date = tables.LinkColumn('demo:second', args=[], attrs={"th": {"style": "background-color:lightgray"}})
    #date = tables.Column(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})
    revenue_sum = NumberColumn(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})
    clicks_sum = tables.Column(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})
    #publisher = tables.Column(attrs={"th": {"style": "background-color:lightgray"}})
    #source = tables.Column(attrs={"th": {"style": "background-color:lightgray"}})

    class Meta:
        model =  RevenueRecord
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': "table table-striped"}
        order_by = '-date'
        fields = ("date","revenue_sum","clicks_sum")
        #fields = ("date","publisher__name","source__name","revenue_sum","clicks_sum")

    #idx = tables.Column(empty_values=(), orderable=False)
    #def render_idx(self):
    #    self.row_counter = getattr(self, 'row_counter', itertools.count(1))
    #    return next(self.row_counter)

