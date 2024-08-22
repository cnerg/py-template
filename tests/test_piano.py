import acme_corp

import pytest


@pytest.fixture
def blank_piano():
    return acme_corp.Piano()


def test_piano_init(blank_piano):
    assert blank_piano.weight == pytest.approx(1_000.0)
    assert blank_piano.height == pytest.approx(0.0)


def test_lifting_piano(blank_piano):
    blank_piano.lift()
    assert blank_piano.height == pytest.approx(3)


def test_dropping_piano(blank_piano):
    pass
