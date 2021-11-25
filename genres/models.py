from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

from .validators import validate_year


class Categories(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=200)
    slug = models.SlugField(verbose_name='Слаг категории', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Genres(models.Model):
    name = models.CharField(verbose_name='Название жанра', max_length=200)
    slug = models.SlugField(verbose_name='Название жанра', unique=True)

    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанр'

    def __str__(self):
        return f'{self.name}'


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название произведения',
        max_length=200
    )
    year = models.IntegerField(
        verbose_name='Год выхода',
        validators=[validate_year],
        default=None
    )
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг',
        null=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    description = models.CharField(
        verbose_name='Описание произведения',
        max_length=1000)
    genre = models.ManyToManyField(Genres, through='GenresTitles')
    category = models.ForeignKey(
        Categories,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )

    class Meta:
        verbose_name = 'Произведения'
        verbose_name_plural = 'Произведение'


class GenresTitles(models.Model):
    genre = models.ForeignKey(Genres, on_delete=CASCADE)
    title = models.ForeignKey(Title, on_delete=CASCADE)
