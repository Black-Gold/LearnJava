# znew

## 说明

**znew命令** 用于将使用compress命令压缩的“.Z”压缩包重新转化为使用gzip命令压缩的“.gz”压缩包

## 选项

```markdown
-f     强制执行转换操作，即是目标“.gz”已经存在
-t     删除原文件前测试新文件
-v     显示文件名和每个文件的压缩比
-9     Use the slowest compression method (optimal compression)
-P     使用管道完成转换操作，以降低磁盘空间使用
-K     当“.Z”文件比“.gz”文件小时，保留“.Z”文件; implies -t

```
