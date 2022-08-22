![](https://img.shields.io/badge/Status:-RELEASED-green)

## Web Application Node Type (Abstract)

Abstract node type representing a web application.

| Name | URI | Version | Derived From |
|:---- |:--- |:------- |:------------ |
| `WebApplication` | `radon.nodes.abstract.WebApplication` | 1.0.0 | `tosca.nodes.WebApplication` |

### Properties

| Name | Required | Type | Constraint | Default Value | Description |
|:---- |:-------- |:---- |:---------- |:------------- |:----------- |
| `name` | `false` | `string` |   |   | Name of the web application |
| `granularity` | `false` | `string` | `valid_values: [monolithic, coarse-grained, fine-grained]` |   | Decomposition granularity |
| `word_embedding` | `false` | `string` | `valid_values: [esa, word2vec, glove, fasttext]` |   | Word embedding |
| `similarity_tradeoff` | `false` | `float` | `greater_or_equal: 0.0`, `less_or_equal: 1.0` |   | Similarity trade-off |
| `clustering_algorithm` | `false` | `string` | `valid_values: [hierarchical, kmedoids, dbscan, spectral]` |   | Clustering algorithm |
| `clustering_parameters` | `false` | `map: string` |   |   | Map of clustering parameters |
| `validity_index` | `false` | `string` | `valid_values: [gamma, silhouette]` |   | Validity index |
| `dependence_proportion` | `false` | `float` | `greater_or_equal: 0.5`, `less_or_equal: 1.0` |   | Dependence proportion |
| `entries` | `false` | `map: radon.datatypes.Entry` |   |   | Map of entries |
| `core_elements` | `false` | `list: string` |   |   | List of core elements |

\* The following table summarizes valid settings for the clustering properties of a `WebApplication`.

| Clustering Algorithm | Clustering Parameters:<br>&bull; Key Name | <br>&bull; Default Value<sup>[1](#fn1)</sup> | <br>&bull; Description |
|:-------------------- |:----------------------------------------- |:-------------------------------------------- |:---------------------- |
| `hierarchical` | `linkage`<br>`K` | &ndash;<br>&ndash; | Definition of the inter-cluster distance<br>Number of clusters to discover |
| `kmedoids` | `K`<br>`R` | &ndash;<br>&ndash; | Number of clusters to discover<br>Number of times to repeat the clustering |
| `dbscan` | `epsilon`<br>`m` | &ndash;<br>1 | Neighborhood of a data point<br>Minimum neighbors of a core point |
| `spectral` | `K`<br>`sigma`<br>`R` | &ndash;<br>0.6006<br>&ndash; | Number of clusters to discover<br>Scaling factor of the Gaussian kernel<br>Number of times to repeat the clustering |

<sup id="fn1">1</sup> If not explicitly specified, parameters without a default value are automatically determined by optimizing the validity index.

### Requirements

| Name | Capability Type | Node Type Constraint | Relationship Type | Occurrences |
|:---- |:--------------- |:-------------------- |:----------------- |:------------|
| `host` | `tosca.capabilities.Compute` | `radon.nodes.abstract.WebServer` | `tosca.relationships.HostedOn` | [1, 1] |
