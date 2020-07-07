import os

# 请填入需要加密的模型 文件名
class Encryption:
    def __init__(self,filepath):
        self.filename=filepath
    
    def encryption(self):
        filename = self.filename
        tmpfile = 'tempfileforDeepFace.tmp'
        dataSize = 4096 # 请输入一个二次幂形式的参数
        isCry = False   #判断是否加密

        newfile = open(tmpfile,'wb+')
        orginfile = open(filename,'rb+')

        # 验证是否重复加密/解密
        orginfile.seek(0)
        isDone = orginfile.read(4)
        if isDone == str.encode("Liya"):
            newfile.close()
            orginfile.close()
            os.remove(tmpfile)
            exit("已完成加密，无需再加密")


        orginfile.seek(0)
        newfile.seek(0)
        newfile.write(b"Liya")

        while True:
            block = orginfile.read(dataSize)
            if not block:
                break
            newfile.write(block)

        print("零时文件创建成功结束")

        newfile.seek(0)
        orginfile.seek(0)
        orginfile.truncate()

        while True:
            block=newfile.read(dataSize)
            if not block:
                break
            orginfile.write(block)

        orginfile.close()
        newfile.close()

        print("加密成功")


        if os.path.exists(tmpfile):
            os.remove(tmpfile)
        else:
            print("删除失败，请手动删除tmp文件")

        print("删除临时文件")