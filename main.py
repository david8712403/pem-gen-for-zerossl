import os


def read_file(path: str):
    f = open(path, 'r')
    content = ''
    for line in f.readlines():
        content += line
    f.close()
    return content


def write_pem_file(filename: str, ssl_content: str):
    f = open(f'{filename}.pem', 'w')
    f.write(ssl_content)
    f.close()


if __name__ == '__main__':
    # certificate.crt → private.key → ca_bundle.crt
    file_name = os.getenv('PEM_FILE_NAME')
    pem_str = read_file('ssl/certificate.crt') + read_file('ssl/private.key') + read_file('ssl/ca_bundle.crt')
    write_pem_file(f'ssl/{file_name}', pem_str)
