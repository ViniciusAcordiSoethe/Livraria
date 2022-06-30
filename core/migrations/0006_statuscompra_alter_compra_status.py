# Generated by Django 4.0.5 on 2022-06-29 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.statuscompra'),
        ),
    ]
