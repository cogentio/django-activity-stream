from django.db import migrations, models
from django.conf import settings
from django.utils.timezone import now


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0004_add_action_type'),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=255)),
                ("timestamp", models.DateTimeField(default=now)),
                (
                    "action",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=models.deletion.CASCADE,
                        related_name="comments",
                        to="actstream.Action",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=models.deletion.CASCADE,
                        related_name="action_comments",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
