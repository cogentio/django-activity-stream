from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0003_add_follow_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='action_type',
            field=models.PositiveSmallIntegerField(null=True, db_index=True),
        ),
    ]
