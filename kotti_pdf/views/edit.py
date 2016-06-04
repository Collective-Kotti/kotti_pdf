# -*- coding: utf-8 -*-

"""
Created on 2015-12-16
:author: Andreas Kaiser (disko@binary-punks.com)
"""
from pyramid.view import view_config

from kotti.views.edit.content import FileEditForm, FileAddForm

from kotti_pdf import _
from kotti_pdf.resources import PDF


@view_config(name=PDF.type_info.add_view,
             permission=PDF.type_info.add_permission,
             renderer='kotti:templates/edit/node.pt')
class PDFAddForm(FileAddForm):
    item_type = _(u"PDF")
    item_class = PDF


@view_config(name='edit', context=PDF, permission='edit',
             renderer='kotti:templates/edit/node.pt')
class PDFEditForm(FileEditForm):
    pass
