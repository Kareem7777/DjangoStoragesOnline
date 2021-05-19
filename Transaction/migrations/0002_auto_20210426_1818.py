# Generated by Django 3.2 on 2021-04-26 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Setup', '0004_alter_items_items_name'),
        ('Transaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail_in',
            name='Items_Items_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.items'),
        ),
        migrations.AddField(
            model_name='detail_in',
            name='Master_in_master_in_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Transaction.master_in'),
        ),
        migrations.AddField(
            model_name='detail_out',
            name='Items_Items_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.items'),
        ),
        migrations.AddField(
            model_name='detail_out',
            name='Master_out_master_out_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Transaction.master_out'),
        ),
        migrations.AddField(
            model_name='master_in',
            name='Customer_Customer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.customer'),
        ),
        migrations.AddField(
            model_name='master_in',
            name='Storage_Storage_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.storage'),
        ),
        migrations.AddField(
            model_name='master_out',
            name='Customer_Customer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.customer'),
        ),
        migrations.AddField(
            model_name='master_out',
            name='Storage_Storage_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.storage'),
        ),
        migrations.AddField(
            model_name='master_out',
            name='Supplier_Supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.supplier'),
        ),
        migrations.AlterField(
            model_name='master_in',
            name='Supplier_Supplier_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Setup.supplier'),
        ),
    ]