# -*- coding: utf-8 -*-

"""
Created on 2016-06-04
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

__version__ = "1.0.3"

from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_pdf')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_pdf.kotti_configure

        to enable the ``kotti_pdf`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_pdf'
    settings['kotti.alembic_dirs'] += ' kotti_pdf:alembic'
    settings['kotti.available_types'] += ' kotti_pdf.resources.PDF'
    settings['kotti.fanstatic.view_needed'] += (
        ' kotti_pdf.fanstatic.css_and_js'
    )


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_pdf:locale')
    config.add_static_view('static-kotti_pdf', 'kotti_pdf:static')

    config.scan(__name__)
