# 加密调用代码

from Encryption import Encryption
enc = Encryption('Debug\H128_data.dat')
enc.encryption()


# 解密调用代码

from Decrypt import Decrypt
dec = Decrypt('Debug\H128_data.dat')
dec.decrypt()
