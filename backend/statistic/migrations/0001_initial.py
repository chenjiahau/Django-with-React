# Generated by Django 4.2.7 on 2023-11-26 08:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BigLottery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(help_text='輸入九碼期別， 例：103000001期)', max_length=9, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9)], verbose_name='期別')),
                ('number1', models.IntegerField(help_text='請輸入1~49的整數', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='第一個號碼')),
                ('number2', models.IntegerField(help_text='請輸入1~49的整數', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='第二個號碼')),
                ('number3', models.IntegerField(help_text='請輸入1~49的整數', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='第三個號碼')),
                ('number4', models.IntegerField(help_text='請輸入1~49的整數', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='第四個號碼')),
                ('number5', models.IntegerField(help_text='請輸入1~49的整數', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='第五個號碼')),
                ('number6', models.IntegerField(help_text='請輸入1~49的整數', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9)], verbose_name='第六個號碼')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
