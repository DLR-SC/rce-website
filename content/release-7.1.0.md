Title: RCE 7.1 
Date: 2016-05-24 15:00
Category: Releases
Author: RCE
Image: release-7.1/general.png

With RCE 7.1 we release a new minor version with some major improvements for RCE. As always, here is a selection of some improvements.
Please see [GitHub](https://github.com/rcenvironment/rce/wiki/Changelog:-7.x.x-Releases) for the full changelog.

### Reworked Help System

In this release, we present the new RCE help system. You can open it by going to "Help -> Help Contents" in the menu bar. There you find not only all of the component's help, but also Tool Integration help and the user and developer guides.
The new system has a much better usability, being able to search through all help content and having a much better navigation. Also, the dynamic help for components got a unified and cleaner look.

![Photo]({attach}images/release-7.1/help_system.png)

### Outline View

When workflows use many components, they get quite big. For keeping track of the workflow, we added a new outline view. This view displays the complete workflow in a small image and shows which area of the workflow is currently shown in the workflow editor.

![Photo]({attach}images/release-7.1/outline_view.png)

### Canceling of Component Runs

It is now possible, to cancel integrated components, the Script component and the Cluster component during their execution. This can be useful, if a script or tool runs for a very long time, but it is already clear that the results won't be valid for example. You can then cancel the worfklow and save resources and time.

![Photo]({attach}images/release-7.1/canceled.png)

### SSH Remote Access Improvements

The SSH Remote Access was extended with the feature to use key file authentication. 
Secondly, it is now possible to use published workflows via the remote access.


### Component Improvements

Many components got some improvements, the most important are:

In the **XML Merger**, the mapping file can now be sent to the XML Merger as an input.  
The **Output Writer** got some new placeholders for naming the output file: "original filename" and "execution count".  
Failure tolerant loops can now be used with the **Evaluation Memory**.  
The data type "Matrix" is now available in the **Script Component**.  
For the **Converger**, a new selection of behaviour if check limit is reached was added.  