Title: RCE 10.2.0
Date: 2020-11-16 08:00
Category: Releases
Author: RCE

We are happy to announce the recent release of RCE 10.2 (Green Monkey).
In addition to a number of minor improvements to both the user interface and the internal workings of RCE, this release includes a more powerful Switch component that allows forwarding inputs to an arbitrary number of succeeding components.
We have furthermore extended the script API available to tool integrators in the pre- and postscript and to workflow designers via the Script component.
Moreover, the Script component can now be configured to retain a single long-lived instance of a Python interpreter that executes all scripts used in a given workflow.

In addition to these production-ready features we introduce experimental support for integrating workflows as components.
We also included a number of robustness and stability improvements for the experimental SSH uplink connections.
We anticipate production-ready releases of both features in the upcoming RCE 11.0.

Please see [GitHub](https://github.com/rcenvironment/rce/releases) for the full changelog.


### Re-Designed Switch Component

The Switch component is one of the foundational building blocks of many RCE workflows, as it allows routing data to different components depending on some condition.
Previous versions of RCE restricted the Switch component to a single condition and routed data to one of at most two outputs if the condition evaluated to true or false, respectively.

In RCE 10.2 we lift this restriction and allow users to define an arbitrary number of conditions and corresponding outputs in a switch component.
Each output is associated with a condition and receives the input data if that condition evaluates to true.
Furthermore, the user may opt to only forward the data to the first output whose condition evaluates to true.
If no condition evaluates to true, then the component forwards the data to a default output.

As usual with component upgrades, this extension requires no action on the part of the user when opening workflows created with older versions.
Workflows containing old versions of the Script component will be updated when they are first opened with RCE 10.2 or later.
The original version will be stored in a backup for future use with older versions of RCE.

### Input File Factory in Python Module

When working with tools written in Python, tool integrators often use the pre-script of the tool integration to write a simple Python script to disk.
These scripts are in turn imported by the integrated tool in order to set some variables.
This process is inherently cumbersome and error-prone, since it amounts to implementing a small-scale code generator as part of the pre-script.
To simplify this process, we have extended the RCE Python-module with an "Input File Factory".
This factory facilitates the creation of such input files without resorting to manipulation of plain strings.

The module is available both in pre- and post-scripts as well as in scripts executed via the Script component in a workflow.
Please refer to the [user guide](https://rcenvironment.de/pages/documentation/documentation.html) or to the online help of the Script component for further information on the API of the Input File Factory.

### Python Script Execution via Agent

One of the most widely used built-in RCE-components is the script component.
This component allows users to execute arbitrary Python scripts, e.g., for small data conversions.
Previous versions of RCE offered the user two methods for executing such scripts:
Either via the Java-based Python implementation [Jython](https://www.jython.org/) or by using an external Python interpreter.

Both methods have drawbacks.
On the one hand, Jython supports only a limited subset of the complete Python ecosystem and only supports Python 2.7 for the foreseeable future.
On the other hand, using an external Python interpreter allows the developer to use custom-made Python interpreters and access to the expressive power of the complete Python language and its ecosystem.
This, however, comes at a severe runtime penalty, since RCE spawns a new instance of the interpreter for each execution of a script.
This serves to isolate subsequent script executions against one another.

In order to alleviate both shortcomings, we have introduced a new method for executing Python scripts in RCE 10.2, called the "Python Agent."
Users can select this agent as the execution method in the properties of each script component.
If at least one script component in an executed workflow uses this novel Python Agent for execution, RCE will spawn a single instance of an external Python interpreter for that workflow execution.
It will then execute all Python scripts that have the Python Agent set as their execution method using this single long-running process.
Thus, scripts can benefit from the complete Python ecosystem and custom-made interpreters while only suffering from a very minor overhead incurred by starting that interpreter.

### Workflow as Component (Experimental Feature)

One of the most commonly requested features is the possibility to not only build a workflow out of integrated tools, but to also include other workflows as components in a larger workflow.
This is often useful if a larger workflow comprises multiple disciplines, each of which communicates with others only via a well-defined and small interface.
Including each and every individual tool in one large workflow makes the resulting workflow hard to read, understand, and maintain.

Thus, in RCE 10.2, we have implemented a first prototype of functionality that allows the user to integrate a workflow as a component and to use that component just like any other tool in a workflow.
This functionality is currently only accessible via the command console, namely via the command `wf integrate`.
For more information, please refer to the [user guide](https://rcenvironment.de/pages/documentation/documentation.html).

Please be aware that this feature is currently experimental and not intended for productive use.
Details of the implementation are subject to change without prior notice which may lead to breaking workflows that use this feature.

For future versions we are working on a graphical interface which will make this feature more easily accessible.

### SSH Uplink Robustness

We have improved the resilience of SSH uplink connections against failed connection attempts and unstable network connections.
Due to the experimental nature of the SSH uplink in RCE 10, some failure conditions led to dangling network connections and problems with reconnecting.
This has been fixed in RCE 10.2.
While the SSH Uplink feature remains experimental and is still not recommended for use in production, with this update we have severely increased its usefulness for evaluation.