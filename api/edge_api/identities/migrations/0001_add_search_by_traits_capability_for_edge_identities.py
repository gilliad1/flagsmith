# Generated by Django 3.2.25 on 2024-08-15 10:46

import django.contrib.postgres.indexes
from django.db import migrations, models
from django.contrib.postgres.operations import BtreeGinExtension
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environments', '0035_add_search_by_traits_capability_for_edge_identities'),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.CreateModel(
            name='EdgeIdentityMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('edge_identity_uuid', models.UUIDField(db_index=True)),
                ('identifier', models.CharField(max_length=2000)),
                ('searchable_traits', models.TextField()),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='environments.environment')),
            ],
        ),
        migrations.AddIndex(
            model_name='edgeidentitymeta',
            index=django.contrib.postgres.indexes.GinIndex(fields=['searchable_traits'], name='edge_api_id_searcha_816c05_gin'),
        ),
    ]
