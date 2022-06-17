# BiocPy

Interface to all [BiocPy](https://github.com/BiocPy) Packages. The package itself does not provide any methods or functionality on its own. It provides an 

- easier way to install all the relevant packages
- an easier interface to access the base data representations or classes

## Install

Package is published to [PyPI](https://pypi.org/project/biocpy/)

```shell
pip install biocpy
```

## Usage

To import any of the classes

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

## Contents

* [Overview](readme)
* [License](license)
* [Authors](authors)
* [Changelog](changelog)
* [Module Reference](api/modules)


## Indices and tables

```eval_rst
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

[Sphinx]: http://www.sphinx-doc.org/
[Markdown]: https://daringfireball.net/projects/markdown/
[reStructuredText]: http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
[recommonmark]: https://recommonmark.readthedocs.io/en/latest
[autostructify]: https://recommonmark.readthedocs.io/en/latest/auto_structify.html
