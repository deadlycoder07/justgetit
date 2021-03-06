# Generated by Django 3.0.4 on 2020-03-18 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FabricDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pfmno', models.CharField(max_length=100)),
                ('factory', models.CharField(choices=[('factory1', 'factory1'), ('factory2', 'factory2'), ('factory3', 'factory3'), ('factory4', 'factory4'), ('factory5', 'factory5')], default='0', max_length=100)),
                ('fabric', models.CharField(choices=[('woven', 'Woven'), ('knit', 'Knit'), ('others', 'Others')], default='0', max_length=100)),
                ('wash', models.CharField(choices=[('non-wash', 'Non-Wash'), ('wash', 'Wash')], default='0', max_length=100)),
                ('category', models.CharField(max_length=200, null=True)),
                ('subcategory', models.CharField(max_length=200, null=True)),
                ('supercategory', models.CharField(max_length=200, null=True)),
                ('styletype', models.CharField(choices=[('formal', 'Formal'), ('casual', 'Casual')], default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Obgenerate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.CharField(max_length=190)),
                ('styleno', models.CharField(max_length=100)),
                ('operations', models.CharField(max_length=100)),
                ('complexity', models.IntegerField(default='1')),
                ('spi', models.IntegerField(default='12')),
                ('stitch_length', models.IntegerField(default='3')),
                ('thread_consumption', models.IntegerField()),
                ('machine_auto', models.CharField(default='SNLS', max_length=100)),
                ('work_aid', models.CharField(default='BINDER', max_length=100)),
                ('smv', models.DecimalField(decimal_places=5, default='0.33', max_digits=6)),
                ('allowance', models.DecimalField(decimal_places=5, max_digits=6)),
                ('sam', models.DecimalField(decimal_places=5, default='0.53', max_digits=6)),
                ('ct', models.DecimalField(decimal_places=5, default='0.88', max_digits=6)),
                ('grade', models.CharField(max_length=100)),
                ('mpno', models.IntegerField()),
                ('mpalloc', models.IntegerField()),
                ('Name', models.CharField(blank=True, max_length=190)),
                ('oph', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.ManyToManyField(blank=True, to='sewfinal.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sewfinal.Category')),
                ('sub_category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sewfinal.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='StyleDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operations', models.CharField(max_length=100)),
                ('complexity', models.IntegerField(default='1')),
                ('spi', models.IntegerField(default='12')),
                ('stitch_length', models.IntegerField(default='3')),
                ('thread_consumption', models.IntegerField()),
                ('machine_auto', models.CharField(default='SNLS', max_length=100)),
                ('work_aid', models.CharField(default='BINDER', max_length=100)),
                ('smv', models.DecimalField(decimal_places=5, default='0.33', max_digits=6)),
                ('allowance', models.DecimalField(decimal_places=5, max_digits=6)),
                ('sam', models.DecimalField(decimal_places=5, default='0.53', max_digits=6)),
                ('ct', models.DecimalField(decimal_places=5, default='0.88', max_digits=6)),
                ('grade', models.CharField(max_length=100)),
                ('comp', models.CharField(max_length=200)),
                ('attribute', models.CharField(max_length=200)),
                ('pfmno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sewfinal.FabricDetails')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderno', models.CharField(max_length=100)),
                ('styleno', models.CharField(max_length=100)),
                ('lineno', models.CharField(max_length=100)),
                ('order_quantity', models.IntegerField()),
                ('mins_shift', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('expected_skill_level', models.IntegerField()),
                ('target', models.IntegerField()),
                ('fabric', models.CharField(blank=True, choices=[('woven', 'Woven'), ('knit', 'Knit'), ('others', 'Others')], default='0', max_length=100)),
                ('wash', models.CharField(blank=True, choices=[('non-wash', 'Non-Wash'), ('wash', 'Wash')], default='0', max_length=100)),
                ('styletype', models.CharField(blank=True, choices=[('formal', 'Formal'), ('casual', 'Casual')], default='0', max_length=100)),
                ('attribute', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sewfinal.Attributes')),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sewfinal.Category')),
                ('comp', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sewfinal.Components')),
                ('subcategory', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sewfinal.SubCategory')),
                ('supercategory', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='sewfinal.SuperCategory')),
            ],
        ),
        migrations.AddField(
            model_name='attributes',
            name='comp',
            field=models.ManyToManyField(blank=True, to='sewfinal.Components'),
        ),
    ]
