# **ssh-copy-id**

## 说明

**ssh-copy-id命令** 可以把本地主机的公钥复制到远程主机的authorized_keys文件上，ssh-copy-id命令也会给远程主机的
用户主目录（home）和`~/.ssh`, 和`~/.ssh/authorized_keys`设置合适的权限

## 选项

```markdown
ssh-copy-id [-i [identity_file]] [user@]machine

-i：指定公钥文件
```

## 实例

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@server # 把本地的ssh公钥文件安装到远程主机对应的账户下
```


