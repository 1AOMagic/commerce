# Generated by Django 4.2.1 on 2023-05-25 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0004_alter_listing_high_bidder"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listing", old_name="high_bidder", new_name="bidders",
        ),
    ]