Title: RCE 10.1
Date: 2020-05-18 08:00
Category: Releases
Author: RCE

We are pleased to announce the recent release of RCE 10.1.
Besides fixing some minor bugs we implemented the following improvments.

## Profile Management and UI  
We added the possibility to select recently used profiles to the default selection menu. 
Also the correct version number will be displayed on these profiles. 
Furthermore we fixed some bugs that occured while upgrading profiles to a new version.

- Added the possibility to select recently used profiles th the default profile selection menu.
- Fixed bug in the profile selection menu that the correct versions will be displayed for recently used profiles
- Fixed bug when upgrading profiles

## Data Management  
A warning was added that appears when a not valid directory name is chosen for a specific platform.

- Added warning in case of directory names that are not valid on all platforms
- Fixed bug in the output writer that the file extension will be transferred correctly

## Tool Integration  
We improved the integration of tools to be more robust against several errors.

- Fixed bug in the tool execution that occured on Windows for "execution commands" that begin and end with a quotation mark
- Made integration more robust against errors in individual integrations

## Workflow Example Project  
A new example file was added to the Workflow Example Project that is compatible with CPACS3.

- Added example file for CPACS 3

## Monitoring  
- Replaced the previously used SIGAR library with the more up-to-date OSHI library
- Updated the displayed information about RCE subprocesses to platform changes

## Miscellaneous  
- Removed irrelevant log output on startup and shutdown
- Fixed minor GUI bugs
- Fixed a bug in "wf graph" console command

## Internal Improvements  
- Updated the reference checkstyle version to 8.30
- Updated Maven-checkstyle-plugin to 3.1.1
- Updated Easymock to 4.2
- Improved source compatibility with recent versions of Eclipse
- Added "Automatic-Module-Name" bundle headers
