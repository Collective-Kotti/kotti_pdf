# -*- coding: utf-8 -*-

"""
Created on 2015-12-16
:author: Andreas Kaiser (disko@binary-punks.com)
"""
# from depot.fields.filters.thumbnails import WithThumbnailFilter
from kotti.resources import Content
from kotti.resources import File
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declared_attr
from zope.interface import implementer

from kotti_pdf import _
from kotti_pdf.interfaces import IPDF


@implementer(IPDF)
class PDF(File):
    """PDF is a specialized version of :class:`~kotti.resources.File`, that
    adds thumbnails and has different views.
    """

    #: Primary key column in the DB
    id = Column(Integer(), ForeignKey('files.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'PDF',
        title=_(u'PDF'),
        add_view=u'add_pdf',
        addable_to=[u'Document'],
        selectable_default_views=[],
        uploadable_mimetypes=['application/pdf'],
        )
