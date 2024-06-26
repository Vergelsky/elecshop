# Generated by Django 5.0.6 on 2024-06-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplychainparticipant',
            name='contact',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукты', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterModelOptions(
            name='supplychainparticipant',
            options={'verbose_name': 'Участник цепи поставок', 'verbose_name_plural': 'Участники цепи поставок'},
        ),
        migrations.AddField(
            model_name='supplychainparticipant',
            name='building',
            field=models.CharField(default='sdsf', max_length=100, verbose_name='Дом'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplychainparticipant',
            name='city',
            field=models.CharField(default='asd', max_length=100, verbose_name='Город'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplychainparticipant',
            name='country',
            field=models.CharField(default='asdasd', max_length=100, verbose_name='Страна'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supplychainparticipant',
            name='street',
            field=models.CharField(default='asd', max_length=300, verbose_name='Улица'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='supplychainparticipant',
            name='debt',
            field=models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Задолженность'),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
