# Generated by Django 4.0.1 on 2022-06-11 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('morphologyApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bithday', models.DateTimeField(verbose_name='Дата рождения')),
                ('body_length', models.IntegerField(max_length=3, verbose_name='Длина тела(см)')),
                ('body_weight', models.IntegerField(max_length=3, verbose_name='Масса тела(кг)')),
                ('acromial_diameter', models.IntegerField(max_length=3, verbose_name='Акромиальный диаметр(мм)')),
                ('mid_chest_transverse_diameter', models.IntegerField(max_length=3, verbose_name='Среднегрудинный поперечный диаметр(мм)')),
                ('hip_width', models.IntegerField(max_length=3, verbose_name='Тазо-бедреный диаметр(ширина таза 1)(мм)')),
                ('interbody_diameter', models.IntegerField(max_length=3, verbose_name='Межвертельный диаметр(ширина таза 3)(мм)')),
                ('width_two_closed_knees', models.IntegerField(max_length=3, verbose_name='Ширина двух сомкнутых колен(мм)')),
                ('shin_circumference_minimal', models.IntegerField(max_length=3, verbose_name='Обхват голени минимальный(мм)')),
                ('forearm_circumference_minimal', models.IntegerField(max_length=3, verbose_name='Обхват предплечья минимальный(мм)')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
