# **tail**

## 说明

**tail命令** 用于输入文件中的尾部内容。tail命令默认在屏幕上显示指定文件的末尾10行。如果给定的文件不止一个，则在显示的每个文件前面加一个文件名标题。如果没有指定文件或者文件名为“-”，则读取标准输入。

注意：如果表示bytes或lines的K值之前有一个”+”号，则从文件开头的第K项开始显示，K值后缀：b表示512，b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,GB 1000*1000*1000, G 1024*1024*1024, and so on for T, P, E, Z, Y

## 选项

```info
--c, --bytes=K ：输出文件尾部的第K（K为整数）个字节内容
-f, --follow[={name|descriptor}] ：显示文件最新追加的内容。“name”表示以文件名的方式监视文件的变化。“-f”与“-fdescriptor”等效
-F：与选项“-follow=name --retry"连用时功能相同
-n, --lines=K ：输出文件的尾部N（N位数字）行内容
--pid=<进程号> ：与“-f”选项连用，当指定的进程号的进程终止后，自动退出tail命令
-q或——quiet或——silent：当有多个文件参数时，不输出各个文件名
-s<秒数>或——sleep-interal=<秒数>：与“-f”选项连用，指定监视文件变化时间隔的秒数
```

## 实例

```sh
tail file           # 显示文件file的最后10行
tail -n +20 file    # 显示文件file的内容，从第20行至文件末尾
tail -c 10 file     # 显示文件file的最后10个字符）
```