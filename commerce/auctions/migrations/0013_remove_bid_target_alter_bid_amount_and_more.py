# Generated by Django 4.2.1 on 2024-01-14 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0012_rename_comment_comments_message"),
    ]

    operations = [
        migrations.RemoveField(model_name="bid", name="target",),
        migrations.AlterField(
            model_name="bid", name="amount", field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="listing",
            name="price",
            field=models.ForeignKey(
                blank="True",
                null="True",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bid",
                to="auctions.bid",
            ),
        ),
    ]
