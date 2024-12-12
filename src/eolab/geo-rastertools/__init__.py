# -*- coding: utf-8 -*-
"""This module contains the eolab's geo-rastertools CLI and API
"""
from importlib.metadata import version

# Change here if project is renamed and does not equal the package name
dist_name = "geo-rastertools"
__version__ = version(dist_name)

from eolab.geo-rastertools.rastertools import RastertoolConfigurationException
from eolab.geo-rastertools.rastertools import Rastertool, Windowable
# import rastertool Filtering
from eolab.geo-rastertools.filtering import Filtering
# import rastertool Hillshade
from eolab.geo-rastertools.hillshade import Hillshade
# import rastertool Radioindice
from eolab.geo-rastertools.radioindice import Radioindice
# import rastertool Speed
from eolab.geo-rastertools.speed import Speed
# import rastertool SVF
from eolab.geo-rastertools.svf import SVF
# import rastertool Tiling
from eolab.geo-rastertools.tiling import Tiling
# import rastertool Timeseries
from eolab.geo-rastertools.timeseries import Timeseries
# import rastertool Zonalstats
from eolab.geo-rastertools.zonalstats import Zonalstats
# import the method to run a rastertool
from eolab.geo-rastertools.main import rastertools, add_custom_rastertypes

__all__ = [
    "RastertoolConfigurationException", "Rastertool", "Windowable",
    "Filtering", "Hillshade", "Radioindice", "Speed", "SVF", "Tiling",
    "Timeseries", "Zonalstats",
    "run_tool", "add_custom_rastertypes"
]
