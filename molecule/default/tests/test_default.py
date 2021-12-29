"""Role testing files using testinfra."""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import pytest


@pytest.mark.parametrize("directory", [
    "/srv/app01",
    "/srv/app02"
])
def test_directory_present(host, directory):
    """Test if directory is present."""
    item = host.file(directory)

    assert item.is_directory
