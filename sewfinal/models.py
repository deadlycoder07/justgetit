from django.db import models

# Create your models here.

Factory = (
    ('factory1', 'factory1'),
    ('factory2', 'factory2'),
    ('factory3', 'factory3'),
    ('factory4', 'factory4'),
    ('factory5', 'factory5'),
)

Fabric_choices = (
    ('woven', 'Woven'),
    ('knit', 'Knit'),
    ('others', 'Others')
)

Wash = (
    ('non-wash', 'Non-Wash'),
    ('wash', 'Wash'),
)

Style = (
    ('formal', 'Formal'),
    ('casual', 'Casual'),
)


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.name


class SuperCategory(models.Model):
    name = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FabricDetails(models.Model):
    pfmno = models.CharField(max_length=100)
    factory = models.CharField(max_length=100, default="0", choices=Factory)
    fabric = models.CharField(max_length=100, default="0", choices=Fabric_choices)
    wash = models.CharField(max_length=100, default="0", choices=Wash)
    category = models.CharField(max_length=200, null=True)
    subcategory = models.CharField(max_length=200, null=True)
    supercategory = models.CharField(max_length=200, null=True)
    styletype = models.CharField(max_length=100, default="0", choices=Style)


class Components(models.Model):
    comp = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.comp


class Attributes(models.Model):
    name = models.CharField(max_length=200, null=True)
    comp = models.ManyToManyField(Components, blank=True)

    def __str__(self):
        return self.name


class StyleDetails(models.Model):
    pfmno = models.ForeignKey(FabricDetails, on_delete=models.CASCADE)
    comp = models.CharField(max_length=200)
    attribute = models.CharField(max_length=200)
    operations = models.CharField(max_length=100)
    complexity = models.IntegerField(default="1")
    spi = models.IntegerField(default="12")
    stitch_length = models.IntegerField(default="3")
    thread_consumption = models.IntegerField()
    machine_auto = models.CharField(max_length=100, default="SNLS")
    work_aid = models.CharField(max_length=100, default="BINDER")
    smv = models.DecimalField(max_digits=6, default="0.33", decimal_places=5)
    allowance = models.DecimalField(max_digits=6, decimal_places=5)
    sam = models.DecimalField(max_digits=6, default="0.53", decimal_places=5)
    ct = models.DecimalField(max_digits=6, default="0.88", decimal_places=5)
    grade = models.CharField(max_length=100)
    comp = models.CharField(max_length=200)
    attribute = models.CharField(max_length=200)


class OrderDetails(models.Model):
    orderno = models.CharField(max_length=100,unique=True)
    styleno = models.CharField(max_length=100,unique=True)
    lineno = models.CharField(max_length=100)
    order_quantity = models.IntegerField()
    mins_shift = models.IntegerField()
    capacity = models.IntegerField()
    expected_skill_level = models.IntegerField()
    target = models.IntegerField()
    fabric = models.CharField(max_length=100, default="0", choices=Fabric_choices,blank=True)
    wash = models.CharField(max_length=100, default="0", choices=Wash,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True)
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True)
    supercategory = models.ForeignKey(SuperCategory,on_delete=models.CASCADE,blank=True)
    styletype = models.CharField(max_length=100, default="0", choices=Style,blank=True)
    comp = models.ForeignKey(Components,on_delete=models.CASCADE,blank=True)
    attribute = models.ForeignKey(Attributes,on_delete=models.CASCADE,blank=True)

class Obgenerate(models.Model):
    orderno=models.CharField(max_length=190)
    styleno = models.CharField(max_length=100)
    operations = models.CharField(max_length=100)
    complexity = models.IntegerField(default="1")
    spi = models.IntegerField(default="12")
    stitch_length = models.IntegerField(default="3")
    thread_consumption = models.IntegerField()
    machine_auto = models.CharField(max_length=100, default="SNLS")
    work_aid = models.CharField(max_length=100, default="BINDER")
    smv = models.DecimalField(max_digits=6, default="0.33", decimal_places=5)
    allowance = models.DecimalField(max_digits=6, decimal_places=5)
    sam = models.DecimalField(max_digits=6, default="0.53", decimal_places=5)
    ct = models.DecimalField(max_digits=6, default="0.88", decimal_places=5)
    grade = models.CharField(max_length=100)
    mpno = models.IntegerField()
    mpalloc = models.IntegerField()
    Name = models.CharField(max_length=190,blank=True)
    oph = models.IntegerField()
    cost = models.IntegerField()


