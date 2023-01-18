webpackHotUpdatedash_pdf_components("main",{

/***/ "./src/lib/components/DashPdfComponents.react.js":
/*!*******************************************************!*\
  !*** ./src/lib/components/DashPdfComponents.react.js ***!
  \*******************************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "default", function() { return DashPdfComponents; });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _ViewSDKClient__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../ViewSDKClient */ "./src/lib/ViewSDKClient.js");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! prop-types */ "./node_modules/prop-types/index.js");
/* harmony import */ var prop_types__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(prop_types__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _CustomPdfActions__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../CustomPdfActions */ "./src/lib/CustomPdfActions.js");
/* harmony import */ var _SidebarTable__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../SidebarTable */ "./src/lib/SidebarTable.js");
/* harmony import */ var _adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @adobe/react-spectrum */ "./node_modules/@adobe/react-spectrum/dist/module.js");
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); Object.defineProperty(subClass, "prototype", { writable: false }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf ? Object.setPrototypeOf.bind() : function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } else if (call !== void 0) { throw new TypeError("Derived constructors may only return object or undefined"); } return _assertThisInitialized(self); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Boolean.prototype.valueOf.call(Reflect.construct(Boolean, [], function () {})); return true; } catch (e) { return false; } }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf.bind() : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }



 // import "../appStyle.css";




/**
 * PDF component using the Adobe Embed API. 
 * Takes file url location and json annotations.
 */

