# login

## 说明

**login命令** 用于给出登录界面，可用于重新登录或者切换用户身份，也可通过它的功能随时更换登入身份。在Slackware发行版中 ，可在命令后面
附加欲登入的用户名称，它会直接询问密码，等待用户输入。当`/etc/nologin`文件存在时，系统只root帐号登入系统，其他用户一律不准登入

## 选项

```markdown
login [ -p ] [ -h 主机 ] [ -H ] [ -f 用户名 | 用户名 ]

-p  告诉login指令不销毁环境变量
-h   指定远程服务器的主机名
```
