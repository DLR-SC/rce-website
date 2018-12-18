Title: RCE 9.0.0 beta
Date: 2018-12-17 14:00
Category: Releases
Author: RCE



We recently released a public beta version of RCE 9.0, which includes new features as well as improvements to existing ones.
In the following, we give an overview over the highlights of this version.
A full changelog will, as usual, be available together with the final release.

Being a beta version of the forthcoming RCE 9.0, this version contains nearly all functionality which is planned to be included in the full release.
The documentation and the graphical interface, however, are not yet finished and are due to change before the release in early 2019.

Implementing the new features of RCE 9.0 required significant changes to the way the user profiles are stored.
Hence, depending on your configuration, some manual steps may be necessary when upgrading existing profiles.
If you would like to reinstate these settings, please consult the [**Migration Guide**](pages/documentation/migration-guide.html).
Moreover, the same changes required raising the minimal required Java version to Java 8u161.

### New Authorization System

RCE now features a fine-grained publication system that allows granting access to published tools only to certain users.
While previously, a published tool was accessible to all instances in the same RCE network, users can now create so-called "Authorization Groups" and restrict access to a published tool to members of certain groups.
Moreover, tools can be assigned to the pre-defined "public" group, which models the old behavior of making a tool accessible to every visible RCE instance.

![Photo]({attach}images/release-9.0.0/authorization.png)

### New Command Line Commands

We have implemented the new commands `wf details` and `wf open` to further inspect the execution of a workflow from the command line, e.g., when running RCE in headless mode or accessing an instance via SSH.
The command `wf details` lists detailed statistics for a workflow execution including its current status, the workflow controller used, and the number of executions of each component.
When using the RCE GUI, the workflow execution can also be inspected via the command `wf open`, which opens a graphical view displaying the number of executions and the current state of each component.

![Photo]({attach}images/release-9.0.0/wfdetails.png)

### Robustness Against Network Outages

In previous versions of RCE, all systems running any component of a distributed workflow had to be available both at the start of the workflow as well as during the whole duration of the workflow execution.
Otherwise, i.e., if any machine involved became unavailable or unresponsive at any point during the execution of the workflow, the whole execution was canceled.
With RCE 9.0, this is no longer the case:
The workflow controller now waits for temporarily unavailable machines to reconnect or recover.
Hence, the workflow execution can recover from temporary network disruptions and periods of high CPU load while executing workflow components.

### Enhanced Remote Access via SSH

We have significantly improved the capabilities of SSH connections between RCE instances.
Previously, only tools and workflows that satisfied strict requirements towards their inputs and outputs could be published via SSH.
With this new release, these requirements are dropped and all tools that are published in the "public" group (see "New Authorization System" above) are accessible via SSH.
Moreover, it is possible to publish arbitrary workflows via SSH.

Furthermore, SSH connections now support accessing tool documentation and automatically reconnect when a previously interrupted connection becomes available again.
Finally, canceling a workflow now also cancels all currently running remote tools that are accessed via SSH connections.

### Known Issues

* The view "Cluster Job Monitor" does currently not work. This will be fixed in the final release.
* It is not yet possible to unpublish a deactivated component. We will provide a mechanism to do so in the final release.

---
Please see the [**Migration Guide**](pages/documentation/migration-guide.html) for documentation about profile migration to RCE 9.