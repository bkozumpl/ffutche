# Generated by Django 3.1 on 2020-04-29 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('paradigm', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarshipID', models.CharField(max_length=12)),
                ('denomination', models.TextField(max_length=40)),
                ('referred_studies', models.CharField(max_length=25)),
                ('amount', models.IntegerField(null=True)),
                ('academic_year', models.DateField(max_length=10)),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolID', models.CharField(max_length=45)),
                ('school_name', models.TextField(max_length=45)),
                ('school_address', models.CharField(max_length=45)),
                ('type_of_school', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('country_province', models.CharField(max_length=45)),
                ('em_contact', models.CharField(max_length=45)),
                ('em_contact_num1', models.IntegerField(null=True)),
                ('em_contact_num2', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Hollow_Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hollow_year', models.CharField(max_length=45)),
                ('activities', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='username', max_length=45)),
                ('password1', models.CharField(default='password1', max_length=45)),
                ('password2', models.CharField(default='password2', max_length=45)),
                ('firstname', models.CharField(default='firstname', max_length=45)),
                ('middlename', models.CharField(default='middlename', max_length=45)),
                ('lastname', models.CharField(default='lastname', max_length=45)),
                ('gender', models.CharField(default='gender', max_length=45)),
                ('type_of_user', models.CharField(default='user type', max_length=45)),
                ('phone1', models.IntegerField(null=True)),
                ('phone2', models.IntegerField(null=True)),
                ('address1', models.CharField(default='address1', max_length=45)),
                ('address2', models.CharField(default='address2', max_length=45)),
                ('dob_day', models.CharField(default='DD', max_length=45)),
                ('dob_month', models.CharField(default='MM', max_length=45)),
                ('dob_year', models.CharField(default='0000', max_length=45)),
                ('cityofbirth', models.CharField(default='city', max_length=45)),
                ('countryofbirth', models.CharField(default='country', max_length=45)),
                ('marital_status', models.CharField(default='relationship status', max_length=45)),
                ('number_of_children', models.CharField(default='children?', max_length=45)),
                ('occupation', models.CharField(default='job', max_length=45)),
                ('employer_name', models.CharField(default='employer', max_length=45)),
                ('employer_address', models.CharField(default='employer address', max_length=45)),
                ('email', models.EmailField(default='email', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tuition_Fees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_level', models.CharField(max_length=15)),
                ('academic_year', models.IntegerField(null=True)),
                ('tuition', models.IntegerField(null=True)),
                ('clothing', models.CharField(max_length=45)),
                ('furniture', models.CharField(max_length=45)),
                ('books', models.CharField(max_length=45)),
                ('misc', models.CharField(max_length=45)),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.School')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awarded_on', models.CharField(max_length=45)),
                ('delivery_method', models.CharField(max_length=45)),
                ('award_justification', models.CharField(max_length=45)),
                ('awarded_amount', models.CharField(max_length=45)),
                ('scholarshipID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Scholarship')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_attended', models.CharField(max_length=45)),
                ('Class', models.CharField(max_length=45)),
                ('grade', models.IntegerField(null=True)),
                ('degree', models.CharField(max_length=45)),
                ('rank', models.CharField(max_length=45)),
                ('dismissed', models.CharField(max_length=45)),
                ('dismissed_reason', models.CharField(max_length=45)),
                ('schoolID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.School')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship_Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
                ('academic_year', models.IntegerField(null=True)),
                ('scholarshipID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Scholarship')),
            ],
        ),
    ]
