# Generated by Django 3.2.6 on 2021-09-07 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0013_auto_20210823_0345'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='state',
            field=models.SmallIntegerField(choices=[(0, 'OPEN'), (1, 'PROCESSING'), (2, 'DONE'), (3, 'ARCHIVED')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.SmallIntegerField(choices=[(0, 'OPEN'), (1, 'PROCESSING'), (2, 'DONE'), (3, 'ARCHIVED')], default=0),
        ),
        migrations.CreateModel(
            name='FoodLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.SmallIntegerField(choices=[(0, 'OPEN'), (1, 'PROCESSING'), (2, 'DONE'), (3, 'ARCHIVED')], default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('orderline', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pos.orderline')),
            ],
            options={
                'unique_together': {('orderline', 'state')},
            },
        ),
    ]