===========
Packages
===========

This section concerns the Packages part of the **Medulla** tool.


By clicking on the Packages menu, users are directly taken to the packages accessible based on their permissions:

![Packages](images/packages.png)

In the left menu, there are various sub-menus regarding the packages:

![Submenu](images/sousmenu.png)

Adding a Package 
===================

From the main "package" icon, a creation interface and a wizard are available to assist in package creation.
To create a package, its installation must be silent or without user interaction.
MSI versions of applications should be preferred as they are developed for mass deployment silently.

To create a package, files constituting the package must be provided via:
-	Samba Share "Package";
-	MMC interface.

Samba Share "Package"
--------------------------

It allows for easier management of large files.
It is imperative to create a folder containing the files.
If your package contains a sub-folder, it must be zipped.

MMC Interface
----------------

Through the interface, simply load the necessary files.

![Source Package](images/sourcepaquet.png)

Creation Assistant
------------------------

Example of creating a package containing PDFCreator

Click on the "Add a package" menu
Then choose "Send from this page"
Select the .msi or .exe file of PDFCreator then
Click on transmit files

![PDFCreator](images/pdfcreator.png)

The file will then be transmitted to **Medulla**, which will attempt to automatically detect the installation command.

Fill in the "Name", "Version", and "Description" fields of the package.

In the request section, you can see the command generated automatically.
The installation command is generally of the form "filename" -ms 
Silent installation parameters can be added for InnoSetup as follows: 
/SP /VERYSILENT /NORESTART

![Command](images/command.png)

Click on "Validate" at the bottom of the page.
The package is then awaiting integration into the system and synchronization with various sites.
Once the package is synchronized, it appears in the list of available packages.

Deployment testing can be done on a test machine.

In this case, we observe that PDFCreator installed PDFArchitect and a Toolbar in Internet Explorer.

So, we need to search for solutions on the Internet with typical keywords like: "pdf creator silent installation toolbar".
The "wpkg" site provides interesting information:
http://wpkg.org/PDFCreator
Components=program,ghostscript,images2pdf,pdfarchitect...
Tasks=desktopicon,desktopicon\common,winexplorer

The official site also provides additional parameters.
http://www.pdfforge.org/content/setup-command-line-parameters
/COMPONENTS="comma separated list of component names"
Overrides the default components settings.
Sample: /COMPONENTS=”program,ghostscript,comsamples,helpfiles\english,languages\english”

Then edit the package to add the following parameters:
/COMPONENTS= "program,ghostscript,images2pdf,helpfiles,helpfiles\french,languages,languages\french" 
/MERGETASKS="!desktopicon" /ForceInstall

Assistance Command
----------------------

Most installers offer assistance, which can be launched from a CMD console:
c:\ myinstaller.exe / ?

Advanced Package Creation
----------------------------

From the Packages view, create a new package by filling in the fields for a classic deployment:

![Advanced Deployment](images/deploiementavance.png)

Further down on this same page, move the **Download File** action to the Workflow and define the URL containing the file to download

![Download File](images/downloadfile.png)

During package deployment, the file will be downloaded into the package folder on the client machine. It can be processed with the appropriate action.
Here, we have taken the case of the **Run Command** action.
So, move the **Run command** action to the Workflow and enter the command to process the downloaded file:

![Run Command](images/runcommand.png)

Click **Confirm** to create the package.

Another important function is present: the **Execute Script** function, which allows running a script in the desired language

![Script](images/script.png)

By clicking on the "Options" button, we can access a set of parameters allowing, for example, to choose the script suffix or the script hashbang:

![Options](images/options.png)

There is also the **Unzip a File** function, which allows unzipping a file containing multiple files.
For this function, simply pass the filename and the agent will unzip the file before executing the installation.
Similarly, in the options of this function, we can pass, for example, a folder path to unzip the file into, as well as other options.

![Unzip](images/dezip.png)

Package Deployment
-----------------------

During deployment, the progress of the steps is displayed. The following lines show that a download is taking place and it is successful:

![Success](images/succes.png)

In case of error, the following lines are displayed:

![Failure](images/echec.png)

And in the general view of deployments, the status is as follows: **ABORT TRANSFER FAILED**

Scheduled Deployment
======================

This type of deployment allows scheduling when the deployment will take place but also several options:

![Program](images/program.png)

The different fields to fill in are as follows:
- The command name,
- The notion of start and end range, which freezes a deployment window,
- The deployment interval, which defines a time range during which the deployment should take place,
- Deployment prioritization, for example, if multiple deployments are already in progress.

Group Deployment
=======================

Group deployment is identical to unit deployment. However, additionally, there is application convergence, see the next point.

![Convergence](images/convergence.png)

Convergence
============

Convergence is a specific deployment that has the particularity of not having an end.
It will check every day that the stations are compliant with what has been defined and will make them compliant if necessary.
Beforehand, your packages must be ready for convergence. Also, convergence applies only to groups.
To make convergence available for a package, it must be associated with its inventory footprint.

Example with the 7-ZIP package:
The package has been created and installed for the first time.
Associate the package with its inventory.

![7-ZIP](images/7zip.png)

From three characters onwards, the completion proposes a list of corresponding inventory entries.
Select the one corresponding to the software, and convergence becomes available during deployment on a group.

![Inventory Entry](images/orange.png)

To activate convergence, select the orange "infinity" icon.

![Convergence](images/convergence2.png)

Convergence has no end; its scheduling is defined by a deployment interval.

For example, if we want an interval from 3 PM to 5 PM every day, it should be done like this: 

![Interval](images/intervalle.png)
