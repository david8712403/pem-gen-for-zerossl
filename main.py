
def read_file_string(path: str):
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
    pem_str = read_file_string('ssl/certificate.crt') + \
              read_file_string('ssl/private.key') + \
              read_file_string('ssl/ca_bundle.crt')
    print(pem_str)
    write_pem_file("ssl/test", pem_str)
