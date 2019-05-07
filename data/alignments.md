# Assert aligments between Pleiades place resources and external resources

_Pleiades_ uses [the "Linked Places Format"](http://whgazetteer.org/2018/09/11/lp-format/) developed by the [World Historical Gazetteer](http://whgazetteer.org/), [Pelagios](http://commons.pelagios.org/), and [Cultures of Knowledge](http://www.culturesofknowledge.org/) to ingest information about alignments with external gazeteers, atlases, and the like. 

## Minimaly sufficient "Linked Places" format

Alignments to _Pleiades_ from a third-party gazetteer or digital atlas can be suggested via a JSON-LD file conforming to [the "Linked Places" format](https://github.com/LinkedPasts/linked-places). The following components must be present, if applicable, for each feature to be aligned:

- "@id"
- "properties" : "title"
- "names"
- "geometry"
- "links"
  - at least one element with ```type``` of "closeMatch" or "exactMatch" and ```identifier``` containing the full _Pleiades_ place resource URI to which the alignment is to be made.

A simple example file may be seen in ```data/templates/alignments-lp.json```.
