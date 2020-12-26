try:
    # working directory preference
    from __vars__ import __choice__
except ImportError:
    # library backup
    from test.__vars__ import __choice__

if __choice__ == 'this':
    from test.this import shared
elif __choice__ == 'that':
    from test.that import shared
else:
    raise ImportError(f'__vars__.__choice__ must be either "this" or "that" but was {__choice__}')

__all__ = ['shared']
