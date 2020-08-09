# Generated by Django 3.0.6 on 2020-08-02 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_appi', '0008_auto_20200801_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, default='billy-huynh-W8KTS-mhFUE-unsplash.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_appi.Topic'),
        ),
    ]