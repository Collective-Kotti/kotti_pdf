# -*- coding: utf-8 -*-

"""
Created on 2015-12-16
:author: Andreas Kaiser (disko@binary-punks.com)
"""

# import PIL
# import rfc6266
from unidecode import unidecode

from kotti.util import extract_from_settings
from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_pdf.interfaces import IPDF


@view_defaults(context=IPDF, permission='view')
class PDFView(object):
    """The PDFView class is registered for the :class:`IPDF` context."""

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(name='view',
                 renderer='kotti_pdf:templates/pdf.pt')
    def view(self):
        """
        :result: Empty dictionary to be handed to the pdf.pt template for
                 rendering.
        :rtype: dict
        """
        return {}

    @view_config(name="pdf")
    def pdf(self, subpath=None):
        """Return the pdf in a specific scale, either inline
        (default) or as attachment.
        :param subpath: [download] (optional).
                        When 'download' is the last element in subpath.
        :type subpath: str
        :result: complete response object
        :rtype: pyramid.response.Response
        """

        if subpath is None:
            subpath = self.request.subpath

        width, height = (None, None)
        subpath = list(subpath)

        if (len(subpath) > 0) and (subpath[-1] == "download"):
            disposition = "attachment"
            subpath.pop()
        else:
            disposition = "inline"

        if not (width and height):
            return self.request.uploaded_file_response(
                self.context.data, disposition)

        pdf = self.context.data.file.read()
        res = Response(
            headerlist=[
                ('Content-Disposition', '{0};filename="{1}"'.format(
                    disposition,
                    self.context.filename.encode('ascii', 'ignore'))),
                ('Content-Length', str(len(pdf))),
                ('Content-Type', str(self.context.mimetype)),
            ],
            body=pdf,
        )
        # res.content_disposition = rfc6266.build_header(
        #     self.context.filename, disposition=disposition,
        #     filename_compat=unidecode(self.context.filename))
        return res
