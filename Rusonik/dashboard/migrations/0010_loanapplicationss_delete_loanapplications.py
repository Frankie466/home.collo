# Generated by Django 5.0.7 on 2024-12-10 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_rename_loanapplication_loanapplications'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplicationss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(default='example@example.com', max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan_duration', models.IntegerField()),
                ('employment_status', models.CharField(choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')], default='Employed', max_length=50)),
                ('id_number', models.CharField(max_length=20)),
                ('kra_pin', models.CharField(blank=True, max_length=20, null=True)),
                ('id_scan', models.FileField(blank=True, null=True, upload_to='id_scans/')),
                ('payslip', models.FileField(blank=True, null=True, upload_to='payslips/')),
                ('guarantor1_name', models.CharField(blank=True, max_length=255, null=True)),
                ('guarantor1_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('guarantor1_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('guarantor1_employment_status', models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')], default='Employed', max_length=50, null=True)),
                ('guarantor1_id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('guarantor1_payslip', models.FileField(blank=True, null=True, upload_to='guarantor1_payslips/')),
                ('guarantor2_name', models.CharField(blank=True, max_length=255, null=True)),
                ('guarantor2_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('guarantor2_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('guarantor2_employment_status', models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')], default='Employed', max_length=50, null=True)),
                ('guarantor2_id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('guarantor2_payslip', models.FileField(blank=True, null=True, upload_to='guarantor2_payslips/')),
            ],
        ),
        migrations.DeleteModel(
            name='LoanApplications',
        ),
    ]
