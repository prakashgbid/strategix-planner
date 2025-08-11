"""
smart-planner
================

A powerful Python package extracted from OSA.
"""

__version__ = "0.1.0"
__author__ = "OSA Contributors"

from .core import SmartPlanner
from .exceptions import SmartPlannerError

__all__ = [
    "SmartPlanner",
    "SmartPlannerError",
]
