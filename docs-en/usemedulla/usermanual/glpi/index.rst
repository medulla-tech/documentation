===========================================
Correlation with Asset Management Tool
===========================================

This section concerns the GLPI configuration part of the Pulse tool.


Local GLPI
===========

By default, Pulse has an existing configuration to use the local GLPI.
Simply connect to the following address: http://ippulse/glpi

To log in:
-	Login: root
-	Password: the one used during Pulse installation

Existing GLPI
==============

To connect Pulse to an existing GLPI, it needs to be configured in the following file:

# vi /etc/mmc/plugins/glpi.ini.local

The main elements are:

[main]
dbhost =            ← IP of GLPI SQL base
dbname =            ← GLPI database name
dbuser =            ← GLPI database user
dbpasswd =          ← GLPI database password
glpi_computer_uri = ← URL link between Pulse and GLPI

[webservices]
purge_machine =     ← deletion from Pulse
glpi_base_url =     ← GLPI base URL
glpi_username =     ← GLPI admin user
glpi_password =     ← admin password

[authentication_glpi]
baseurl =           ← URL for identification

Also, ensure that the inventory server is relayed to the correct GLPI server. The configuration is done in the following file:

# vi /etc/mmc/pulse2/inventory-server/inventory-server.ini.local

[main]
url_to_forward =
http://serverglpi/glpi/plugins/fusioninventory/front/plugin_fusioninventory
.communication.php

Displaying Machines
=======================

Pulse allows selective display of GLPI computers based on the following filters:
-	state
-	type
-	entity

Convention for filter usage:
i.e. state=1 type=2|3|7 entity=2|5
filter_on = state=3

Entities and Locations
=================

Top-level entities are reserved for physical sites where Pulse is installed or a multi-site Pulse.

GLPI allows assigning computers to entities and locations based on discriminant criteria (IP address, subnet mask...). It can also use the agent's TAG.
These rules work as a stack. The order of these stacks goes from top to bottom and stops as soon as a criterion matches one of these rules.
Rules consist of a set of name, criterion(s), and action(s).

Entity Rule
-------------------

Possible discriminant criteria include:

-	IP address
- Domain
-	Computer name
-	Serial Number
-	Subnet
-	Operating system / Comment
-	Fusioninventory label

Example :
~~~~~~~~~~

.. image:: images/rules.png

Possible actions include:
-	Entity
-	Location
-	Entity from TAG
-	Ignore during import

.. image:: images/actions.png

Location Rules
---------------

Identical to entities, this section allows separating entities for more details.

Group Management
====================

Group management allows GLPI groups to match Pulse groups.

Example :

-	GLPI-Hotliner minimum group for access to Pulse
- Assigns rights in GLPI based on the group.
- GLPI-Hotliner => access to Remote Desktop
- GLPI-Supervisor & GLPI-Technician => access to Pulse
- GLPI-Admin & GLPI-Super-Admin => access to Pulse with user management

Creating a Pulse Group
---------------------------

You need to create the necessary groups for using Pulse.

.. image:: images/group.png

The group must start with "GLPI-". It is recommended to follow the nomenclature in the example.

Synchronize GLPI Groups
------------------------------

To synchronize GLPI groups, go to the "Administration" tab, "Groups" then "LDAP directory link" and click on the "Import new groups" button.
Then import the new groups.

User Management
=========================

Assignment Rules and Profiles
--------------------------------

From GLPI, Administration >> Rules >> Rules for assigning user permissions, add a new rule:

.. image:: images/newrule.png

Then add a membership criterion to the new group:

.. image:: images/criteria.png

And finally, add an action that assigns users to the desired entity and assigns a rights profile to these users:

.. image:: images/assign.png

Adding the User to the Group in Pulse
-------------------------------------------

To add a user to a group in Pulse, edit a user and add their group:

.. image:: images/addgroup.png

Default groups provide full access to all entities.

Upon logging into Pulse, this user will be confined to the corresponding entity, the same restriction applies in GLPI.

It is obviously possible to repeat the operation with a second group and a second entity.

Pulse Application Dictionary
==============================

In the following directory, a set of filters allows the renaming and standardization of inventory values. These rules are applied on-the-fly to inventories.

# cd etc/mmc/pulse2/inventory-server/xml-fix
# ls
00_Replace_bad_characters.py  
01_Dell_consistency.py     
02_ATI_consistency.py   
03_ASUS_consistency.py  
04_Adobe_consistency.py  
05_HP_consistency.py     
06_Laptop_type.py    
07_Virtual_machine_type.py  
08_Microsoft_consistency.py
99_Strip_leading_trailing_spaces.py

Example of Dell manufacturer standardization:

def xml_fix(xml):
  import xml.etree.cElementTree as ET
  xml = ET.fromstring(xml)
  tree = ET.ElementTree(xml)
  root = tree.getroot()
  for subelem1 in root:
    if subelem1.tag == 'CONTENT':
      for subelem2 in subelem1:
          for subelem3 in subelem2:

            # DELL vendor name should always be the same
            if subelem3.text in ['DELL', 'Dell Corp.', 'Dell Computer Corp.', 'Dell', 'Dell Computer Corporation']:
              subelem3.text = 'Dell Inc.'

  return ET.tostring(root)
