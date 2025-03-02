# Generated by Django 5.0.7 on 2024-12-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_loan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoanApplicationForms',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='application_date',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='loan_purpose',
        ),
        migrations.RemoveField(
            model_name='loanapplication',
            name='user',
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='employment_status',
            field=models.CharField(choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')], default='Employed', max_length=50),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='full_name',
            field=models.CharField(default='pius', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor1_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor1_employment_status',
            field=models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')], default='Employed', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor1_id_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor1_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor1_payslip',
            field=models.FileField(blank=True, null=True, upload_to='guarantor1_payslips/'),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor1_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor2_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor2_employment_status',
            field=models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Self-Employed', 'Self-Employed'), ('Unemployed', 'Unemployed')], default='Employed', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor2_id_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor2_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor2_payslip',
            field=models.FileField(blank=True, null=True, upload_to='guarantor2_payslips/'),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='guarantor2_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='id_number',
            field=models.CharField(default=40090973, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='id_scan',
            field=models.FileField(blank=True, null=True, upload_to='id_scans/'),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='kra_pin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='payslip',
            field=models.FileField(blank=True, null=True, upload_to='payslips/'),
        ),
        migrations.AddField(
            model_name='loanapplication',
            name='phone',
            field=models.CharField(default=254708229705, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_duration',
            field=models.IntegerField(),
        ),
    ]
