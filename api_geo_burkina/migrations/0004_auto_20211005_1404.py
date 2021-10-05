# Generated by Django 3.2.7 on 2021-10-05 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_geo_burkina', '0003_auto_20211004_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('chef_lieu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api_geo_burkina.departements')),
            ],
        ),
        migrations.AddField(
            model_name='provinces',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region', to='api_geo_burkina.region'),
        ),
    ]