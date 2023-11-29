from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.core.validators import (
    MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
)

# Create your models here.

model_action_choices = (
    ('R', 'Read'),
    ('C', 'Create'),
    ('U', 'Update'),
    ('D', 'Delete')
)

class Log(models.Model):
    model = models.CharField(
        max_length=50,
    )
    action = models.CharField(
        max_length=6,
        choices=model_action_choices
    )
    instance = models.CharField(
        max_length=50,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.model} {self.action} {self.created_at}'

    class Meta:
        ordering=['-created_at']
        verbose_name_plural='Logs'

class BigLottery(models.Model):
    period = models.IntegerField(
        verbose_name='期數',
        help_text='請輸入整數',
        validators=[MinValueValidator(1), MaxValueValidator(999)]
    )
    month = models.IntegerField(
        verbose_name='月份',
        help_text='請輸入整數',
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    day = models.IntegerField(
        verbose_name='日期',
        help_text='請輸入整數',
        validators=[MinValueValidator(1), MaxValueValidator(31)]
    )
    day_of_week = models.IntegerField(
        verbose_name='星期',
        help_text='請輸入整數',
        validators=[MinValueValidator(1), MaxValueValidator(7)]
    )
    number1 = models.IntegerField(
        verbose_name='第一個號碼',
        help_text='請輸入1~49的整數',
        validators=[MinValueValidator(1), MaxValueValidator(49)]
    )
    number2 = models.IntegerField(
        verbose_name='第二個號碼',
        help_text='請輸入1~49的整數',
        validators=[MinValueValidator(1), MaxValueValidator(49)]
    )
    number2 = models.IntegerField(
        verbose_name='第二個號碼',
        help_text='請輸入1~49的整數',
        validators=[MinValueValidator(1), MaxValueValidator(49)]
    )
    number3 = models.IntegerField(
        verbose_name='第三個號碼',
        help_text='請輸入1~49的整數',
        validators=[MinValueValidator(1), MaxValueValidator(49)]
    )
    number4 = models.IntegerField(
        verbose_name='第四個號碼',
        help_text='請輸入1~49的整數',
        validators=[MinValueValidator(1), MaxValueValidator(49)]
    )
    number5 = models.IntegerField(
        verbose_name='第五個號碼',
        help_text='請輸入1~49的整數',
        validators=[MinValueValidator(1), MaxValueValidator(49)]
    )
    number6 = models.IntegerField(
        verbose_name = '第六個號碼',
        help_text = '請輸入1~49的整數',
        validators = [MinValueValidator(1), MaxValueValidator(49)]
    )
    special_number = models.IntegerField(
        verbose_name='特別號碼',
        help_text='請輸入1~49的整數',
        validators=[MinValueValidator(1), MaxValueValidator(49)]
    )
    flag = models.BooleanField(
        verbose_name='有效樣本',
        help_text='請勾選是否納入統計',
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f'{self.period}'

    class Meta:
        ordering=['-period']
        verbose_name_plural='BigLotteries'