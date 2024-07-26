import socket
import os

#host to listen on 
HOST = '192.168.1.203'

def main():
    #create raw socket, bin to public interface 
    if os.name == 'nt':
        socket_protocol = socket.IPPROTO_IPV6
    else: 
        socket_protocol = socket.IPPROTO_ICMPV6

    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind((HOST, 0))

# include IP header in capture 
    sniffer.setsockopt(socket.IPPROTO_IPV6, socket.IP_HDRINCL,1)

# read packet
    if os.name == 'nt':
      sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    print(sniffer.recvfrom(65565))
     
# Logged through window, turn off promiscous mode
    if os.name == 'nt':
      sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    
if __name__ == '__main__':
     main()    
    