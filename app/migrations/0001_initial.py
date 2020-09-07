# Generated by Django 3.1 on 2020-09-06 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commit_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_terms', models.TextField()),
                ('license_acceptance', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_decription', models.TextField()),
                ('project_url', models.URLField()),
                ('accessibility', models.CharField(choices=[('Public', 'Public'), ('Private', 'Private'), ('Restricted', 'Restricted')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(choices=[('Python', 'Python'), ('Java', 'Java'), ('C/C++', 'C/C++'), ('Node', 'Nodejs'), ('Typescript', 'Typescript'), ('Django', 'Django'), ('React', 'React'), ('Angular', 'Angular'), ('Flask', 'Flask'), ('Vue', 'Vue'), ('Javascript', 'Javascript'), ('Web', 'HTML/CSS')], max_length=12)),
                ('skill_experience', models.CharField(choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('E', 'Expert')], max_length=12)),
                ('years_of_experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('payment', models.CharField(blank=True, choices=[('VISA', ' Visa Card'), ('PAYPAL', 'Paypal'), ('MASTER CARD', 'Master Card'), ('MPESA', 'MPESA')], max_length=15)),
                ('git_auth_token', models.CharField(blank=True, max_length=512, null=True)),
                ('price_per_hour', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('commits', models.ManyToManyField(to='app.Commit')),
                ('licence_agreement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.license')),
                ('project', models.ManyToManyField(to='app.Project')),
                ('skills_list', models.ManyToManyField(to='app.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FeaturePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('time_line', models.IntegerField()),
                ('commit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commit')),
                ('licence_agreement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.license')),
                ('proposed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='commit',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
    ]