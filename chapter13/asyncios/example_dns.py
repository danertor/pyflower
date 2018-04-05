import asyncio
from contextlib import suppress

ip_map = { b'facebook.com.': '173.252.120.6',
           b'yougov.com.': '213.52.133.246',
           b'wipo.int.': '193.5.93.80'
           }

def lookup_dns(data):
    domain = b''
    pointer, part_length = 13, data[12]
    while part_length:
        domain += data[pointer:pointer+part_length] + b'.'
        pointer += part_length + 1
        part_length = data[pointer - 1]

    ip = ip_map.get(domain, '127.0.0.1')
    return domain, ip

def create_response(data, ip):
    ba = bytearray
    packet = ba(data[:2]) + ba([129,128]) + data[4:6] * 2
    packet += ba(4) + data[12:]
    packet += ba([192, 12, 0, 1, 0, 1, 0, 0, 0, 60, 0, 4])
    for x in ip.split('.'): packet.append(int(x))
    return packet

class DNSProtocol(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        print("Received request from {}".format(addr[0]))
        domain, ip = lookup_dns(data)
        ...




