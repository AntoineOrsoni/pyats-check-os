# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# ## Pre-setup

# %%
# import the aetest module
from pyats import aetest
import logging
from genie.testbed import load
import argparse
import sys
import pprint

# set debug level DEBUG, INFO, WARNING
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# set pprint
pp = pprint.PrettyPrinter(indent = 2)

# %% [markdown]
# ## Loading the testbed, connecting to the device

# %%
testbed = load('/home/anorsoni/Projets/2020-CAP-Altitude/pyats-check-os/testbed.yaml')

asr903_5 = testbed.devices["ASR903_5"]

asr903_5.connect(init_exec_commands=[],
                 init_config_commands=[],
                 log_stdout=False)


# %%
isis = asr903_5.parse('show isis neighbors')
pp.pprint(isis)

# %% [markdown]
# ## Setting the db

# %%



