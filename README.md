# Network Packet Capture and Analysis Tool

## Description

This repository contains a network packet capture and analysis tool written in Python. The script allows users to capture packets on a specified network interface and provides basic information about the captured packets, such as whether they are ARP or IP packets.

## Features
- Captures network packets from a specified interface.
- Filters packets using custom filters (e.g., `arp`, `ip`).
- Decodes Ethernet frames and provides basic details about ARP and IP packets.

## Usage

To use the script, run the following command:

```bash
python packet_capture.py -i <interface> -f <filter>
