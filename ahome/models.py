from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Категория"  # произносимое имя в единственном числе
        verbose_name_plural = "Категории"  # произносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.name


class Verse(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    short_description = models.TextField(max_length=256, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)

    class Meta:
        # django само определяет единственное и множественное число, но можно переопределить
        verbose_name = "Verse"  # произносимое имя в единственном числе
        verbose_name_plural = "Verses"  # произносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.name


class Book(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    short_description = models.TextField(max_length=256, blank=True, null=True, default=None)
    static = models.PositiveIntegerField('Просмотры', default=0)  # количество просмотров

    class Meta:
        verbose_name = "Рукопись"  # произносимое имя в единственном числе
        verbose_name_plural = "Рукописи"  # произносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s" % self.name


class Chapter(models.Model):
    name = models.CharField(max_length=64)
    book = models.ForeignKey(Book, blank=True, null=True, default=None, on_delete=models.SET_NULL)
    numer = models.IntegerField(blank=True, null=True)
    short_description = models.TextField(max_length=256, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Глава"  # произносимое имя в единственном числе
        verbose_name_plural = "Главы"  # произносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s %s %s" % (self.name, self.numer , self.book.name)


class Diary(models.Model):
    short_description = models.TextField(max_length=256, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now=True)
    static = models.PositiveIntegerField('Просмотры', default=0)     # количество просмотров

    class Meta:
        verbose_name = "Заметка"  # произносимое имя в единственном числе
        verbose_name_plural = "Заметки"  # произносимое имя во множественном числе

    def __str__(self):  # настройка презинтации модели вадминке
        return "%s %s %s" % (self.created.day, self.short_description, self.update.day)


