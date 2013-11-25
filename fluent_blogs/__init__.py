# following PEP 386
__version__ = "0.9.7"

# Fix for internal messy imports.
# When base_models is imported before models/__init__.py runs, there is a circular import:
# base_models -> models/managers.py -> invoking models/__init__.py -> models/db.py -> base_models.py
#
# This doesn't occur when the models are imported first.
