# **fc**

## 说明

**fc命令** 自动掉用vi编辑器修改已有历史命令，当保存时立即执行修改后的命令，也可以用来显示历史命令。fc命令编辑历史命令时，
会自动调用vi编辑器。fc保存文件后，会自动执行所编辑过的命令

## 选项

```markdown
用法:fc [-e 编辑器名] [-lnr] [起始] [终结] 或 fc -s [模式=替换串] [命令]

-l：
-n：显示历史命令时，不显示编号
-r：反序显示历史命令

```

## 实例

```bash
fc -l -10     #显示10条历史命令

```


