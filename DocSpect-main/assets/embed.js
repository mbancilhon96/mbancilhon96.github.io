let API_KEY = '899d52477b7d4b589f808242e8d36cc3'; // testPDFhost key
let previewFilePromise;
// let pdf_url = "files/ElectricalServicesTest.pdf";
let pdf_url = directLinkFromDropboxLink("https://www.dropbox.com/s/z2cc6wqirocjn35/ElectricalServicesTest.pdf?dl=0")
let pdf_filename = "Electrical Maintenance Agreement";

/* Control the viewer customization.
 * It lists down all supported variables with default values.
 **/
let viewerConfig = {
    showAnnotationTools: true,
    enableFormFilling: false,
    showLeftHandPanel: true,
    showDownloadPDF: false,
    showPrintPDF: false,
    showPageControls: true,
    dockPageControls: false
    // defaultViewMode: "", /* Allowed possible values are "FIT_PAGE", "FIT_WIDTH" or "". */
};

/* Wait for Adobe Document Services PDF Embed API to be ready */
// document.addEventListener("adobe_dc_view_sdk.ready", function () {
//     /* Initialize the AdobeDC View object */
//     var adobeDCView = new AdobeDC.View({
//         clientId: API_KEY,
//         /* Pass the div id in which PDF should be rendered */
//         divId: "pdf-viewer",
//     });

//     /* Invoke the file preview API on Adobe DC View object */
//     previewFilePromise = adobeDCView.previewFile({
//         /* Pass information on how to access the file */
//         content: {
//             /* Location of file where it is hosted */
//             location: {
//                 url: pdf_url, 
//                 //"https://documentcloud.adobe.com/view-sdk-demo/PDFs/Bodea%20Brochure.pdf"
//             },
//         },
//         /* Pass meta data of file */
//         metaData: {
//             /* file name */
//             fileName: pdf_filename
//         }
//     }, viewerConfig);
// });

// Converts a standar Dropbox link to a direct download link
function directLinkFromDropboxLink(dropboxLink) {
    return dropboxLink.replace("www.dropbox.com", "dl.dropboxusercontent.com").replace("?dl=0", "");
}
 
// var scrollTopBtn = document.getElementById("scroll-to-top")
// if (scrollTopBtn){
//     scrollTopBtn.addEventListener('click', scrollToTop());
// }

function scrollToTop() {
    previewFilePromise.then(adobeViewer => {
        adobeViewer.getAPIs().then(apis => {
                apis.gotoLocation(1, 0, 0) //(<Page_Number>, <X_Coordinate>, <Y_Coordinate>)
                        .then(() => console.log("Success"))
                        .catch(error => console.log(error));
         });
    });
}

// window.addEventListener("load", function() {
// document.getElementById("scrollTopBtn").addEventListener('click', scrollToTop);
// });