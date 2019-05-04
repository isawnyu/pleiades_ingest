# Assert aligments between Pleiades place resources and external resources

Pleiades supports two formats for specifying alignments between external gazetteer/atlas resources and Pleiades places:

 - [The "Linked Places Format"](http://whgazetteer.org/2018/09/11/lp-format/) developed by the World Historical Gazetteer, Pelagios, and Cultures of Knowledge.  
 - Our own "alignments json" format, described below.

# Minimaly sufficient LP format

TBA 

# Aligments JSON

A JSON file is required. It must contain a single object, which in turn contains one or more objects corresponding to each Pleiades resource to which references are to be added. The key for each of these objects must be the corresponding Pleiades URI. The value for each of these objects is a JSON array containing one or more objects whose attributes provide the bibliographic detail necessary to create a Pleiades reference citation.

The specification for this JSON file may be found in ```data/templates/references.hjson``` (hjson format). An example JSON file, generated from the specification, may be found in ```data/templates/references.json```. A schema (jsonschema format), suitable for validating references JSON files, may be found in ```data/schema/references.json```. 

