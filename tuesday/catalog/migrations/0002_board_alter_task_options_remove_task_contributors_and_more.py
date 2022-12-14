# Generated by Django 4.1 on 2022-08-21 13:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a board name', max_length=200)),
                ('contributors', models.ManyToManyField(help_text='List of contributors', to='catalog.contributor')),
            ],
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['deadline']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='contributors',
        ),
        migrations.RemoveField(
            model_name='task',
            name='name',
        ),
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('w', 'in work'), ('fn', 'finished'), ('fr', 'frozen')], default='w', help_text='task status', max_length=2),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular task across whole board', primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='TaskInstance',
        ),
        migrations.AddField(
            model_name='task',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.board'),
        ),
    ]
