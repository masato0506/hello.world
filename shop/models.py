from django.db import models


class Publisher(models.Model):
    """ジャンル"""

    class Meta(object):
        db_table = 'publisher'

    name = models.CharField(verbose_name='ジャンル', max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    """著者モデル"""

    class Meta(object):
        db_table = 'author'

    name = models.CharField(verbose_name='著者名', max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """プロフィール"""

    class Meta(object):
        db_table = 'book'
    GENDER_CHOICES = (
        (0, '男性'),
        (1, '女性'),
        (2, 'どちらでもない'),
    )


    image = models.ImageField(verbose_name='画像', null=True, blank=True)
    title = models.CharField(verbose_name='名前', max_length=255)
    gender = models.IntegerField(verbose_name='性別', choices=GENDER_CHOICES, default=2)
    age = models.IntegerField(verbose_name='年齢', default=0)
    description = models.TextField(verbose_name='経歴', null=True, blank=True)
    publisher = models.ForeignKey(Publisher, verbose_name='ジャンル', on_delete=models.PROTECT)


    def __str__(self):
        return self.title
