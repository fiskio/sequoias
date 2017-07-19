# just a test to check that all is OK
import cntk as C


def test_cntk_ok():
    print('CNTK version: %s' % C.__version__)
    assert C.__version__ == '2.0'
