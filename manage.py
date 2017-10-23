#!/usr/bin/env python
import os
from aldryn_django import startup


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    startup.manage(path=os.path.dirname(os.path.abspath(__file__)))
