# Generated by Django 3.2.7 on 2021-10-04 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_geo_burkina', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provinces',
            name='Departements',
        ),
        migrations.AddField(
            model_name='departements',
            name='departements',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='departement', to='api_geo_burkina.departements'),
        ),
        migrations.AlterField(
            model_name='provinces',
            name='chef_lieu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='chef_lieu', to='api_geo_burkina.departements'),
        ),
    ]
