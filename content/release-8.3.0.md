Title: RCE 8.3
Date: 2019-07-05 14:00
Category: Releases
Author: RCE

We recently released RCE 8.3, which increases the configurability of the TiGL viewer and furthermore includes some maintenance updates as well as security fixes and bugfixes.
Please see [GitHub](https://github.com/rcenvironment/rce/releases) for the full changelog.

In the past, TiGL Viewer was delivered together with RCE, which complicated the use of versions other than the one that was bundled with RCE.
In order to make it easier for users to substitute novel versions of TiGL Viewer, we have decoupled TiGL Viewer and RCE, and made the path used for calling the external executable of TiGL viewer configurable via the well-known `configuration.json` file.
We have furthermore opted to *not distribute* TiGL viewer as part of RCE starting with RCE 8.3.
If you would like to continue using TiGL viewer as part of your workflow or data analysis, please refer to the [**Migration Guide**](pages/documentation/migration-guide.html) for detailed instructions on how to do so.