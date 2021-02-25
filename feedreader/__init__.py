try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sherlock').version
except Exception as e:
    VERSION = 'unknown'