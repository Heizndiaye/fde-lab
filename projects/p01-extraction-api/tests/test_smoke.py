import extraction_api


def test_package_exposes_version() -> None:
    assert isinstance(extraction_api.__version__, str)
