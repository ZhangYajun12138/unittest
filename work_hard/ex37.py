# coding:utf-8
# 符号

# keywords
'''
and 逻辑与
del 删除list中的元素
from 从模块中包含函数或类
not 逻辑非
while 一般用于无限循环
as 取别名，一般用于打开文件时with open("a.txt","w") as f:
elif 循环的第二个判断
global 在函数或者类中更改全局变量的值，若不加，则j
or 逻辑或
with 一般用于打开文件时with open("a.txt","w") as f:
assert 单元测试,断言
else 条件判断中使用
pass 跳过

yield 返回生成器
def fab(max):
    a,b = 0,1
    while a < max:
        yield a
        a,b = b,a+b
print("斐波那契数列')
for i in fab(20):
    print(i,end = "")

break 跳出循环,循环结束，注意：如果从for或者while循环中break后，else语句不执行

except 异常处理，捕获异常
import 引入头文件
print 打印
class 创建类
exec 执行存储在字符串或者文件中的铺python语句

in 是否包含在内
a = "a"
b = "abcde"
a in b 表示a是否包含在b内

raise 抛出异常
continue 跳过此次判断，继续下一次循环
finally 异常处理其他情况
is 通过id判断两个对象是否相等
rerun 返回值
def 创建函数
for 循环
lambda 匿名函数
try 可能出现异常的函数体
'''

# 数据类型
'''
True bool类型真
False bool类型假
None 空值
string 字符串
number
float 浮点型
list 列表
tuple 元组，不可更改，只读
dictionary 字典
'''

# 字符串转义序列
'''
\\ 斜杠
\' 单引号
\" 双引号
\a 系统响铃
\b 退格符
\f 换页符
\n 换行符
\r 回车符
\t 横向制表符
\v 纵向制表符
'''

# 字符串格式化
'''
%d 整数类型
%i 
%o 无符号八进制数
%u 无符号整型
%x 无符号十六进制数
%X 无符号十六进制数，大写
%e 科学计数法，浮点数
%E 科学计数法，浮点数
%f 浮点数，可指定小数点后的精度
%F
%g 根据值的大小决定使用%f或者%e
%G 根据值的大小决定使用%f或者%e
%c 字符，ASCII码
%r 
%s 字符串
%%

'''

# 操作符号
'''
+
-
*
** 指数
/
//
%
<
>
<=
>=
==
!=
<>
()
[]
{}
@
,
:
. 
=
;
+=
-=
*=
/=
//=
%=
**=
'''
