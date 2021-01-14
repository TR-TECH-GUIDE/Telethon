from .client.telegramclient import TelegramClient
from .network import connection
from .tl import types, functions
from . import version, events, utils, errors
# It is important that this is after the utils import to avoid circular imports (#1669).
from .tl import custom
from .tl.custom import Button

__version__ = version.__version__

__all__ = [
    'TelegramClient', 'Button',
    'types', 'functions', 'custom', 'errors',
    'events', 'utils', 'connection'
]
