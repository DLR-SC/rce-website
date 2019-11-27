Title: RCE 10.0
Date: 2019-11-22 08:00
Category: Releases
Author: RCE

We are pleased to announce the recent release of RCE 10.0 (Green Monkey). In addition to a number of minor changes, this release adds a welcome screen that helps new users with their first steps with RCE, an icon caching mechanism that improves the usability of RCE when working with remote tools, and an experimental feature for securely connecting multiple internal networks via the Internet. We furthermore included a first draft of an Administrator Guide that aims to help network administrators with evaluating the security impact of RCE.

Please see [GitHub](https://github.com/rcenvironment/rce/releases) for the full changelog.

### Welcome Screen
Previous versions of RCE greeted new users with a blank workflow editor upon their first startup. While there existed and still exists documentation for the first steps in the User guide as well as in the included example workflows, this information was not easily discoverable for first-time-users. To make RCE more welcoming to these users, RCE 10.0 includes a welcome screen that is shown on first startup and directs users towards the built-in example project and the user guide. It also contains links to our website and to the sign-up page for our newsletter. We hope that this initial welcoming aids users in their first steps with RCE.

![Photo]({attach}images/release-10.0.0/welcome.png)

### Icon Caching
A central feature of RCE is the seamless integration of remote tools into a local workflow. When editing a workflow, all tools are displayed with their name and, if set, with an icon identifying this tool. For remote tools, however, the icon was only shown if the tool was available when the workflow was loaded. Otherwise, the icon was replaced with a default RCE icon. This led to usability issues when working with large workflows, as the user would have to be connected with all remote tool suppliers in order to be able to easily navigate and inspect the workflow. Starting with RCE 10.0, RCE caches the icons of remote components and thus displays such icons even when offline.

### Experimental Secure Uplink
The standard network connections of RCE are only intended for use within a local, trustworthy network. Since RCE 7.0, we have furthermore offered secure SSH connections that allow connecting such networks via an unsecure intermediary, such as the Internet. Until now, each connection could only be used to connect two such networks, i.e., to construct a point-to-point connection between networks. This obviously led to a large setup overhead when working with tool providers in multiple networks. RCE 10.0 includes an experimental feature that allows an instance to function as a secure uplink server. Such an uplink server accepts secure connections from multiple clients and interconnects all these clients. This greatly simplifies setting up RCE networks between multiple collaborators that do not share local, secure networks.

See the RCE 10 [**User Guide**](pages/documentation/documentation.html) (Section 3.6.2) for more information on how to set up a secure uplink server.

![Photo]({attach}images/release-10.0.0/uplink.png)

This feature will be fully released soon.

### Administration Guide
When using RCE to set up connections via the internet, it has to be evaluated how this connection impacts the security of the local network. In order to aid network administrators in this task, we have published a first draft of a [**guide**](pages/documentation/documentation.html) for administrators that covers the technical details of the implementation of RCE's network connections. It is furthermore intended to serve as a collection of best practices when setting up and configuring RCE networks.

### Technical Improvements
We have fixed and improved a number of technical issues and inconveniences in RCE. Please refer either to Github for a summary of these changes, or to our public issue tracker for a more detailed overview.