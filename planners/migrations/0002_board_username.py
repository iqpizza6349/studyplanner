# Generated by Django 3.2.7 on 2021-10-26 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('planners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.boardmember'),
        ),
    ]