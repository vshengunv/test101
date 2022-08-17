"""
pyinstaller -F -p F:\study Auto_pay.py --noconsole


-D:打包成多个文件
-p：指定python安装包路径
-i：指定图标，到网上下载一个图标,保存为logi.ico文件，
mian.py：要打包的文件
注意main.py与logo.ico必须放在同一个目录下
-D与-F一一对应，-F是打包成一个单独的文件。
最后一排加上--noconsole，就是无窗口运行。
--key=keys :使用keys进行加密打包，例如 pyinstaller --key-keys=1234 -F xx.py
"""





if __name__ == '__main__':

    # TestMylog.print_log(webdriver.Chrome())


