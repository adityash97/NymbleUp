# Generated by Django 4.0.4 on 2022-04-23 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('responseType', models.SmallIntegerField(blank=True, choices=[(1, 'yes/no'), (2, 'text'), (3, 'numberic')], default=2, max_length=10)),
                ('mandatory', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerType1', models.CharField(blank=True, choices=[(1, 'YES'), (2, 'NO')], max_length=4)),
                ('answerType2', models.TextField(max_length=500)),
                ('answerType3', models.IntegerField()),
                ('questionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dynamicform.question')),
            ],
        ),
    ]