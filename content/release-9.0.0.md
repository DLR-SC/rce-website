Title: RCE 9.0
Date: 2019-03-13 14:00
Category: Releases
Author: RCE

We recently released RCE 9.0, which includes new features as well as improvements to existing ones.
In the following, we give an overview over the highlights of this version.
Please see [GitHub](https://github.com/rcenvironment/rce/releases) for the full changelog.

Implementing the new features of RCE 9.0 required significant changes to the way the user profiles are stored.
Hence, depending on your configuration, some manual steps may be necessary when upgrading existing profiles.
If you would like to reinstate these settings, please consult the [**Migration Guide**](pages/documentation/migration-guide.html#rce9).
Moreover, the same changes required raising the minimal required Java version to Java 8u161.

### New Authorization System

RCE now features a fine-grained publication system that allows granting access to published tools only to certain users.
While previously, a published tool was accessible to all instances in the same RCE network, users can now create so-called "Authorization Groups" and restrict access to a published tool to members of certain groups.
Moreover, tools can be assigned to the pre-defined "public" group, which models the old behavior of making a tool accessible to every visible RCE instance.
The Authorization Groups are managed via the new Component Publishing view.

![Photo]({attach}images/release-9.0.0/authorization.png)

### Enhanced Remote Access via SSH

We have significantly improved the capabilities of SSH connections between RCE instances.
Previously, only tools and workflows that satisfied strict requirements towards their inputs and outputs could be published via SSH.
With this new release, these requirements are dropped and all tools that are published in the "public" group (see "New Authorization System" above) are accessible via SSH.
Moreover, it is possible to publish arbitrary workflows via SSH.

Furthermore, SSH connections now support accessing tool documentation and automatically reconnect when a previously interrupted connection becomes available again.
Finally, canceling a workflow now also cancels all currently running remote tools that are accessed via SSH connections.

### New Command Line Commands

We have implemented the new commands `wf details` and `wf open` to further inspect the execution of a workflow from the command line, e.g., when running RCE in headless mode or accessing an instance via SSH.
The command `wf details` lists detailed statistics for a workflow execution including its current status, the workflow controller used, and the number of executions of each component.
When using the RCE GUI, the workflow execution can also be inspected via the command `wf open`, which opens a graphical view displaying the number of executions and the current state of each component.

Moreover, we have implemented the commands `auth`, `auth create`, `auth delete`, `auth import`, `auth export`, and `auth list` to manage the creation and distribution of Authorization Groups (see ''New Authorization System'' above). For more information on these new commands, please refer to the [user guide](pages/documentation/documentation.html) or the built-in help system of the command console.

![Photo]({attach}images/release-9.0.0/wfdetails.png)

### New Naming Rules for Tools, Versions, and Group Names

In order to improve cross-platform support for tools and to simplify internal handling, we have added strict validation of tool names and versions as well as group names. Existing tools that violate these rules are automatically deactivated and have to be activated before becoming available again.

### Robustness Against Network Outages and High CPU Load

In previous versions of RCE, all systems running any component of a distributed workflow had to be available both at the start of the workflow as well as during the whole duration of the workflow execution.
Otherwise, i.e., if any machine involved became unavailable or unresponsive at any point during the execution of the workflow, the whole execution was canceled.
With RCE 9.0, this is no longer the case:
The workflow controller now waits for temporarily unavailable machines to reconnect or recover.
Hence, the workflow execution can recover from temporary network disruptions and periods of high CPU load while executing workflow components.


---
Please see the [**Migration Guide**](pages/documentation/migration-guide.html#rce9) for documentation about profile migration to RCE 9.