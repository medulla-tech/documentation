================================
Installer Medulla sur VirtualBox
================================

Pré-requis
------------

* PowerShell Core Version 6 ou supérieur
* VirtualBox version 7 ou supérieure

Si ces exigences ne sont pas remplies, elles seront installées.

NB: Pour installer PowerShell Core Version 6 ou supérieur, exécutez ce qui suit:

 PowerShell.exe -File. \ Create_vbox_Vm.ps1

Installation du serveur Medulla
-------------------------------

Pour créer une machine virtuelle et installer Medulla, la commande suivante doit être exécutée:

 pwsh.exe -File .\create_vbox_vm.ps1

La machine virtuelle créée aura les caractéristiques suivantes:

* Debian 12 OS à jour;
* 8 Go de RAM;
* 2 CPU.

Attendez que le processus d'installation se termine, un résumé affichera tous les mots de passe nécessaires (copiez-les dans un endroit sûr).
