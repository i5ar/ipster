import os
import json
# from pprint import pprint
import powerline


# import pip
# repository_root = pip.main(['show', 'powerline-status'])
repository_root = os.path.dirname(os.path.dirname(powerline.__file__))
config_files = os.path.join(
    os.path.join(repository_root, 'powerline'), 'config_files')
config_file = os.path.join(config_files, 'config.json')

with open(config_file, "r+") as f:
    data = json.load(f)

    data_ipython = data['ext']['ipython']
    # pprint(data_ipython)

    # Edit configuration for IPython
    data_ipython['colorscheme'] = 'solarized'
    data_ipython['local_themes']['out'] = 'out_agnoster'
    data_ipython['theme'] = 'in_agnoster'
    # pprint(data_ipython)

    # Assign data
    data['common']['term_truecolor'] = True
    data['ext']['ipython'] = data_ipython
    # pprint(json.dumps(data))

    # Write data
    f.seek(0)
    f.write(json.dumps(data, indent=4, sort_keys=True))
    f.truncate()
