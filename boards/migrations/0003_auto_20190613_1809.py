# Generated by Django 2.2.2 on 2019-06-13 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20190613_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boards',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cards',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lists',
            name='boardid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='boards.Boards'),
        ),
        migrations.AlterField(
            model_name='lists',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='lists',
            unique_together=set(),
        ),
    ]
