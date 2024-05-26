# Generated by Django 5.0.3 on 2024-05-26 09:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CountryModel",
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
                ("Name", models.CharField(max_length=120)),
            ],
            options={
                "db_table": "country",
            },
        ),
        migrations.CreateModel(
            name="CustomerMode",
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
                (
                    "Surname",
                    models.TextField(
                        choices=[("mr", "Mr"), ("miss", "Miss"), ("mrs", "Mrs")]
                    ),
                ),
                ("Firstname", models.CharField(max_length=200)),
                (
                    "Gender",
                    models.TextField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ]
                    ),
                ),
                ("Card_number", models.CharField(max_length=120)),
                (
                    "Nationality",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assign_app.countrymodel",
                    ),
                ),
            ],
            options={
                "db_table": "customer",
            },
        ),
        migrations.CreateModel(
            name="CustomerDocumentModel",
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
                ("atteched_file", models.FileField(upload_to="upload/data/")),
                ("Extracted_json", models.JSONField(default=dict)),
                ("Created_at", models.TimeField()),
                (
                    "Customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assign_app.customermode",
                    ),
                ),
            ],
            options={
                "db_table": "customerdocument",
            },
        ),
        migrations.CreateModel(
            name="DocumentSetModel",
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
                ("Name_of_document", models.CharField(max_length=500)),
                (
                    "Has_backside",
                    models.CharField(
                        blank=True,
                        choices=[("yes", "Yes"), ("no", "No")],
                        max_length=5,
                        null=True,
                    ),
                ),
                ("OcrLables", models.JSONField(blank=True, default=dict, null=True)),
                (
                    "Country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assign_app.countrymodel",
                    ),
                ),
            ],
            options={
                "db_table": "documentset",
            },
        ),
        migrations.CreateModel(
            name="UserModel",
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
                ("User_name", models.CharField(max_length=120)),
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=55)),
                (
                    "country_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assign_app.countrymodel",
                    ),
                ),
            ],
            options={
                "db_table": "user",
            },
        ),
        migrations.AddField(
            model_name="customermode",
            name="CreateBy",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="assign_app.usermodel"
            ),
        ),
    ]