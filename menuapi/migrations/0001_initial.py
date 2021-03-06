# Generated by Django 4.0.1 on 2022-05-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesOfMeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('dessert', 'dessert'), ('main_course', 'main_course'), ('starters', 'starters'), ('salad', 'salad'), ('mignardise', 'mignardise')], default='starters', max_length=150)),
            ],
        ),
    ]
