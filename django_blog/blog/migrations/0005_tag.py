# Generated by Django 5.1.6 on 2025-03-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_author_alter_comment_post_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('post', models.ManyToManyField(related_name='tag', to='blog.post')),
            ],
        ),
    ]
