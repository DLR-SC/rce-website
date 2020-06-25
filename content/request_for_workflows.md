Title: We are Looking For Workflow Samples 
Date: 2020-05-10 6:00
Category: News
Author: RCE

As part of the development of RCE, we are involved in a number of research projects.
Colleagues working on these projects regularly construct workflows that are far larger and more intricate than anything we envisioned when we started development.
While involvement in these projects allows for "keyhole insight" into the practical use of RCE, we are yet missing a comprehensive overview over the types of workflows constructed in practical use of RCE.

This overview is, however, necessary for continued user-focussed development of RCE.
Thus, we have decided to start an ongoing call for workflow samples.
If you have constructed or are currently constructing an RCE workflow, if you are free to share that workflow, and if you would like to support further development of RCE, please send a copy of that workflow to [rce@dlr.de](mailto:rce@dlr.de).

At this point we are only interested in the workflow file, i.e., the file ending in `.wf`.
If you are using RCE via its GUI, you can access the properties of any workflow-file via right-clicking on it in the Project Explorer and selecting the entry "Properties".
The third line in that window indicates the location of that file on your computer.

While we are currently working on a concrete research project in which we require real-life workflows (see below), we intend to retain these workflows for future research.
If you have already sent us a workflow for research purposes and would like to have it removed from our collection, please send an email to [rce@dlr.de](mailto:rce@dlr.de).
We will remove that workflow as soon as possible.
Please be aware that the workflow file contains the names as well as the configurations of all components used in that workflow.
This includes, in particular, the python scripts executed by Script components.

In the following we showcase one concrete project that requires such real-life workflows.
As part of his Bachelor Thesis, a student working at our institute is researching ways to automatically determine structures in RCE workflows.
It is our hope that this work will lead to better methods for understanding workflows.
We attach his call below in both English and German.

# English Version

Dear users of RCE,

my name is Dominik Schneider.
I am a dual student at DLR and have been working on RCE for three years now.
My study time is slowly coming to an end, the last step is now writing my bachelor thesis.

In my bachelor thesis I am trying to use different graph clustering methods to break up RCE workflows into groups.
The idea is based on the RCE feature that allows placing colored labels within a workflow.
In sample workflows as well as in workflows in productive use, these labels are used to identify related components.

Currently, these labels are created manually.
For this, the semantic meaning of the individual components and their interrelationships must be known.
My goal is to check whether components can be grouped without knowing the semantic meaning of the components.
Only the structure of the workflow should be used for this.
To be able to do the work I need as many workflows as possible for evaluation.

The workflows should have the following properties:

- The workflow contains several components.
- Components can be grouped semantically (e.g., as part of a simulation step).
- In the best case, labels are already drawn (not strictly necessary).

If you are uncertain whether a workflow fulfills these properties, I would still kindly ask you to send me the workflow.
The size of the workflows is not relevant for these experiments.
For the bachelor thesis it is certainly advantageous to examine workflows with a strongly varying number of components and deviations from the desired properties.

For my research only a workflow file with file extension `.wf` is necessary.
I do not require any associated tools, toolintegrations, files, logs or other outputs.
I am only concerned with the structure of the workflows, which is completely represented by the workflow files.
I ultimately only process the names of the components as well as connections between components including the used data types and the defined constraints.
The content of the data which is exchanged between the components does not matter (apart from the data types) and is not needed for the analysis.

If the attempt is successful, the project may even become a new feature of RCE.
Automated labeling of workflows could make working with RCE even more comfortable.

Thank you very much and best regards

Dominik Schneider

# German Version

Hallo Nutzerinnen und Nutzer von RCE,

mein Name ist Dominik Schneider.
Ich bin dualer Student beim DLR und arbeite mittlerweile seit drei Jahren an RCE.
Meine Studienzeit nähert sich langsam dem Ende, der letzte Schritt ist nun das Schreiben meiner Bachelorarbeit.

Im Rahmen meiner Bachelorarbeit versuche ich, mit verschiedenen Graph Clustering Methoden RCE Workflows in Gruppen aufzugliedern.
Die Idee basiert auf dem RCE Feature, farbige Markierungen innerhalb eines Workflows anzubringen.
Diese Markierungen werden in RCE als "Labels" bezeichnet.
Sowohl in Beispielworkflows als auch in Workflows im produktiven Einsatz werden diese Markierungen verwendet um zusammengehörige Komponenten zu kennzeichnen.

Diese Markierungen werden bisher manuell erstellt.
Hierfür muss die semantische Bedeutung der einzelnen Komponenten und ihrer Zusammenhänge bekannt sein.
Mein Ziel ist es zu prüfen, ob Komponenten gruppiert werden können, ohne dass die semantische Bedeutung der Komponenten bekannt ist.
Hierfür soll lediglich die Struktur des Workflows herangezogen werden.
Damit ich die Arbeit durchführen kann benötige ich möglichst viele Workflows zur Evaluation.

Die Workflows sollten folgende Eigenschaften haben:

- Der Workflow enthält mehrere Komponenten.
- Komponenten lassen sich semantisch gruppieren (z.B. als Teil eines Simulationsschrittes).
- Markierungen sind im besten Fall schon eingezeichnet (nicht zwangsweise notwendig).

Solltet ihr euch nicht sicher sein, ob ein Workflow diese Eigenschaften erfüllt, würde ich euch trotzdem bitten, mir den Workflow zukommen zu lassen.
Die Größe der Workflows ist nicht unbedingt relevant.
Für die Bachelorarbeit ist es sicherlich von Vorteil auch Workflows mit stark unterschiedlicher Komponentenanzahl und Abweichungen von den gewünschten Eigenschaften zu untersuchen.

Für meine Untersuchung ist lediglich eine Workflowdatei mit Dateiendung `.wf` notwendig.
Ich benötige keine zugehörigen Tools, Toolintegrationen, Dateien, Logs oder sonstige Outputs.
Es geht mir lediglich um die Struktur der Workflows, welche vollständig durch die Workflowdateien abgebildet wird.
Die Informationen, die ich letztendlich verarbeite, sind die Namen der Komponenten sowie Verbindungen zwischen Komponenten inklusive der verwendeten Datentypen und der festgelegten Constraints.
Welche Daten zwischen den Komponenten ausgetauscht werden spielt keine Rolle (abgesehen von den Datentypen) und werden nicht für die Analyse benötigt.

Wenn der Versuch erfolgreich ist, wird aus dem Projekt eventuell sogar ein neues Feature von RCE.
Automatisiertes Labeling von Workflows könnte das Arbeiten mit RCE noch angenehmer gestalten.

Vielen Dank und viele Grüße

Dominik Schneider
