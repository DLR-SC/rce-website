Title: RCE Startup Issues
Date: 2020-01-17
Category: News
Author: RCE

We are currently investigating an issue occurring when running RCE on Windows 10.
In certain configurations RCE is unable to start and instead produces an error log in its installation directory.
This error is due to a third-party-library that is incompatible with newer versions of Windows 10.
We are working on a fix for this issue which will be available towards the end of next week.
This fix will *not be available via the RCE update mechanism*, but only for manual download on this website.

When starting RCE on an affected system, the splash screen shows up for a couple of seconds and disappears before the user is asked for a workspace.
No error message is shown.
After the splash screen has disappeared, an error log with a name like `rce_errorXXXX.log` appears in the installation directory of RCE (i.e., in the directory containing the file `rce.exe`).
This file starts with the following lines, where the JRE version and the Java VM indicate the versions installed on the user's machine.

	#
	# A fatal error has been detected by the Java Runtime Environment:
	#
	#  EXCEPTION_ACCESS_VIOLATION (0xc0000005) at pc=0x0000000010014ed4, pid=5516, tid=0x0000000000002ec8
	#
	# JRE version: OpenJDK Runtime Environment (8.0_202-b08) (build 1.8.0_202-b08)
	# Java VM: OpenJDK 64-Bit Server VM (25.202-b08 mixed mode windows-amd64 compressed oops)
	# Problematic frame:
	# C  [sigar-amd64-winnt.dll+0x14ed4]
	
This issue merely prevents RCE to start and does not affect any personal data.
The user's workspace and configuration are untouched.
This behavior has only been observed on machines running Windows 10 and does not occur on machines running Linux.

We use the third-party-library [SIGAR](https://github.com/hyperic/sigar) in RCE to collect information on system load when running on Windows.
There are no known issues with this library on Windows 7.
On certain Windows 10 configurations, however, the library causes the enclosing JVM to terminate upon virtually every API call.
Since this issue only affects certain configurations of Windows 10, this issue did not show up during testing of RCE 10.

Our first solution is to release a hotfix for this issue in which we disable system monitoring.
Since this fix removes functionality, we will not distribute it via the standard RCE update mechanism, but instead provide download links on [https://rcenvironment.de](https://rcenvironment.de).
For future releases we are working on replacing SIGAR with a more modern library for system monitoring that does not exhibit such behavior.