# 5-1
# s = 'Hello world\n文本文件的读取方法\n文本文件的写入方法\n'
#
# with open('sample.txt', 'w') as fp:    #默认使用cp936编码
#     fp.write(s)
#
# with open('sample.txt') as fp:         #默认使用cp936编码
#     print(fp.read())

# 5-2 将一个CP936编码格式的文本文件中的内容全部复制到另一个使用UTF8编码的文本文件中
# def fileCopy(src, dst, srcEncoding, dstEncoding):
#     with open(src, 'r', encoding=srcEncoding) as srcfp:
#         with open(dst, 'w', encoding=dstEncoding) as dstfp:
#             dstfp.write(srcfp.read())
#
# fileCopy('sample.txt', 'sample_new.txt', 'cp936', 'utf8')


# 示例5-3   遍历并输出文本文件的所有行内容。
# with open('sample.txt') as fp:      #假设文件采用CP936编码
#     for line in fp:                 #文件对象可以直接迭代
#         print(line)


# 示例5-4   假设已有一个文本文件sample.txt，将其中第13、14两个字符修改为测试。
# with open('sample.txt', 'r+') as fp:
#     fp.seek(13)
#     fp.write('测试')

# 示例5-5  假设文件data.txt中有若干整数，所有整数之间使用英文逗号分隔，编写程序读取所有整数，将其按升序排序后再写入文本文件data_asc.txt中。











