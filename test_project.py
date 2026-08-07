import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
import github_desktop_for_linux_2306f as mod

def test_cli_runs():
    assert mod.cli([]) in (0, 1)
