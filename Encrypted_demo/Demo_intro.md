# I know it's not right to save the key with plain text and upload it, but it's just a demo anyway.
# Video Encryption Demo

以下是一个使用 Python 对视频文件进行简单加密的代码原型，并包含各部分的详细解释。此代码将视频的内容读取并通过一个对称密钥进行加密，使用了常见的 cryptography 库。

## 代码解释：

### 生成密钥 (generate_key)：

使用 `Fernet.generate_key()` 生成一个对称加密密钥，并将其保存到一个文件中 (`secret.key`)。密钥在加密和解密过程中都会被使用。

### 加载密钥 (load_key)：

从保存的 `secret.key` 文件中读取加密密钥，用于加密或解密。

### 加密视频 (encrypt_video)：

加载密钥并使用它创建一个 `Fernet` 对象。
读取原始视频文件的内容，然后使用 `fernet.encrypt()` 对内容进行加密。
将加密后的内容写入到新的文件中。

### 解密视频 (decrypt_video)：

加载密钥并使用它创建一个 `Fernet` 对象。
读取加密的视频文件内容，使用 `fernet.decrypt()` 对内容进行解密。
将解密后的内容写入到新的文件中。

## 注意事项：

- 此方法使用对称加密算法，即相同的密钥用于加密和解密。因此，确保密钥的安全至关重要。
- 该示例适用于小型视频文件，对于大型视频文件，需考虑逐块读取和加密，以节省内存。