# Generated by Django 3.2 on 2021-05-15 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Setup', '0005_auto_20210430_0052'),
        ('Transaction', '0004_auto_20210427_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='cash_in',
            fields=[
                ('cash_in_id', models.AutoField(primary_key=True, serialize=False)),
                ('cash_in_code', models.IntegerField(blank=True)),
                ('cash_in_date', models.DateField(auto_now_add=True)),
                ('cash_in_notes', models.CharField(blank=True, max_length=1000, null=True)),
                ('cash_in_paid', models.FloatField(blank=True, null=True)),
                ('Customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Setup.customer')),
                ('Supplier_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Setup.supplier')),
            ],
        ),
    ]