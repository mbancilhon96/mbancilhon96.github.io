# AUTO GENERATED FILE - DO NOT EDIT

export dashpdfcomponents

"""
    dashpdfcomponents(;kwargs...)

A DashPdfComponents component.
PDF component using the Adobe Embed API. 
Takes file url location and json annotations.
Keyword arguments:
- `id` (String; optional): The ID used to identify this component in Dash callbacks.
- `apiKey` (String; optional): Api key for authentication
- `currPdf` (String; optional): URL to file that will be displayed
- `documentTable` (Array; optional): Annotations that will appear as highlights
- `key` (String; optional): The ID used to identify this component in Dash callbacks.
- `label` (String; optional): A label that will be printed when this component is rendered.
- `pdfRendered` (String; optional): URL to file that will be displayed
- `showImpact` (Bool; optional)
- `toggle` (Bool; optional)
"""
function dashpdfcomponents(; kwargs...)
        available_props = Symbol[:id, :apiKey, :currPdf, :documentTable, :key, :label, :pdfRendered, :showImpact, :toggle]
        wild_props = Symbol[]
        return Component("dashpdfcomponents", "DashPdfComponents", "dash_pdf_components", available_props, wild_props; kwargs...)
end

