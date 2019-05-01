# pleiades_ingest

Specifications, tools, and tests for ingesting external data into [the _Pleiades_ gazetteer of ancient places](https://pleiades.stoa.org).

Specifications, documentation, and example files are kept in ```data/```. There are four files for each type of ingest file _Pleiades_ is prepared to support. We'll use "references" as an example:

 - ```data/references.md``` introduces the basic file structure etc. and tells you where to find the rest of its documentation
 - ```data/templates/references.hjson``` provides the actual specification itself using [the hjson format](http://hjson.org) because it supports inline comments
 - ```data/templates/references.json``` is an example file, generated from the hjson spec
 - ```data/schemas/references.json``` uses [the jsonschema format](https://json-schema.org/) and serves to validate JSON files to ensure they conform to the spec

## generating example json files

```bash
pip install hjson
hjson -j data/templates/references.hjson > data/templates/references.json
```

## validating example json files

```bash
pip install jsonschema
jsonschema -i data/templates/references.json data/schemas/references.json
```

_pleiades_ingest_ is the work of [Tom Elliott](https://paregorios.org/about/) (tom.elliott@nyu.edu). Copyright (c) 2019 New York University. See LICENSE.txt file for complete rights information.


