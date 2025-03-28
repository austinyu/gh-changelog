


from gh_changelog.core import Version

def parse_version_str(version_str: str) -> Version:
    """
    Parse a version string into its components.

    Args:
        version_str (str): The version string to parse.

    Returns:
        tuple: A tuple containing the major, minor, and patch version.
    """
    numeric_start: int = 0
    while numeric_start < len(version_str) and not version_str[numeric_start].isdigit():
        numeric_start += 1
    numeric_end: int = len(version_str) - 1
    while numeric_end >= 0 and not version_str[numeric_end].isdigit():
        numeric_end -= 1
    version_str_num = version_str[numeric_start:numeric_end + 1]
    parts = version_str_num.split(".")
    if len(parts) > 3:
        raise ValueError(f"Version string {version_str} has too many components.")
    try:
        major = int(parts[0])
        minor = int(parts[1]) if len(parts) > 1 else 0
        patch = int(parts[2]) if len(parts) > 2 else 0
    except ValueError as e:
        raise ValueError(
            f"Version string {version_str} contains non-numeric components."
        ) from e
    return Version(major, minor, patch, version_str[numeric_end + 1 :].split("-"))
