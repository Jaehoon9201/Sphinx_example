"""
    my config
    ~~~~~~~~~
"""


def cfg_from_file(filename):
    """
    Load a config file and merge it into the default options.
    """
    import yaml
    with open(filename, 'r') as f:
        yaml_cfg = edict(yaml.load(f))
        # IF ERROR, CHANGE ABOVE LINE TO "yaml_cfg = edict(yaml.safe_load(f))"

    _merge_a_into_b(yaml_cfg, __C)


def def_tester2(filename):
    """
    Load a config file and merge it into the default options.
    """
    import yaml
    with open(filename, 'r') as f:
        yaml_cfg = edict(yaml.load(f))
        # IF ERROR, CHANGE ABOVE LINE TO "yaml_cfg = edict(yaml.safe_load(f))"

    _merge_a_into_b(yaml_cfg, __C)
