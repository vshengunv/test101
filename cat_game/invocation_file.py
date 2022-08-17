# 跨目录调用文件
import sys
from  os.path import dirname,abspath

# __file__用于获取文件所在的路径，调用os下的abspath（file）可以得到文件的绝对路径：
project_path = dirname(dirname(abspath(__file__)))
# dirname( )函数用于获取上级目录，所以当两个dirname( )嵌套时，得到的目录为该文件的路径
# 将该路径与“\\module1”目录拼接，可得到该文件所属的目录，添加到path即可
sys.path.append(project_path + "\\module")  #module 表示文件名


def add(a=1,b=2):
    if a is None:
        raise NameError("'a' cannot be empty" )
    else:
        c1 = a + b
        return c1;




'''
“if __name__ == '__main__':”表示当模块被直接运行时，下面的代码块将被运行；当
模块被其他程序文件调用时，下面的代码块不被运行。    所以一般将测试代码放在此函数下面
'''
if __name__ == '__main__':
    print(add(1,1));
    print(add(None, 2))                     #当add函数中 a 为 None 时打印NameError



