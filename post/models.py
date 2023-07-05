from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)



    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='posts',
                                 related_query_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.category:
            return f'{self.category.title} > {self.title} > {self.body}'
        else:
            return self.title


# eidable - если False то запись нельзя поменять

# defaust - значение по умолчанию для поля ,добавляет значение если данные не переданы

# unique- если True то будет вызываться ошибка при попытке создать запись которая уже имеется в таблице

# primary_key - если True то это поле станет первичным ключем в таблице
# primary_key - null = False unique = True
# jango.core.validators import Min

# class Product(models.Model):
#     name = models.CharField(max_length= 100)
#     price = models.DecimalField(max_length=8, decimal_places=2, validators= [MinValueValidator(0), MaxValueValidator(200)])
#
#     code = models.CharField(max_length= 10, validators=[
#         RegexValidator(regex = r'[A-Z]{3}\d{3}$',
#         message = 'Code must be in format AAA-666,'
#                        )
#
#     ])


# class Pastport(models.Model):
#     info=models.CharField(max_length=255)
#
# class Person(models.Model):
#     passport = model.OneToOneField(Passprt , on_delete = models.CASCADE)
#
# class Tag(models.Model):
#     title = models.CharField(max_length=255)
#
# class Post(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

# on_delite =models.CASCADE - каскадное удаление (если удаляется главный обьекто,то
# удаляются и все зависящие от него обьектвы)

# on_delete = models.PROTECT - вызывает ошибку при попытке удаления главного удаления

# on_delete = models.SET_NULL - не удаляет зависящие обьекты а проставляет null если null = True

# models.SET_DEFAULT - ставит default ,если был определен defaulst

# models.DO_NOTHING - ничегот не делает (может возникнуть ошибка если не пропмсать blank = True, null = True)

