# Generated by Django 3.2.6 on 2021-08-29 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Teacher_Name', models.CharField(max_length=100)),
                ('Teacher_Address', models.TextField()),
                ('Teacher_Joining_Date', models.DateTimeField(auto_now_add=True)),
                ('School_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Student_Address', models.TextField(blank=True, null=True)),
                ('Student_Roll_No', models.IntegerField(blank=True, null=True)),
                ('Student_File', models.FileField(blank=True, null=True, upload_to='pdf')),
                ('School_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.school')),
                ('Teacher_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='demo.teacher')),
            ],
        ),
    ]