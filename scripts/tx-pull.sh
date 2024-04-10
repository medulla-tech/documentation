#!/bin/bash

# This script maps PO and POT files to transifex ressources
# on https://www.transifex.com
# tx script can be downloaded on https://developers.transifex.com/docs/cli
#
SCRIPT_PROJECT=`pwd`

which tx > /dev/null
if [ $? -ne 0 ]; then
        echo "Install the transifex client v0.4 (pip install transifex-client==0.4)"
        exit 1
fi

#TODO: Adapt to new transifex.
#test -d .tx || tx init --host=https://www.transifex.com

[ ! x$1 == x ] && lang="-l $1" && shift 1
args=$@

modules="index contribute admin audit firststep rdp reboot update gui installagent installdocker installlinux installmedulla installvbox machine_group pulse_agent technicaloperations glpi deploy_agent imaging historique interface packages admin introduction audit computers"
for mod in $modules
do
   cd $SCRIPT_PROJECT/../source/locale/
   echo `pwd`
   echo "tx pull -a -f -r medullas-documentation.p${mod} ${lang} ${args}"
   tx pull -a -f -r medullas-documentation.${mod} ${lang} ${args}
done


