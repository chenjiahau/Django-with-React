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
    period = models.CharField(
        verbose_name='期別',
        help_text='輸入九碼期別， 例：103000001期)',
        max_length=9,
        validators=[MinLengthValidator(9), MaxLengthValidator(9)]
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