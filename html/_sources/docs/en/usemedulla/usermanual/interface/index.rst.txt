=====================================
Medulla Interface
=====================================

This section covers the interface part of the Medulla tool, including access to the interface, the homepage,


Web Browser
============================

Medulla's user interface is a web interface.
The following browsers are compatible:
- Microsoft Internet Explorer version 10 minimum
- Safari version 6.2 minimum
- Mozilla Firefox version 31 minimum
- Google Chrome version 32.0 minimum

Accessing the Interface
============================

To access the interface, the user must enter the following address in the browser's address bar: http://medulla-server/mmc/

Once the user arrives at the Medulla graphical interface, a username/password entry form is accessible, along with a drop-down menu to choose the language used.

![Connection](images/connexion.png)

Homepage
============================

Once logged in to the interface, you will have access to the Medulla homepage.
This homepage consists of 3 zones.

Menu Bar
----------------

The first zone is the top of the pages: the main menu.
It provides navigation between all Medulla modules.
The menus adapt according to the profile and rights of the user profile (cf ACL).

![Banner](images/bandeau.png)

In the case of this menu (in the screenshot above), the user has access to all functionalities.
In this screenshot, the profile is that of an administrator.

In this menu, you will find buttons to access the following functions:

- Dashboard
- Users
- Groups
- Computers
- Backup
- Imaging
- Packages
- Audit
- Services
- History
- Admin

Information Widget
---------------------

On the homepage, you will find a number of widgets that provide information easily.

![Dashboard](images/dashboard.png)

These widgets can be broken down into 2 categories:


* Information about the Medulla server itself:

    * Disk usage rate;
    * General server information: uptime (how long the server has been online), server RAM usage;
    * Available updates;
    * Extraction of logs and log files, and configuration files of the software;
    * The ability to restart/stop the Medulla server directly.

* Information about your park:

    * Computers with antivirus;
    * The number of machines online and offline;
    * The number of machines with the "Backup" function configuration active;
    * The number of computers that are up-to-date in the inventory, not inventoried, or out of inventory;
    * The various operating systems used on your computer park.

Widgets related to your park are in the form of pie charts. By clicking on the areas of the pie charts, you can create groups of machines corresponding to the areas.
For example, if you click on the "Windows 10 (2009)" area in Operating Systems, you will have machines with Windows 10 version 2009 as the operating system.

Location and Options Banner
-----------------------------------

Under the banner containing the menu of Medulla functions, you will find a banner that allows you to know
the location of the software's pages, to be able to log out or switch to expert mode (more information on this mode in the following chapters).

![Location](images/localisation.png)

Interface Organization by Zone
=====================================

![Zones](images/zones.png)

The interface is organized by zone:
For each module, there is a "Menu" zone located on the left.
Depending on the choice of the left menu, in the "Presentation" zone, you have either a list of results or an input form.
For the result type, there are different zones in the presentation panel:

* The "Filter" zone allows you to reduce the list of results presented according to a criterion.
* The "Action" zone allows, for the element of the line, to launch an action.

Actions on Elements
=============================

![Machines](images/machines.png)

In our example, List of machines from the "Computers" module,
we will find the following actions that can be performed for each machine:

![Machine Actions](images/actionsMachines.png)

Actions are represented by icons.
*Access to these different actions is configurable by user profile.*
You will find an explanation of the different icons in the corresponding chapters.
