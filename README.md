<h1>Python 3 Network Tutoria</h1>

This project takes baby steps into the creation of a network sniffer.

<h2>Running</h2>

<p>1. Clone repository</p>
<p>2. Run venv:<br /> source bin/activate</p>

<h2>Content</h2>

<h3>Dir 1 - socket initialization</h3>
<p>Single server.py file demonstrating socket creation</p>

<h3><b>Dir 2 - echo reply with sockets</h3>
<p>server.py and client.py. Client sends message to server and gets reply</p>

<h3>Dir 3 - echo reply witk threading</h3>
<p>client.py and server.py with threading and support for 20 clients</p>

<h3>Dir 4 - reverse tcp shell</h3>
<p>server.py waits for clients and on connect runs remote commands on client</p>

<h3>Dir 4 - echo server with socketserver</h3>
<p>server.py uses socketserver module to create a TCP server which echoes messages from client. client.py sends user input to server</p>