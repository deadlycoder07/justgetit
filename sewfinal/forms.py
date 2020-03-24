from django import forms

from django.forms import ModelForm
from .models import FabricDetails, Category, SubCategory, SuperCategory
from .models import Attributes, Components, StyleDetails
from .models import OrderDetails, Obgenerate
from .admin import *


class pfm(forms.ModelForm):
    class Meta:
        model = FabricDetails
        fields = '__all__'
        fields_order = ['pfmno', 'factory', 'fabric', 'wash', 'category', 'subcategory', 'supercategory', 'styletype']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class operations(forms.ModelForm):
    class Meta:
        model = StyleDetails
        fields = '__all__'
        fields_order = ['pfmno', 'comp', 'attribute', 'operations', 'complexity', 'spi', 'stitch_length',
                        'thread_consumption', 'machine_auto', 'work_aid', 'smv', 'allowance', 'sam', 'ct', 'grade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class orders(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = '__all__'
        fields_order = ['orderno', 'stno', 'lineno', 'order_quantity', 'mins_shift', 'capacity', 'expected_skill_level',
                        'target', 'fabric', 'wash', 'category', 'subcategory', 'supercategory', 'styletype', 'comp',
                        'attribute']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class obgen(forms.ModelForm):
    class Meta:
        model = Obgenerate
        fields = ['orderno','styleno','operations', 'complexity', 'spi', 'stitch_length', 'thread_consumption', 'machine_auto', 'work_aid',
                  'smv', 'allowance', 'sam', 'ct', 'grade', 'mpno', 'mpalloc', 'Name', 'oph', 'oph']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


