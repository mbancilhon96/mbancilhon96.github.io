# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashPdfComponents(Component):
    """A DashPdfComponents component.
PDF component using the Adobe Embed API. 
Takes file url location and json annotations.

Keyword arguments:

- id (string; default ""):
    The ID used to identify this component in Dash callbacks.

- apiKey (string; default ""):
    Api key for authentication.

- currPdf (string; optional):
    URL to file that will be displayed.

- documentTable (list; optional):
    Annotations that will appear as highlights.

- key (string; optional):
    The ID used to identify this component in Dash callbacks.

- label (string; default ""):
    A label that will be printed when this component is rendered.

- pdfRendered (string; default ""):
    URL to file that will be displayed.

- showImpact (boolean; optional)

- toggle (boolean; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_pdf_components'
    _type = 'DashPdfComponents'
    @_explicitize_args
    def __init__(self, key=Component.UNDEFINED, id=Component.UNDEFINED, label=Component.UNDEFINED, apiKey=Component.UNDEFINED, pdfRendered=Component.UNDEFINED, currPdf=Component.UNDEFINED, documentTable=Component.UNDEFINED, toggle=Component.UNDEFINED, showImpact=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'apiKey', 'currPdf', 'documentTable', 'key', 'label', 'pdfRendered', 'showImpact', 'toggle']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'apiKey', 'currPdf', 'documentTable', 'key', 'label', 'pdfRendered', 'showImpact', 'toggle']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(DashPdfComponents, self).__init__(**args)
