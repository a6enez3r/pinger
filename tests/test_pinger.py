"""
test_pinger.py: test pinger code
"""
from pinger import __version__


def test_version():
    """
    Test module version is set from git
    """
    assert __version__ is not None
