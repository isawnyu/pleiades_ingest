# Add references to existing Pleiades places

A JSON file is required. It must contain a single object, which in turn contains one or more objects corresponding to each Pleiades resource to which references are to be added. The key for each of these objects must be the corresponding Pleiades URI. The value for each of these objects is a JSON array containing one or more objects whose attributes provide the bibliographic detail necessary to create a Pleiades reference citation.

The specification for this JSON file may be found in ```data/templates/references.hjson``` (hjson format). An example JSON file, generated from the specification, may be found in ```data/templates/references.json```. A schema (jsonschema format), suitable for validating references JSON files, may be found in ```data/schema/references.json```. 