var DashPdfComponents = /*#__PURE__*/function (_Component) {
  _inherits(DashPdfComponents, _Component);

  var _super = _createSuper(DashPdfComponents);

  function DashPdfComponents() {
    var _this;

    _classCallCheck(this, DashPdfComponents);

    _this = _super.call(this);

    _defineProperty(_assertThisInitialized(_this), "viewerConfig", {
      /* Enable commenting APIs */
      enableAnnotationAPIs: true,

      /* Default value is false */
      // includePDFAnnotations: true, // If true, annotations are saved to PDF buffer
      embedMode: "FULL_WINDOW"
    });

    _defineProperty(_assertThisInitialized(_this), "setAnnotationManager", function (annotManager) {
      _this.setState({
        annotationManager: annotManager
      });
    });

    _defineProperty(_assertThisInitialized(_this), "loadPdf", function () {
      if (_this.props.pdfRendered == "") {
        console.log("empty load" + _this.props.pdfRendered);
        return;
      } ////// load the embed API script
      // const url = "https://documentcloud.adobe.com/view-sdk/main.js";
      // const script = document.createElement("script");
      // script.src = url;
      // script.async = true;
      // document.body.appendChild(script);


      var fileUrl = _this.state.documentTable[_this.props.pdfRendered].fileUrl;
      var fileName = _this.state.documentTable[_this.props.pdfRendered].fileName;
      var fileId = _this.props.pdfRendered;
      var highlightsArr = _this.state.documentTable[_this.props.pdfRendered].highlightsArr;
      var viewSDKClient = new _ViewSDKClient__WEBPACK_IMPORTED_MODULE_1__["default"]();
      _this.state.viewSDKClient = viewSDKClient;
      viewSDKClient.ready().then(function () {
        /* Invoke the file preview and get the Promise object */
        _this.state.previewFilePromise = viewSDKClient.previewFile(_this.props.id, _this.viewerConfig, _this.props.apiKey, fileUrl, fileName, fileId);
        /* Use the annotation manager interface to invoke the commenting APIs */

        _this.state.previewFilePromise.then(function (adobeViewer) {
          adobeViewer.getAPIs().then(function (apis) {
            viewSDKClient.registerEventsHandler(apis);
          });
          adobeViewer.getAnnotationManager().then(function (annotManager) {
            _this.setAnnotationManager(annotManager);

            if (highlightsArr.length != 0) {
              console.log("adding annotations");
              annotManager.addAnnotations(highlightsArr) // annotManager.addAnnotationsInPDF(highlightsArr)            
              .then(function (result) {
                console.log("Success!! Annotations added", result);
              })["catch"](function (error) {
                console.log(error);
              });
            }
            /* Set UI configurations */


            var customFlags = {
              showToolbar: false,

              /* Default value is true */
              showCommentsPanel: false,

              /* Default value is true */
              downloadWithAnnotations: true,

              /* Default value is false */
              printWithAnnotations: true
              /* Default value is false */

            };

            _this.state.annotationManager.setConfig(customFlags);
          });
        });
      });
      console.log("Loading: " + _this.props.pdfRendered);
    });

    _defineProperty(_assertThisInitialized(_this), "updateAnnotationReview", function (id, status) {
      var newDict = Object.assign({}, _this.state.highlightsDict);
      newDict[id].isReviewed = true;
      newDict[id].isCorrect = status;

      _this.setState({
        highlightsDict: newDict
      }); // TODO call docTable function instead


      _this.state.documentTable[_this.props.pdfRendered].highlightsArr[0].creator.isCorrect = status;
      _this.state.documentTable[_this.props.pdfRendered].highlightsArr[0].creator.isReviewed = true;
    });

    _defineProperty(_assertThisInitialized(_this), "addAnnotation", function (newArr) {// Add annotation 
      // index annot of pdfRendered 
      // add to document table
    });

    _defineProperty(_assertThisInitialized(_this), "updatePdfRendered", function (id) {
      _this.props.setProps({
        pdfRendered: id,
        key: id
      });

      _this.loadPdf();
    });

    _defineProperty(_assertThisInitialized(_this), "setIsOpen", function () {});

    _this.state = {
      annotationManager: undefined,
      documentTable: undefined,
      highlightsDict: undefined,
      selectedText: "",
      drawerOpen: false,
      pdfRendered: ""
    };
    return _this;
  }

  _createClass(DashPdfComponents, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      this.loadPdf();
    }
  }, {
    key: "render",
    value: function render() {
      var _this$props = this.props,
          key = _this$props.key,
          id = _this$props.id,
          label = _this$props.label,
          apiKey = _this$props.apiKey,
          pdfRendered = _this$props.pdfRendered,
          documentTable = _this$props.documentTable; // console.log(this.props.pdfRendered);
      // console.log(documentTable[0].contractId);
      // console.log(documentTable[1].data);

      var dict = {};
      documentTable.forEach(function (element) {
        return dict[element.contractId] = element.data;
      });
      this.state.documentTable = dict;

      if (this.props.pdfRendered != "") {
        // Create a dictionary mapping each unique annotation id to category and name
        var highlightsDict = {};
        var highlightsArr = this.state.documentTable[this.props.pdfRendered].highlightsArr;
        highlightsArr.forEach(function (element) {
          return highlightsDict[element.id] = element.creator;
        });
        this.state.highlightsDict = highlightsDict;
      }

      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_5__["Provider"], {
        theme: _adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_5__["defaultTheme"]
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "pdf-view-container"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_SidebarTable__WEBPACK_IMPORTED_MODULE_4__["default"], {
        width: "size-800",
        documentTable: this.state.documentTable,
        updatePdfRendered: this.updatePdfRendered
      }), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        id: id,
        className: "pdf-view full-window-div"
      }), this.state.annotationManager && /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_CustomPdfActions__WEBPACK_IMPORTED_MODULE_3__["default"], {
        annotationManager: this.state.annotationManager,
        highlightsDict: this.state.highlightsDict,
        viewSDKClient: this.state.viewSDKClient,
        updateAnnotationReview: this.updateAnnotationReview,
        addAnnotation: this.addAnnotation
      })));
    }
  }]);

  return DashPdfComponents;
}(react__WEBPACK_IMPORTED_MODULE_0__["Component"]);


DashPdfComponents.defaultProps = {
  id: "",
  label: "",
  apiKey: "",
  pdfRendered: ""
};
DashPdfComponents.propTypes = {
  /**
   * The ID used to identify this component in Dash callbacks.
   */
  key: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * The ID used to identify this component in Dash callbacks.
   */
  id: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * A label that will be printed when this component is rendered.
   */
  label: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * Api key for authentication
   */
  apiKey: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * URL to file that will be displayed
   */
  pdfRendered: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * URL to file that will be displayed
   */
  currPdf: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * Annotations that will appear as highlights
   */
  documentTable: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.array,

  /**
   * Dash-assigned callback that should be called to report property changes
   * to Dash, to make them available for callbacks.
   */
  setProps: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.func
};

/***/ })

})
//# sourceMappingURL=3db4f6a-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiIzZGI0ZjZhLW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==