from cryptography.fernet import Fernet
import os

# 1. 生成密钥并保存到文件中
# 解释：生成一个对称加密密钥，用于加密和解密视频文件
def generate_key():
    key = Fernet.generate_key()
    with open('Encrypted_demo\secret.key', 'wb') as key_file:
        key_file.write(key)

# 2. 加载密钥
# 解释：从文件中读取之前生成的密钥
def load_key():
    return open('Encrypted_demo\secret.key', 'rb').read()

# 3. 加密视频文件
# 解释：使用加载的密钥对视频文件进行加密
def encrypt_video(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)
    
    # 读取视频内容
    with open(input_file, 'rb') as file:
        original_data = file.read()
    
    # 加密数据
    encrypted_data = fernet.encrypt(original_data)
    
    # 将加密后的数据写入到输出文件中
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

# 4. 解密视频文件
# 解释：使用相同的密钥对加密的视频文件进行解密
def decrypt_video(input_file, output_file):
    key = load_key()
    fernet = Fernet(key)
    
    # 读取加密的视频内容
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    
    # 解密数据
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # 将解密后的数据写入到输出文件中
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

# 主函数执行流程
def main():
    # 生成密钥（仅需执行一次）
    if not os.path.exists('secret.key'):
        generate_key()
    
    # 输入视频文件路径
    input_video = 'D:/Semester9/GradDesign/Prototype1/1.mp4'
    encrypted_video = 'encrypted.mp4'
    decrypted_video = 'decrypted.mp4'

    # 加密视频
    encrypt_video(input_video, encrypted_video)
    print(f"视频已加密，保存为 {encrypted_video}")

    # 解密视频
    decrypt_video(encrypted_video, decrypted_video)
    print(f"视频已解密，保存为 {decrypted_video}")

if __name__ == "__main__":
    main()
