=============
Agent **Medulla**
=============

This section concerns the Agent part of the **Medulla** tool.


The **Medulla** agent consists of 5 services:
- FusionInventory: OCS-compatible inventory agent
- OpenSSH: SSH remote access server
- TightVNC: VNC remote desktop
- Pulseagent: the **Medulla** agent service.
- Pulse Network Notify: Service to detect interface changes
The agent is available for Windows, Mac, and Linux.

Windows Agent
==============

By default, during its installation, **Medulla** generates a set of agents:

- Pulse-Agent-windows-Minimal-Latest.exe	← Latest version of the interactive agent containing the bare minimum. During installation on the server, the agent will download the dependencies and necessary components.
- Pulse-Agent-windows-Minimal-x.x.x.exe	← Interactive agent containing the bare minimum tagged by version.
- Pulse-Agent-windows-Full-Latest.exe	← Latest version of the agent with interaction and visible interface containing all the components to perform the installation.
- Pulse-Agent-windows-Full-x.x.x.exe	← Agent with interaction and visible interface tagged by version.

The agents are accessible from the following URL:
|	http://ippulse/dowloads/clients/win/

Generating Agents
----------------------

From the **Medulla** console, go to:
# cd /var/lib/pulse2/clients/
# ./generate-pulse-agent.sh

Usage: 
./generate-pulse-agent.sh [--conf-xmppserver=<XMPP configuration server IP>] 
        [--conf-xmppport=<XMPP configuration server port>] 
        [--conf-xmpppasswd=<XMPP configuration server password>] 
        [--aes-key=<32-character AES PSK>] 
        [--xmpp-passwd=<XMPP server password>] 
        [--chat-domain=<XMPP domain>] 
        [--inventory-tag=<Tag added during inventory>] 
        [--minimal [--base-url=<URL used to download the agent and its dependencies>]] 
        [--disable-vnc (Disable VNC support)] 
        [--vnc-port=<VNC port, default is 5900>] 
        [--ssh-port=<SSH port, default is 22>] 
        [--disable-rdp (Disable RDP support)] 
        [--disable-inventory (Disable inventory support)] 
        [--linux-distros (Linux distributions used)]

Agent and Tag
-------------

The **Medulla** agent can be tagged to provide an additional discriminator.

There are several ways to generate this tag:
- Deploy a tag on a computer already possessing a **Medulla** agent
- Generate a **Medulla** agent with a tag

Deploy a Tag on a Computer Already Possessing a **Medulla** Agent
----------------------------------------------------------------

Simply create the appropriate registry key and use **Medulla** to deploy it.


Generate a **Medulla** Agent with a Tag
-----------------------------------------

Go to the following directory:
# cd /var/lib/pulse2/clients

And generate the **Medulla** agent with the desired tag (Example: desk101)
# ./generate-pulse-agent.sh --inventory-tag desk101

Mac Agent
==========

The agent is accessible from the following URL:
	http://ippulse/dowloads/clients/mac/Pulse2AgentsInstaller.tar
    
The installer must be authorized to run in security settings.
Also, as a prerequisite before installing the Pulse package, Xcode corresponding to your version must be installed.

Generate a **Medulla** Agent with a Tag
-----------------------------------

Similar to Windows, go to the following directory:
# cd /var/lib/pulse2/clients/

Then run this command with the desired TAG (Example: desk101)
# ./generate-agent.sh --tag=desk101

Linux Agent
============

The agent is accessible from the following URL:
	http://ippulse/dowloads/linux/Pulse-Agent-linux-MINIMAL-latest.sh

Generate a **Medulla** Agent with a Tag 
-----------------------------------

The procedure is the same as for Mac:

# cd /var/lib/pulse2/clients/
# ./generate-agent.sh --tag=desk101
