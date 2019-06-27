Title: Migration Guide
Date: 2018-12-17 10:20
Author: RCE
status: hidden

####Migration of TiGL Viewer to RCE 9.1

In the past, TiGL Viewer was delivered together with RCE, which complicated the use of versions other than the one that was bundled with RCE.
In order to make it easier for users to substitute novel versions of TiGL Viewer, we have decoupled TiGL Viewer and RCE, and made the path used for calling the external executable of TiGL viewer configurable via the well-known `configuration.json` file.
Since the TiGL Viewer is only available on Windows, this migration only affects users running RCE on Windows and using the TiGL Viewer, either as a component as part of their workflow, or for data analysis during or after the execution of a workflow.

In order to continue using TiGL Viewer in your workflows, please download and install it according to the instructions found at `https://dlr-sc.github.io/tigl/`.
Subsequently, add the following lines to the top level of your `configuration.json`, which is usually found at `C:\Users\<user name>\.rce\<profile name>`:

    "thirdPartyIntegration": {
		"tiglViewer" : {
			"binaryPath" : "<Tigl Viewer Installation Directory>\\tiglViewer.exe"
		}
	}
	
This constitutes the minimal configuration for the TiGL Viewer to work.
You may set additional parameters defining the use of the TiGL Viewer in RCE.
Please refer to the user guide or the reference configuration for more details.

####Profile migration to RCE 9

As part of the new features introduced with RCE 9.0, we improved the way the RCE profiles are stored.
This, however, precludes us from automatically converting all settings made in user profiles created with older versions to the new format.
Hence, in order to reinstate the settings made with older versions of RCE, please follow the steps below.

* *New Validation Rules*   
We have introduced a new set of rules that define the valid component names, group identifiers, and version numbers.
These new rules are applied consistently to tool integration and remote access.
When using a profile containing tools that violate these rules, such tools will be deactivated.
In order to reactivate these tools, please edit the tool integration and adapt the invalid identifiers to the new rules as indicated in the tool integration wizard.
For more information on the range of valid identifiers, please refer to the user guide.

* *Republishing of Components*   
Due to changes to the component publishing system, previously published tools will be unpublished.
In order to republish the affected tools with the same permissions, add them to the pre-defined authorization group "public".
Please refer to the user guide for more details.
Remaining component publication entries in `configuration.json` and `published.conf` are ignored and are reported with a warning during startup.
You need to delete these entries manually in order to eliminate these (harmless) warnings.

* *SSH Connections*   
RCE supports publishing both individual components as well as complete workflows via SSH.
Previously, all published tools were also available to all instances connected via SSH.
Due to conceptual changes to the component publishing system, tools now have to be republished in the pre-defined authorization group "public" in order to be available via SSH.   
Moreover, in previous versions, only workflows that took a single string as their input and provided a single directory as their output could be published via SSH.
In RCE 9.0, we have introduced the new components `SCP Input Loader` and `SCP Output Collector`, which allow for publishing arbitrary workflows via SSH.
Since this novel system replaces the older one, you will have to adapt workflows published via SSH to use the new components in order to republish them.
Please refer to the workflow `05_Remote_Access/Remote_Workflow_Access_Template.wf` for an example how to use the new components.
More details are available in the user guide.