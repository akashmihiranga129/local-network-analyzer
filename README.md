# local-network-analyzer
A beginner friendly Windows CMD based Home Wi-Fi Network Analyzer project to explore local network devices using IP addresses, ARP tables, ping requests, and basic network scanning. Built to learn networking fundamentals and network discovery.

##  Overview

The **Local Network Analyzer** is a beginner-friendly networking project built with Python and Windows networking tools. It explores how devices on a local network can be detected and how their IP addresses can be associated with MAC addresses.

This project is designed to help beginners understand local network scanning, IPv4 addressing, subnetting, and ARP.

##  Features

- Scan a range of IP addresses on a local network.
- Check whether devices respond to ping requests.
- Retrieve IP to MAC address mappings from the ARP cache.
- Display network information in the Windows Command Prompt.
- Learn practical networking concepts through Python.

##  Technologies Used

- **Python**: Project scripting and automation.
- **Windows OS**: Operating system used to run the project.
- **IPv4 Networking**: Addressing devices on a local network.
- **Subnetting and IP Addressing**: Understanding local IP ranges.
- **ARP (Address Resolution Protocol)**: Mapping local IP addresses to MAC addresses.
- **MAC Addressing**: Identifying network interfaces at the link layer.

##  Requirements

Before running the project, make sure you have:

- A Windows computer.
- Python installed.
- An active connection to the local network you want to analyze.
- Permission to scan the network.

##  Getting Started

Follow these steps to download, configure, and run the project.

### Step 1: Clone the Repository

Open Command Prompt or PowerShell and run:

```bash
git clone https://github.com/akashmihiranga129/local-network-analyzer.git
```

### Step 2: Navigate to the Project Folder

Move into the downloaded repository:

```bash
cd local-network-analyzer
```

### Step 3: Find Your Local IP Address

Open Command Prompt and run:

```cmd
ipconfig
```

Find your active network adapter and note these values:

- **IPv4 Address**
- **Subnet Mask**
- **Default Gateway**

For example:

```text
IPv4 Address . . . . . : 192.168.1.9
Subnet Mask . . . . . : 255.255.255.0
Default Gateway . . . : 192.168.1.1
```

Your actual network details may be different.

### Step 4: Configure the IP Address Range

Open `phase_01.py` in your preferred code editor.

Find the IP address prefix used by the scanner and adjust it to match your local network.

For example, if your local network uses `192.168.1.x`, the scan may target addresses from:

```text
192.168.1.1
through
192.168.1.254
```

If your network uses `192.168.0.x`, change the prefix from `192.168.1` to `192.168.0`.

**Important:** Do not assume every network uses the same IP range. Check your IPv4 address and subnet mask before changing the scanner configuration. The example above assumes a typical `/24` network with subnet mask `255.255.255.0`.

Save the file after making your changes.

### Step 5: Run the Python Script

From the project directory, run:

```bash
python phase_01.py
```

If your system uses the Python launcher, you can also try:

```bash
py phase_01.py
```

Follow the output displayed by the script.

##  How It Works

### 1. Scanning IP Addresses

The project uses ping requests to check whether devices respond at addresses within the configured IP range.

Example Windows Command Prompt command for a `192.168.1.x` network:

```cmd
for /L %i in (1,1,254) do @ping -n 1 -w 150 192.168.1.%i
```

What the command means:

- `for /L %i in (1,1,254)`: Iterates through the numbers 1 to 254.
- `ping -n 1`: Sends one ping request to each target.
- `-w 150`: Waits up to 150 milliseconds for a reply.
- `192.168.1.%i`: Builds the target IP address for each iteration.

This command is an example of the scanning approach. The IP prefix must match your local network, and the command may need to be adjusted depending on your configuration.

### 2. Retrieving ARP Information

After communicating with devices on the local network, Windows may have IP-to-MAC address mappings in its ARP cache.

Run:

```cmd
arp -a
```

The output can include:

| Field | Description |
|---|---|
| Internet Address | The IP address associated with an entry |
| Physical Address | The corresponding MAC address, when available |
| Type | Whether the entry is dynamic or static |
| Interface | The local network interface associated with the entries |

### 3. Analyzing the Results

The scan output and ARP cache can help you understand which local addresses responded and which IP-to-MAC mappings are available.

Keep in mind that the ARP cache may not include every device on the network. A device may also be active without responding to ping requests.

##  Example Output

The following output is **illustrative only**. Actual results depend on your network and the devices connected to it.

```text
========================================
 NETWORK ANALYZER | PHASE 01
       LOCAL NETWORK SCANNER
========================================

[INFO] Starting local network scan...
[INFO] Scanning configured IP range...
[INFO] Scan progress: 100%

[INFO] Retrieving ARP cache information...

Interface: 192.168.1.9

Internet Address      Physical Address      Type
192.168.1.1           00-11-22-33-44-55     dynamic
192.168.1.5           66-77-88-99-AA-BB     dynamic
192.168.1.12          CC-DD-EE-FF-00-11     dynamic

========================================
 Scan completed.
========================================
```

The IP addresses and MAC addresses above are fictional examples, not results from a real scan.

##  Limitations

- Some devices block ping requests and may not respond.
- A device can be online without replying to a ping.
- The ARP cache may not contain mappings for every device on the network.
- Completing the IP scan does not guarantee that every connected device has been discovered.
- An IP address or MAC address alone does not reliably identify a device's exact model or owner.
- ARP is primarily useful for discovering mappings on the local network segment.

##  Responsible Use

Use this project only on networks you own or have explicit permission to analyze.

Do not scan networks without authorization. Follow your organization's policies and applicable laws when working with network tools.

##  Detailed Explanation

For the development process and additional context, read the accompanying Medium article:

**[Building a Home Network Analyzer](https://medium.com/@akashmihiranga129/building-a-home-network-analyzer-ce327be12807)**

##  Author

**Akash Mihiranga**

- GitHub: [@akashmihiranga129](https://github.com/akashmihiranga129)
- Repository: [Local Network Analyzer](https://github.com/akashmihiranga129/local-network-analyzer)

##  Support

If you find this project useful for learning Python and networking, consider giving the repository a star on GitHub!
