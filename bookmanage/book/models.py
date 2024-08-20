from django.db import models

# Create your models here.
"""
    1、模型类 需要继承自 models.Model
    2、定义属性
        属性名=models.类型（选项）
        2.1属性名 对应 字段名
            不要使用python关键字、和mysql关键字
            不要使用连续的下划线
        2.2类型 mysql的类型
        2.3选项 是否有默认值，是否唯一，是否为null
            CharField 必须设置 max_length
    3.改变表的名称
        默认表的名称是：子应用名_类名 都是小写
        修改表的名称
        
"""


class BookInfo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # 修改表的名字（固定写法）
    class Meta:
        db_table = "bookinfo"
        verbose_name = "图书信息"  # 后台管理中显示的表名(admin站点使用)


class PeopleInfo(models.Model):

    # 定义一个有序字典
    GENDER_CHOICES = (
        (0, 'Male'),
        (1, 'Female'),
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0)
    description = models.CharField(max_length=100, null=True)
    is_deleted = models.BooleanField(default=False)
    # 删除主表的三种情况
        # 1. 主表记录被删除设置保护，抛出异常
        # 2. 主表的外键被设置为 null
        # 3.主表的外键被设置为 CASCADE(级联)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "peopleinfo"
