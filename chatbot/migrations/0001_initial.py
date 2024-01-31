# Generated by Django 4.2.9 on 2024-01-31 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_state', models.CharField(default='greeting', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_session', to='chatbot.step')),
            ],
        ),
    ]