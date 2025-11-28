import sys
import getopt
import pcapy
from impacket.ImpactDecoder import EthDecoder

def handle_packet(hdr, data):
    """
    Callback for every packet captured.
    Decodes Ethernet frame and prints basic info.
    """
    packet = decoder.decode(data)
    print(packet)

def usage():
    print(f"Usage: {sys.argv[0]} -i <interface> -f <pcap_filter>")
    sys.exit(1)

def main():
    # Default settings
    dev = "eth0"
    filter_exp = "arp"

    # Parse command line arguments
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "i:f:")
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == "-i":
            dev = arg
        elif opt == "-f":
            filter_exp = arg
        else:
            usage()

    # Open the interface in promiscuous mode
    try:
        print(f"[INFO] Opening interface {dev} in promiscuous mode...")
        pcap = pcapy.open_live(dev, 1500, 1, 100)
        pcap.setfilter(filter_exp)
    except Exception as e:
        print(f"[ERROR] Failed to open interface: {e}")
        sys.exit(1)

    print(f"[INFO] Listening on {dev} with filter '{filter_exp}'...")
    print("[INFO] Press Ctrl+C to stop.\n")
    
    # Start capturing packets
    try:
        pcap.loop(0, handle_packet)
    except KeyboardInterrupt:
        print("\n[INFO] Capture stopped by user")
    except Exception as e:
        print(f"[ERROR] Capture error: {e}")

if __name__ == "__main__":
    decoder = EthDecoder()
    main()
