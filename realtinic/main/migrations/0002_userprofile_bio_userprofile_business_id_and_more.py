# Generated by Django 4.0.3 on 2022-04-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=700, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='business_id',
            field=models.FileField(null=True, upload_to='business ids'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gov_id',
            field=models.FileField(null=True, upload_to='government ids'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='in_business_since',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='instagram',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profilepic',
            field=models.ImageField(null=True, upload_to='agents profile image'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tel',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='utility_bills',
            field=models.FileField(null=True, upload_to='utility bills'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='whatsapp',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
    ]