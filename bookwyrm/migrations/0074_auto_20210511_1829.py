# Generated by Django 3.2 on 2021-05-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookwyrm", "0073_sitesettings_footer_item"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="connector",
            name="max_query_count",
        ),
        migrations.RemoveField(
            model_name="connector",
            name="politeness_delay",
        ),
        migrations.RemoveField(
            model_name="connector",
            name="query_count",
        ),
        migrations.RemoveField(
            model_name="connector",
            name="query_count_expiry",
        ),
        migrations.AddField(
            model_name="connector",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="connector",
            name="deactivation_reason",
            field=models.CharField(
                blank=True,
                choices=[
                    ("self_deletion", "Self Deletion"),
                    ("moderator_deletion", "Moderator Deletion"),
                    ("domain_block", "Domain Block"),
                ],
                max_length=255,
                null=True,
            ),
        ),
    ]
