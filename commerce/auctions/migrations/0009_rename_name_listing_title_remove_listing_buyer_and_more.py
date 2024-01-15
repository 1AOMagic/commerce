# Generated by Django 4.2.1 on 2024-01-12 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0008_category_remove_listing_bidders_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listing", old_name="name", new_name="title",
        ),
        migrations.RemoveField(model_name="listing", name="buyer",),
        migrations.RemoveField(model_name="listing", name="creator",),
        migrations.RemoveField(model_name="listing", name="current_bid",),
        migrations.RemoveField(model_name="listing", name="date_created",),
        migrations.AddField(
            model_name="listing",
            name="imageUrl",
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name="listing",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="bid",
            name="bidder",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bidder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="listing", name="price", field=models.FloatField(),
        ),
    ]
