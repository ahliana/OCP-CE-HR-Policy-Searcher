"""Shared test fixtures.

src/api/app.py loads the project .env at import time (override=True), so
a developer's real ADMIN_TOKEN would flip the admin gate on for every
API test and 401 all unauthenticated POSTs. Strip it by default; tests
that exercise the gate set their own token via monkeypatch.setenv.
"""

import pytest


@pytest.fixture(autouse=True)
def _no_ambient_admin_token(monkeypatch):
    monkeypatch.delenv("ADMIN_TOKEN", raising=False)
