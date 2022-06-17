try:
    from multiassayexperiment import MultiAssayExperiment
except ImportError as e:
    msg = (
        "`BiocPy` requirements are not installed.\n\n"
        "`pip` install as follows:\n\n"
        '  pip install "BiocPy" --upgrade\n\n'
        "If you need to specifically install `multiassayexperiment`\n\n"
        '  pip install "multiassayexperiment" --upgrade'
    )
    raise ImportError(str(e) + "\n\n" + msg) from e

__author__ = "jkanche"
__copyright__ = "jkanche"
__license__ = "MIT"
