# Generated by Django 3.0.3 on 2020-03-11 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('money', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TopupLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('topup_date', models.DateField(blank=True, null=True)),
                ('topup_by', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cashier.Member')),
            ],
        ),
        migrations.CreateModel(
            name='SeatBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateField(blank=True, null=True)),
                ('time_out', models.DateField(blank=True, null=True)),
                ('total_price', models.FloatField(max_length=10)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('create_by', models.CharField(max_length=50)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cashier.Member')),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cashier.Zone')),
            ],
        ),
    ]
