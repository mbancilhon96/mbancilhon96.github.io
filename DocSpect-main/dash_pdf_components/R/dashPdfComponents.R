# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashPdfComponents <- function(id=NULL, apiKey=NULL, currPdf=NULL, documentTable=NULL, key=NULL, label=NULL, pdfRendered=NULL, showImpact=NULL, toggle=NULL) {
    
    props <- list(id=id, apiKey=apiKey, currPdf=currPdf, documentTable=documentTable, key=key, label=label, pdfRendered=pdfRendered, showImpact=showImpact, toggle=toggle)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashPdfComponents',
        namespace = 'dash_pdf_components',
        propNames = c('id', 'apiKey', 'currPdf', 'documentTable', 'key', 'label', 'pdfRendered', 'showImpact', 'toggle'),
        package = 'dashPdfComponents'
        )

    structure(component, class = c('dash_component', 'list'))
}
