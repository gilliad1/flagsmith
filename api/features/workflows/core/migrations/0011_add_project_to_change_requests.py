# Generated by Django 4.2.15 on 2024-09-17 15:34

import django.db.models.deletion
from django.db import migrations, models


def set_project_for_existing_environments(apps, schema_model):
    ChangeRequest = apps.get_model("workflows_core", "ChangeRequest")

    for change_request in ChangeRequest.objects.filter(
        environment_id__isnull=False
    ).select_related("environment"):
        change_request.project = change_request.environment.project
        change_request.save()


class Migration(migrations.Migration):

    dependencies = [
        ("environments", "0035_add_use_identity_overrides_in_local_eval"),
        ("projects", "0025_add_change_request_project_permissions"),
        ("workflows_core", "0010_add_ignore_conflicts_option"),
    ]

    operations = [
        migrations.AddField(
            model_name="changerequest",
            name="project",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="change_requests",
                to="projects.project",
            ),
        ),
        migrations.AddField(
            model_name="historicalchangerequest",
            name="project",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="projects.project",
            ),
        ),
        migrations.AlterField(
            model_name="changerequest",
            name="environment",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="change_requests",
                to="environments.environment",
            ),
        ),
        migrations.RunPython(
            set_project_for_existing_environments,
            reverse_code=migrations.RunPython.noop,
        ),
    ]
