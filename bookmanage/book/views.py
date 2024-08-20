from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo

# Create your views here.


def index(request):
    # 1. 获取参数
    # 2. 编写查询代码
    # 3. 处理查询结果
    # 4. ��染模板并返回
    # 5. 注意：返回的 HttpResponse 一定要是 str 类型
    books = BookInfo.objects.all()
    print(books)
    return HttpResponse("index")

########################增加数据########################################


def add_book(request):
    book = BookInfo(
        name='Python 基础',
        pub_date='2020-1-1',
        readcount=100
    )
    book.save()
    return HttpResponse('添加成功')


# 方式二
# objects -- 相当于一个代理 实现增删改查
#

def add_book2(request):
    BookInfo.objects.create(
        name='Python 基础1',
        pub_date='2020-1-1',
        readcount=100
    )

####################修改数据########################


# 方式1
def edit_book():
    book = BookInfo.objects.get(id=6)
    book.name = 'Python 基础2'
    book.save()

# 方式2
def edit_book2(request):
    BookInfo.objects.filter(id=6).update(name='Python 基础3')

# 错误的
# BookInfo.objects.get(id=6).update(name='666')

#################################删除记录#######################################
# 方式1

book = BookInfo.objects.get(id=6)
# 删除分2中，物理删除（这条记录的数据删除）和逻辑删除（修改标记位 例如 is_delete=False）
book.delete() # 直接删除

# 方式2
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=5).delete()

##################查询####################

# get查询单一结果，如果不存在会抛出模型类，DoesNotExist
try:
    book = BookInfo.objects.get(id=6)
except BookInfo.DoesNotExist:
    print("查询结果不存在！！")

# 查询多个结果：
books = BookInfo.objects.all()

# 查询结果的数量
count = BookInfo.objects.count()

# 实现SQL中的where功能，包括
#
## filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单一结果

# 模型类名.objects.filter(属性名__运算符=值) 获取n个结果
# 模型类名.objects.exclude(属性名__运算符=值) 获取n个结果
# 模型类名.objects.get(属性名__运算符=值)  获取1个结果（或者异常）

# 查询编号为1的图书
book1 = BookInfo.objects.get(id=1)
# 查询书名包含'湖'的图书
book2 = BookInfo.objects.filter(name__contains='湖')
# 查询书名以'部'结尾的图书
book3 = BookInfo.objects.filter(name__endswith='部')
# 查询书名为空的图书
book4 = BookInfo.objects.filter(name='')
# 查询编号为1或3或5的图书
book5 = BookInfo.objects.filter(id__in=[1, 3, 5])
# 查询编号大于3的图书
book6 = BookInfo.objects.filter(id__gt=1)
# 查询1980年发表的图书
book7 = BookInfo.objects.filter(pub_date__year=1980)
# 查询1990年1月1日后发表的图书 
book8 = BookInfo.objects.filter(pub_date__gt='1990-01-01')

