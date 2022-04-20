# Generated by Django 4.0.3 on 2022-04-15 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_property_list_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='air_con',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='attic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='basement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='bball',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='bbq_area',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='chandelier',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='closets',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='dining_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='dishwater',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='dryer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='equiped_kitchen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='fence',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='fireplace',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='fitness_arena',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='freezer_fridge',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='garbage_disposer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='garden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='gate',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='indoor_pool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='laundry_room',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='library',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='office',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='oven',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='parking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='patio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='pool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='porch',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='security',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='smoke_detector',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='solar_power',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='spa',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='sport_arena',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='sprinkler',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='tennis_court',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='washing_machine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='wifi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='workshop',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.FileField(upload_to='property_images'),
        ),
        migrations.AlterField(
            model_name='property',
            name='video_link',
            field=models.URLField(blank=True, max_length=350, null=True),
        ),
    ]
