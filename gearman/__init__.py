"""
Gearman API - Client, worker, and admin client interfaces
"""

__version__ = '3.0.0'

from .admin_client import GearmanAdminClient
from .client import GearmanClient
from .worker import GearmanWorker

from .connection_manager import DataEncoder
from .constants import PRIORITY_NONE, PRIORITY_LOW, PRIORITY_HIGH, JOB_PENDING, JOB_CREATED, JOB_FAILED, JOB_COMPLETE

import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass

gearman_root_logger = logging.getLogger('gearman')
gearman_root_logger.addHandler(NullHandler())
