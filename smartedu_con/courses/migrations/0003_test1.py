# Generated by Django 4.1.5 on 2023-02-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_alter_course_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Test1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.ImageField(
                        default="courses/defualt_course_image.jpg",
                        upload_to="courses/%Y/%m/%d/",
                    ),
                ),
                ("available", models.BooleanField(default=False)),
            ],
        ),
    ]