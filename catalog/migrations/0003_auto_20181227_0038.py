# Generated by Django 2.1.4 on 2018-12-26 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20181226_2337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'ordering': ['name', 'start_time']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='auction',
            name='category',
        ),
        migrations.AddField(
            model_name='auction',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Select a category for this auction', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('ART', 'Art'), ('CL', 'Closed'), ('AN', 'Antique'), ('AU', 'Auto'), ('CO', 'Coin')], default='OP', help_text='Enter a category of auction (e.g. Charity, Electronics etc.)', max_length=200),
        ),
    ]
