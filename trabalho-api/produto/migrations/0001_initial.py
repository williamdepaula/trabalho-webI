# Generated by Django 3.0.7 on 2020-06-08 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('quantidade', models.IntegerField()),
                ('descricao', models.TextField()),
                ('custo', models.DecimalField(decimal_places=2, max_digits=6)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=6)),
                ('url_img', models.URLField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.Categoria')),
            ],
            options={
                'db_table': 'produto',
            },
        ),
    ]
