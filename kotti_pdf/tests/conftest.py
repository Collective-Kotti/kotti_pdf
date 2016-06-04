# -*- coding: utf-8 -*-

"""
Created on 2016-06-04
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    import kotti_pdf.resources
    kotti_pdf.resources  # make pyflakes happy
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_pdf.kotti_configure'}
