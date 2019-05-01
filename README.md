# pleiades_ingest

Specifications, tools, and tests for ingesting external data into [the _Pleiades_ gazetteer of ancient places](https://pleiades.stoa.org).

Specifications, documentation, and example files are kept in ```data/templates```. There are three files for each type of ingest file _Pleiades_ is prepared to support. We'll use "references" as an example:

 - ```references.md``` introduces the basic file structure etc. and tells you where to find the rest of its documentation
 - ```references.hjson``` provides the actual specification itself using [the hjson format](http://hjson.org) because it supports inline comments
 - ```references.json``` is an example file, generated from the hjson spec

_pleiades_ingest_ is the work of [Tom Elliott](https://paregorios.org/about/) (tom.elliott@nyu.edu). Copyright (c) 2019 New York University. See LICENSE.txt file for complete rights information.


