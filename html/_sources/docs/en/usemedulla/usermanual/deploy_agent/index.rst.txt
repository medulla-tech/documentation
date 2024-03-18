============================
Pulse Agent Deployment
============================

This section concerns the deployment part of the Pulse tool agent.


The Pulse agent can be installed via different methods:

- GPO
- PsExec
- PXE

Deployment via GPO
====================

It is possible to create a GPO containing the Pulse agent and configure it to start the installation when the computer starts up.

An explanatory video is available at this address:
https://vimeo.com/97123295

Deployment via PsExec
=======================

Deployment via PsExec is possible. To do this, use the following command:
psexec \\target-computer -c agent-pulse.exe -u Administrator -p password  

It should be noted that this method requires the following registry key on the computers:
HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\system /v LocalAccountTokenFilterPolicy /t REG_DWORD /d 1 /f

Deployment via PXE
====================

It is also possible to deploy the agent via PXE.
To do this, you need to transform the post-imaging script "Deploy Pulse Agents" into a boot service and add it to the default menu of Pulse.

Then, start the computer in PXE mode, then select "Deploy Pulse Agents". Upon rebooting the computer, the Pulse agent will be automatically installed.
