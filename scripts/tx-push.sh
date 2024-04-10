#!/bin/bash

# This script maps PO and POT files to transifex ressources
# on https://transifex.mandriva.com

SCRIPT_PROJECT=`pwd`

which tx > /dev/null
if [ $? -ne 0 ]; then
    echo "Install the transifex client v0.4 (pip install transifex-client==0.4)"
    exit 1
fi

#test -d .tx || tx init --host=https://fr.transifex.com/

args=$@

modules="index contribute admin audit firststep rdp reboot update gui installagent installdocker installlinux installmedulla installvbox machine_group pulse_agent technicaloperations glpi deploy_agent imaging historique interface packages admin introduction audit computers"

for mod in $modules
do
    cd $SCRIPT_PROJECT/../source/locale/
    tx push -r medullas-documentation.${mod} -s -t
    #-f --no-interactive
done
~   
