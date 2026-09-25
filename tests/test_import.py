def test_package_imports() -> None:
    """Checks the package is importable from the installed environment."""
    # With the src/ layout this only passes if uv installed the package into .venv
    import safetranslate

    assert safetranslate.__name__ == "safetranslate"
