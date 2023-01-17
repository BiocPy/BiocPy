# BiocPy

Installs all [BiocPy](https://github.com/BiocPy) packages. The package itself does not provide any functionality on its own. It provides an 

- easier way to install all ***core*** packages
- an interface to access the base data representations or classes

## Install

Package is published to [PyPI](https://pypi.org/project/biocpy/)

```shell
pip install biocpy
```

## Usage

To import any of the data classes, 

```python
from biocpy.genomicranges import GenomicRanges
from biocpy.summarizedexperiment import SummarizedExperiment
from biocpy.singlecellexperiment import SingleCellExperiment 
from biocpy.multiassayexperiment import MultiAssayExperiment

gr = GenomicRange(...)
se = SummarizedExperiment(...)
sce = SingleCellExperiment(...)
mae = MultiAssayExperiment(...)
```

For more use cases, checkout the [documentation](https://biocpy.github.io/BiocPy/).


<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.1.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
