# Generated by Django 3.0.3 on 2020-02-20 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('blog', '0012_blogpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPage',
        ),
    ]
