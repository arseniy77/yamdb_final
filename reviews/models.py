from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

from .validators import validate_year  # isort:skip
from users.models import User  # isort:skip


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
            MinValueValidator(0),
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


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        max_length=10000,
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=True,
        null=True
    )
    score = models.IntegerField(
        verbose_name='Оценка',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )

    def __str__(self):
        return f'{self.text:.15}...'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
        unique_together = ('author', 'title')

        constraints = [
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='unique_author_title'
            )
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        blank=True,
        null=True,
        verbose_name='Отзыв'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='comments',
        verbose_name='Автор')
    text = models.TextField(
        max_length=1000,
        verbose_name='Текст комментария'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ('pub_date',)
