Title: RCE 9.1
Date: 2019-06-07 14:00
Category: Releases
Author: RCE

We recently released RCE 9.1, which increases the configurability of the TiGL viewer.
This release furthermore includes some maintenance updates, numerous enhancements to the documentation, as well as security fixes and bugfixes.
Please see [GitHub](https://github.com/rcenvironment/rce/releases) for the full changelog.

In the past, TiGL Viewer was delivered together with RCE, which complicated the use of versions other than the one that was bundled with RCE.
In order to make it easier for users to substitute novel versions of TiGL Viewer, we have decoupled TiGL Viewer and RCE, and made the path used for calling the external executable of TiGL viewer configurable via the well-known `configuration.json` file.
We have furthermore opted to *not distribute* TiGL viewer as part of RCE starting with RCE 9.1.
If you would like to continue using TiGL viewer as part of your workflow or data analysis, please refer to the [**Migration Guide**](pages/documentation/migration-guide.html#rce9) for detailed instructions on how to do so.

Moreover, we have addressed and fixed numerous issues with the behavior of the undo function.
Previously, numerous actions such as, e.g., editing properties could not be undone via the undo function, but had to be reverted manually.
Now, these actions can be reverted in the standard way.

Finally, starting with RCE 9.0, we have introduced the concept of authorization groups that allows users to give fine-grained access control to their published tools.
In order to facilitate administration of these authorization groups, we have added the related console commands to the command suite available to users with the roles `local_admin`, `instance_management_admin`, and `instance_management_delegate_user`.
