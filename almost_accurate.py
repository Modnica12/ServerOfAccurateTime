import socket
from datetime import datetime, timedelta

IP = "127.0.0.1"
UDP_PORT = 123
CONFIG_FILENAME = "server_conf.txt"


def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((IP, UDP_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        current_date = datetime.now()
        with open(CONFIG_FILENAME, 'r') as conf:
            date_with_offset = current_date + timedelta(seconds=int(conf.readline()[:-1]))
            sock.sendto(bytearray(str(date_with_offset.time()), encoding='UTF-8'), addr)


if __name__ == '__main__':
    main()
