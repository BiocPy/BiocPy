try:
    from singlecellexperiment import SingleCellExperiment
except ImportError as e:
    msg = (
        "`BiocPy` dependencies are not installed.\n\n"
        "`pip` install as follows:\n\n"
        "  pip install biocpy --upgrade\n\n"
        "If you need to specifically install `singlecellexperiment`\n\n"
        "  pip install singlecellexperiment --upgrade"
    )
    raise ImportError(str(e) + "\n\n" + msg) from e

__author__ = "jkanche"
__copyright__ = "jkanche"
__license__ = "MIT"
