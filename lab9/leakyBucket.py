def main():
    bucketSize = int(input('Enter the bucket size: '))
    outputRate = int(input('Enter the output rate: '))
    numberOfPackets = int(input('Enter number of packets: '))
    for i in range(0, numberOfPackets):
        print('Packet number: ')
        print(i+1)
        packetSize = int(input('Enter packet size: '))
        if packetSize < bucketSize:
            if(packetSize <= outputRate):
                print('Bucket output successful!')
                print('Last bytes sent: ')
                print(packetSize)
            else:
                print('Bucket output successful!')
                print('Bytes outputted: ')
                print(outputRate)
                sent = packetSize - outputRate
                print('Last bytes sent: ')
                print(sent)
        else:
            print('Bucket Overflow!!')


main()
