<h1>Python 3 Network Tutorial</h1>

This project takes baby steps into the creation of a network sniffer.

<h2>Running</h2>

<ol>
  <li>Clone repository</li>
  <li>Activate venv (optional)</li>
  <li>Open examples and run code inside each folder</li>
</ol>

<h2>Content</h2>

<h3>Dir 1 - socket initialization</h3>
<p>Single server.py file demonstrating socket creation</p>

<h3>Dir 2 - echo reply with sockets</h3>
<p>server.py and client.py. Client sends message to server and gets reply</p>

<h3>Dir 3 - echo reply witk threading</h3>
<p>client.py and server.py with threading and support for 20 clients</p>

<h3>Dir 4 - reverse tcp shell</h3>
<p>server.py waits for clients and on connect runs remote commands on client</p>

<h3>Dir 5 - echo server with socketserver</h3>
<p>server.py uses socketserver module to create a TCP server which echoes messages from client. client.py sends user input to server</p>

<h3>Dir 6 - Raw socket sniffer</h3>
<p>sniffer.py listens and outputs traffic with source and destination MAC/IP</p>

<h3>Dir 7 - Raw socket inject</h3>
<p>inject.py injects raw packet into network</p>

<h3>Dir 8 - Scapy sniffer</h3>