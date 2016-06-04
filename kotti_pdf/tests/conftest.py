# -*- coding: utf-8 -*-

"""
Created on 2016-06-04
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

from pytest import fixture
import kotti_pdf.resources


pytest_plugins = "kotti"


@fixture(scope='session')
def custom_settings():
    kotti_pdf.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_pdf.kotti_configure'}
