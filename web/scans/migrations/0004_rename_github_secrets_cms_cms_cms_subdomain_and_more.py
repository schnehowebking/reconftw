# Generated by Django 4.0.5 on 2022-11-28 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_scan_mode'),
        ('scans', '0003_remove_websuncommonports_webs_uncommon_ports_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cms',
            old_name='github_secrets',
            new_name='cms',
        ),
        migrations.AddField(
            model_name='cms',
            name='subdomain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='webfullinfo',
            name='port',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='webfullinfo',
            name='technologies',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='SubdomainsConsolidated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdomain', models.CharField(blank=True, default='N/A', max_length=100)),
                ('ips', models.CharField(blank=True, default='N/A', max_length=200)),
                ('port', models.CharField(blank=True, default='N/A', max_length=200)),
                ('technology', models.CharField(blank=True, default='N/A', max_length=200)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]