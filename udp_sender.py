import socket
import time

def start_udp_client(ip, port):
    """
    지정된 IP 주소와 포트에서 UDP 신호를 수신하는 함수.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))

    print("Listening on {}:{}".format(ip, port))

    while True:
        data, addr = sock.recvfrom(1024)  # 버퍼 크기는 1024 바이트
        print("Received message: {} from {}".format(data.decode(), addr))
        result = data.decode()
        udp_my_ip = "127.0.0.1"  # 유니티가 실행되고 있는 IP 주소
        udp_my_port = 9875  # 유니티에서 설정한 포트 번호

        send_udp_signal(udp_my_ip, udp_my_port, str(result))
        print("Sent UDP signal to {}:{} with result '{}'".format(udp_my_ip, udp_my_port, result))


def send_udp_signal(ip, port, message):
    """
    지정된 IP 주소와 포트로 UDP 신호를 보내는 함수.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (ip, port))
    sock.close()

def analyze_eeg_data():
    # EEG 신호를 분석하여 0, 1, 2 중 하나의 결과를 3초마다 반환하는 함수
    result = 0
    while True:
        yield result
        result = (result + 1) % 2
        time.sleep(3)  # 3초 대기

def main():

    udp_ip = '0.0.0.0'  # 모든 네트워크 인터페이스에서 수신
    udp_port = 9876  # 서버에서 설정한 포트 번호

    start_udp_client(udp_ip, udp_port)

if __name__ == '__main__':
    main()