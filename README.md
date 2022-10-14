<h1>Python 3 Network Tutorial</h1>

This project takes baby steps into the creation of a network sniffer.

<h2>Running</h2>

<ol>
  <li>Clone repository</li>
  <li>Activate venv (optional)</li>
  <li>Open examples and run code inside each folder</li>
</ol>

<h2>Content</h2>

<h3>Dir 01 - simple socket use case </h3>
<p>Simple socket creation demonstration - ping www.google.com</p>

<h3>Dir 02 - simple server and client use case </h3>
<p>server.py and client.py. Server waits for client and exits</p>

<h3>Dir 03 - simple server with threading and client</h3>
<p>client.py and server.py with threading and support for up to 20 clients</p>

<h3>Dir - server and client communication with threadind </h3>
<p>client.py and server.py communicationg with threading and support for up to 20 clients</p>



<h3>Dir 4 - reverse tcp shell</h3>
<p>server.py waits for clients and on connect runs remote commands on client</p>

<h3>Dir 5 - echo server with socketserver</h3>
<p>server.py uses socketserver module to create a TCP server which echoes messages from client. client.py sends user input to server</p>

<h3>Dir 6 - Raw socket sniffer</h3>
<p>sniffer.py listens and outputs traffic with source and destination MAC/IP</p>

<h3>Dir 7 - Raw socket inject</h3>
<p>inject.py injects raw packet into network</p>