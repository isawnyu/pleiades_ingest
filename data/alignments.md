# Assert aligments between Pleiades place resources and external resources

_Pleiades_ supports two formats for specifying alignments between external gazetteer/atlas resources and _Pleiades_ places:

 - [The "Linked Places Format"](http://whgazetteer.org/2018/09/11/lp-format/) developed by the [World Historical Gazetteer](http://whgazetteer.org/), [Pelagios](http://commons.pelagios.org/), and [Cultures of Knowledge](http://www.culturesofknowledge.org/).  
 - Our own "alignments json" format, described below.

## Minimaly sufficient "Linked Places" format

Alignments to _Pleiades_ from a third-party gazetteer or digital atlas can be suggested via a JSON-LD file conforming to [the "Linked Places" format](https://github.com/LinkedPasts/linked-places). The following components must be present, if applicable, for each feature to be aligned:

- "@id"
- "properties" : "title"
- "names"
- "geometry"
- "links"
  - at least one element with ```type``` of "closeMatch" or "exactMatch" and ```identifier``` containing the full _Pleiades_ place resource URI to which the alignment is to be made.

## Aligments JSON

A JSON file is required. It must contain a single object, which in turn contains one or more objects corresponding to each Pleiades resource to which references are to be added. The key for each of these objects must be the corresponding Pleiades URI. The value for each of these objects is a JSON array containing one or more objects whose attributes provide the bibliographic detail necessary to create a Pleiades reference citation.

The specification for this JSON file may be found in ```data/templates/references.hjson``` (hjson format). An example JSON file, generated from the specification, may be found in ```data/templates/references.json```. A schema (jsonschema format), suitable for validating references JSON files, may be found in ```data/schema/references.json```. 

