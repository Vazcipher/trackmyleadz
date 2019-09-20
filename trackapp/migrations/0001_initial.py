
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_title', models.CharField(max_length=20)),
                ('fk_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.Company')),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('fk_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.Company')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.UserRole')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=25)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=25)),
                ('mobile', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=10)),
                ('fk_login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.UserLogin')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_title', models.CharField(max_length=20)),
                ('fk_role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.UserRole')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_title', models.CharField(max_length=25)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('fk_reciver_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.UserLogin')),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_title', models.CharField(max_length=30)),
                ('lead_source', models.CharField(max_length=20)),
                ('lead_stage', models.CharField(max_length=15)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('created_time', models.TimeField(auto_now_add=True)),
                ('updated_date', models.DateField(blank=True, null=True)),
                ('fk_assigned_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk_assigned_user_id', to='trackapp.UserLogin')),
                ('fk_company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.Company')),
                ('fk_created_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.UserLogin')),
                ('fk_updated_user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fk_updated_user_id', to='trackapp.UserLogin')),
            ],
        ),
        migrations.CreateModel(
            name='LeadDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('product', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('fk_lead_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.Leads')),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followup_title', models.CharField(max_length=20)),
                ('followup_description', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('created_time', models.TimeField(auto_now_add=True)),
                ('fk_created_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.UserLogin')),
                ('fk_lead_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapp.Leads')),
            ],
        ),
    ]
