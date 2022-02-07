# pem-gen-for-zerossl
ZeroSSL產生的憑證檔案要合併成pem的簡易工具


# Docker

Build
```shell
docker build -t pem-gen-for-zerossl . --no-cache
```

Execute
```shell
docker run -v "{ssl_folder}:/ssl" -e PEM_FILE_NAME={pem_file} davidchen03/pem-gen-for-zerossl
```
> 參數說明
> 
> `ssl_folder`: 從ZeroSSL下載後解壓縮的資料夾位置
> 
> `pem_file`: 產生出的`.pem`檔案名稱