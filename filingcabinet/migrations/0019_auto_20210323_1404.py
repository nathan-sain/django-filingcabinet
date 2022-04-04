# Generated by Django 3.1.6 on 2021-03-23 13:04

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILINGCABINET_DOCUMENT_MODEL),
        ("filingcabinet", "0018_auto_20200622_1302"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="listed",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="documentcollection",
            name="listed",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="documentcollection",
            name="uid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name="page",
            name="document",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pages",
                to=settings.FILINGCABINET_DOCUMENT_MODEL,
            ),
        ),
    ]
