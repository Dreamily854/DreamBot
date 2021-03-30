
# 参考文档 https://www.cnblogs.com/niuu/p/10107212.html

# references https://www.cnblogs.com/niuu/p/10107212.html (Chinese)

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

KEY = 'yAGJYT8vDEcue4Bliaf2rFI5edLat4lV'.encode('utf-8')
IV = b'cuy1vui422jef6z9'
class dreambot_aes:
    def __init__(self,KEY,IV):
        self.key = KEY
        self.iv = IV

    def add_to_16(self,text):
        # If 'text' is not a multiple of 16, fill in the multiple of 16 with spaces
        # 如果text不是16的倍数，就用空格补足为16的倍数
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    def encrypt(self,text):
        mode = AES.MODE_CBC
        text = self.add_to_16(text)
        cryptos = AES.new(self.key, mode, self.iv)
        cipher_text = cryptos.encrypt(text)
        # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        # Because the AES encrypted string is not necessarily the ASCII character set, 
        # there may be problems in saving the output, 
        # so it is converted to HEX string here.
        return b2a_hex(cipher_text)

    def decrypt(self,text):
        mode = AES.MODE_CBC
        cryptos = AES.new(self.key, mode, self.iv)
        plain_text = cryptos.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')

#EXAMPLE: dreambot_aes('yAGJYT8vDEcue4Bliaf2rFI5edLat4lV'.encode('utf-8'),b'cuy1vui422jef6z9').encrypt("annnnn")
