import django_tables2 as tables
from .models import RevenueRecord
from django.utils.safestring import mark_safe
from django.utils.text import capfirst

class NumberColumn(tables.Column):
    def render(self, value):
        return '{:0.2f}'.format(value)

class DateColumn(tables.Column):
    def render(self, value):
        return mark_safe('<a href="{0}">{0}</a>'.format(value))

class DatePublisherColumn(tables.Column):
    def render(self, value, record):
        return mark_safe('<a href="{0}/{1}">{0}</a>'.format(value, record['publisher']))

class RevenueTable(tables.Table):
    date = DateColumn(attrs={"th": {"style": "background-color:lightgray"}})
    revenue_sum = NumberColumn(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})
    clicks_sum = tables.Column(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})

    class Meta:
        model =  RevenueRecord
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': "table table-striped"}
        order_by = '-date'
        fields = ("date","revenue_sum","clicks_sum")

class DateTable(tables.Table):
    date = DatePublisherColumn(attrs={"th": {"style": "background-color:lightgray"}})
    publisher__name = tables.Column(verbose_name="publisher",attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"},
                                           "td": {"style": "text-transform: capitalize"},
                                           })
    revenue_sum = NumberColumn(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})
    clicks_sum = tables.Column(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})

    class Meta:
        model =  RevenueRecord
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': "table table-striped"}
        fields = ("date","publisher__name","revenue_sum","clicks_sum")
        order_by = 'publisher__name'

class PublisherTable(tables.Table):
    source__name = tables.Column(verbose_name="source",attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"},
                                                              "td": {"style": "text-transform: capitalize"},
                                                            })
    revenue_sum = NumberColumn(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})
    clicks_sum = tables.Column(attrs={"th": {"style": "background-color:lightgray; text-transform: capitalize"}})

    class Meta:
        model = RevenueRecord
        template_name = "django_tables2/bootstrap.html"
        attrs = {'class': "table table-striped"}
        fields = ("source__name","revenue_sum","clicks_sum")
        order_by = 'source__name'

