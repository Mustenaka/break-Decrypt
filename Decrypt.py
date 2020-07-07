import os

# 请填入需要解密的模型 文件名
class Decrypt:
    def __init__(self,filepath):
        self.filename=filepath

    def decrypt(self):
        filename = self.filename
        tmpfile = 'tempfileforDeepFaceBack.tmp' # 临时文件
        dataSize = 4096 # 请输入一个二次幂形式的参数

        newfile = open(tmpfile,'wb+')
        orginfile = open(filename,'rb+')

        # 验证是否重复加密/解密
        orginfile.seek(0)
        isDone = orginfile.read(4)
        if isDone != str.encode("Liya"):
            newfile.close()
            orginfile.close()
            os.remove(tmpfile)
            exit("文件未加密，请先加密")

        orginfile.seek(4)
        newfile.seek(0)

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

        print("解密成功")

        if os.path.exists(tmpfile):
            os.remove(tmpfile)
        else:
            print("删除失败，请手动删除tmp文件")

        print("删除临时文件")