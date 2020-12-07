"""Ansible-lint version information."""

try:
    import pkg_resources
    __version__ = pkg_resources.get_distribution('ansible-lint').version
except (Exception, ImportError):
    __version__ = 'unknown'
