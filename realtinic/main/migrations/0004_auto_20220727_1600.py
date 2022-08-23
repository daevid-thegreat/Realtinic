# Generated by Django 3.2.13 on 2022-07-27 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220727_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, null=True)),
                ('rating', models.CharField(choices=[('Bad', 'Bad'), ('Fair', 'Fair'), ('Average', 'Average'), ('Good', 'Good'), ('Excellent', 'Excellent')], default='Fair', max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('property', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.property')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]