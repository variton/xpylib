
import pytest

from cli.clihdr import runc 
from fs.fsmgr import FsMgr 

@pytest.fixture(name="_path_decoy")
def childhr_fixture():
    """Get the absolute path to the decoy file."""
    return FsMgr.get_absolute_path_name("decoy.json")+"/decoy.json"

def test_run_str_cmd(_path_decoy):
    res = runc('cat {}'.format(_path_decoy))
    assert res['spectrum'] == 'blue'

def test_run_str_with_embedded_str(_path_decoy):
    res = runc('cat "{}"'.format(_path_decoy))
    assert res['spectrum'] == 'blue'

def test_run_list_str(_path_decoy):
    list_cmd = ['cat',_path_decoy]
    res = runc(list_cmd)
    assert res['spectrum'] == 'blue'
