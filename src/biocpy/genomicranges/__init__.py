try:
    from genomicranges import GenomicRanges
except ImportError as e:
    msg = (
        "`BiocPy` requirements are not installed.\n\n"
        "`pip` install as follows:\n\n"
        '  pip install "BiocPy" --upgrade\n\n'
        "If you need to specifically install `genomicranges`\n\n"
        '  pip install "genomicranges" --upgrade'
    )
    raise ImportError(str(e) + "\n\n" + msg) from e


__author__ = "jkanche"
__copyright__ = "jkanche"
__license__ = "MIT"
