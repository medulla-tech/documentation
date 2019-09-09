=============
Agent Medulla
=============

| Cette section concerne la partie Agent de l'outil Medulla.
|

| L'agent Medulla est composé de 5 services :
| -	FusionInventory : agent d'inventaire compatible « OCS »
| -	OpenSSH : serveur d'accès à distance « SSH »
| -	TightVNC : bureau à distance « VNC »
| -	Pulseagent : le service de l’agent medulla.
| -	Medulla Network Notify : Service qui permet de detecter des changements d’interfaces
| L’agent est décliné pour Windows, Mac et Linux.

Agent Windows
==============

| Par défaut lors de son installation, Medulla génère un ensemble d’agents :
|
| -	Medulla-Agent-windows-Minimal-Latest.exe	← Dernière version de l'agent interactif contenant le strict minimum. Lors de l’installation sur le serveur, l'agent va télécharger les dépendances et les composants nécessaires.
| -	Medulla-Agent-windows-Minimal-x.x.x.exe	← Agent interactif contenant le strict minimum tagué par version.
| -	Medulla-Agent-windows-Full-Latest.exe	← Dernière version de l'agent avec interaction et interface visible contenant l’ensemble des composants pour réaliser l’installation.
| -	Medulla-Agent-windows-Full-x.x.x.exe	← Agent avec interaction et interface visible tagué par version.
|
| Les agents sont accessibles depuis l’url suivante :
|	http://ippulse/dowloads/clients/win/

Génération des agents
---------------------

| Depuis la console Medulla se rendre :
| # cd /var/lib/pulse2/clients/
| # ./generate-medulla-agent.sh
| 
| Usage: 
| ./generate-medulla-agent.sh [--conf-xmppserver=<ip du serveur de configuration XMPP>] 
|         [--conf-xmppport=<port du serveur de configuration XMPP>] 
|         [--conf-xmpppasswd=<Mot de passe du serveur de configuration XMPP>] 
|         [--aes-key=<32-character AES PSK>] 
|         [--xmpp-passwd=<Mot de passe du serveur XMPP>] 
|         [--chat-domain=<Domaine XMPP>] 
|         [--inventory-tag=<Tag ajouté lors de l’inventaire>] 
|         [--minimal [--base-url=<URL utilisée pour télécharger l’agent et ses dépendances>]] 
|         [--disable-vnc (Désactiver le support vnc)] 
|         [--vnc-port=<Port VNC, par défaut 5900>] 
|         [--ssh-port=<Port SSH, par défaut 22>] 
|         [--disable-rdp (Désactiver le support RDP)] 
|         [--disable-inventory (Désactiver le support de l’inventaire)] 
|         [--linux-distros (Distributions linux utilisées)]

Agent et TAG
-------------

| L’agent Medulla peut être tagué afin d’offrir un discriminant supplémentaire.
|
| Il existe plusieurs façons de générer ce TAG :
| -	Déployer un TAG sur un ordinateur possédant déjà un agent Medulla
| -	Générer un agent Medulla avec un TAG

Déployer un TAG sur un ordinateur possédent déjà un agent Medulla
-----------------------------------------------------------------

Il suffit de créer la clé de base de registre adéquate et utiliser Medulla pour la déployer.


Générer un agent Medulla avec un TAG
------------------------------------

| Il faut aller dans le dossier suivant :
| # cd /var/lib/pulse2/clients
| 
| Et générer l'agent Medulla avec le tag voulu (Exemple : bureau101)
| # ./generate-medulla-agent.sh --inventory-tag bureau101

Agent Mac
==========

| L’agent est accessible depuis l’url suivante :
| 	http://ippulse/dowloads/clients/mac/Pulse2AgentsInstaller.tar
|     
| Il faudra autoriser l’installeur à s’exécuter dans les paramètres de sécurité.
| Par ailleurs, en pré-requis avant d’installer le package Medulla, il faut que Xcode correspondant à votre version soit installé.

Générer un agent Medulla avec un TAG
------------------------------------

| Similaire à Windows, il faut aller dans le dossier suivant :
| # cd /var/lib/pulse2/clients/
| 
| Puis lancer cette commande avec le TAG voulu (Exemple : bureau101)
| # ./generate-agent.sh --tag=bureau101

Agent Linux
============

| L’agent est accessible depuis l’url suivante :
| 	http://ippulse/dowloads/linux/Medulla-Agent-linux-MINIMAL-latest.sh

Générer un agent Medulla avec un TAG 
------------------------------------

| La manipulation est la même que pour Mac :
|
| # cd /var/lib/pulse2/clients/
| # ./generate-agent.sh --tag=bureau101
