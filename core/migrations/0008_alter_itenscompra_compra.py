# Generated by Django 4.0.5 on 2022-06-29 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_compra_status_itenscompra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itenscompra',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.compra'),
        ),
    ]