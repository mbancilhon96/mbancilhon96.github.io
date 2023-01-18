webpackHotUpdatedash_pdf_components("main",{

/***/ "./node_modules/css-loader/dist/cjs.js!./src/lib/appStyle.css":
/*!********************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./src/lib/appStyle.css ***!
  \********************************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.i, ".category-badge.badge {\n    font-size: 18px;\n    width: 100%;\n}\n\n.pdf-view-container {\n    width: 100vw;\n    height: 100vh;\n    display: flex;\n}\n\n.pdf-view {\n    width: calc(100% - 400px);\n}\n\n.annotations-container {\n    border-left: 1px solid #e2e2e2;\n    width: 400px;\n}\n\nul {\n    margin: 0 5px;\n    padding: 0;\n}\n\nli * {\n    float: left;\n}\n\nli, h3 {\n    clear: both;\n    list-style: none;\n}\n\ninput, button {\n    outline: none;\n}\n\nbutton {\n    background: none;\n    border: 0px;\n    color: #888;\n    font-size: 15px;\n    width: 60px;\n    margin: 10px 0 0;\n    font-family: Lato, sans-serif;\n    cursor: pointer;\n}\n\nbutton:hover {\n    color: #333;\n}\n\n/* Heading */\n/* h3 {\n    color: #333;\n    font-weight: 700;\n    font-size: 15px;\n    border-bottom: 1px solid #333;\n    padding: 15px 0 14px;\n    margin: 0;\n    text-align: center;\n} */\n\ninput[type=\"text\"] {\n    margin: 0;\n    font-size: 18px;\n    line-height: 18px;\n    height: 18px;\n    padding: 10px;\n    border: 1px solid #ddd;\n    background: #fff;\n    border-radius: 6px;\n    font-family: Lato, sans-serif;\n    color: #888;\n}\n\ninput[type=\"text\"]:focus {\n    color: #333;\n}\n\n/* Annotation list */\nli {\n    overflow: hidden;\n    margin: 5px 0;\n    padding: 10px 0;\n    width: auto;\n    border: 2px solid #3D85B0;\n}\n\nli > input[type=\"checkbox\"] {\n    margin: 0 10px;\n    position: relative;\n    top: 15px;\n}\n\nli > label {\n    font-size: 18px;\n    /* line-height: 40px; */\n    width: 237px;\n    padding: 0 0 0 11px;\n}\n\nli > input[type=\"text\"] {\n    width: 226px;\n}\n\nli > .delete:hover {\n    color: #CF2323;\n}\n\n.selected {\n    border: 2px solid #3D85B0;\n}\n\n.unselected {\n    border: 2px solid #eee;\n}\n", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./src/lib/style.css":
false,

/***/ "./node_modules/css-loader/dist/runtime/api.js":
/*!*****************************************************!*\
  !*** ./node_modules/css-loader/dist/runtime/api.js ***!
  \*****************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/*
  MIT License http://www.opensource.org/licenses/mit-license.php
  Author Tobias Koppers @sokra
*/
// css base code, injected by the css-loader
// eslint-disable-next-line func-names
module.exports = function (useSourceMap) {
  var list = []; // return the list of modules as css string

  list.toString = function toString() {
    return this.map(function (item) {
      var content = cssWithMappingToString(item, useSourceMap);

      if (item[2]) {
        return "@media ".concat(item[2], " {").concat(content, "}");
      }

      return content;
    }).join('');
  }; // import a list of modules into the list
  // eslint-disable-next-line func-names


  list.i = function (modules, mediaQuery, dedupe) {
    if (typeof modules === 'string') {
      // eslint-disable-next-line no-param-reassign
      modules = [[null, modules, '']];
    }

    var alreadyImportedModules = {};

    if (dedupe) {
      for (var i = 0; i < this.length; i++) {
        // eslint-disable-next-line prefer-destructuring
        var id = this[i][0];

        if (id != null) {
          alreadyImportedModules[id] = true;
        }
      }
    }

    for (var _i = 0; _i < modules.length; _i++) {
      var item = [].concat(modules[_i]);

      if (dedupe && alreadyImportedModules[item[0]]) {
        // eslint-disable-next-line no-continue
        continue;
      }

      if (mediaQuery) {
        if (!item[2]) {
          item[2] = mediaQuery;
        } else {
          item[2] = "".concat(mediaQuery, " and ").concat(item[2]);
        }
      }

      list.push(item);
    }
  };

  return list;
};

function cssWithMappingToString(item, useSourceMap) {
  var content = item[1] || ''; // eslint-disable-next-line prefer-destructuring

  var cssMapping = item[3];

  if (!cssMapping) {
    return content;
  }

  if (useSourceMap && typeof btoa === 'function') {
    var sourceMapping = toComment(cssMapping);
    var sourceURLs = cssMapping.sources.map(function (source) {
      return "/*# sourceURL=".concat(cssMapping.sourceRoot || '').concat(source, " */");
    });
    return [content].concat(sourceURLs).concat([sourceMapping]).join('\n');
  }

  return [content].join('\n');
} // Adapted from convert-source-map (MIT)


function toComment(sourceMap) {
  // eslint-disable-next-line no-undef
  var base64 = btoa(unescape(encodeURIComponent(JSON.stringify(sourceMap))));
  var data = "sourceMappingURL=data:application/json;charset=utf-8;base64,".concat(base64);
  return "/*# ".concat(data, " */");
}

/***/ }),

/***/ "./src/lib/appStyle.css":
/*!******************************!*\
  !*** ./src/lib/appStyle.css ***!
  \******************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {


var content = __webpack_require__(/*! !../../node_modules/css-loader/dist/cjs.js!./appStyle.css */ "./node_modules/css-loader/dist/cjs.js!./src/lib/appStyle.css");

if(typeof content === 'string') content = [[module.i, content, '']];

var transform;
var insertInto;



var options = {"insertAt":"top","hmr":true}

options.transform = transform
options.insertInto = undefined;

var update = __webpack_require__(/*! ../../node_modules/style-loader/lib/addStyles.js */ "./node_modules/style-loader/lib/addStyles.js")(content, options);

if(content.locals) module.exports = content.locals;

if(true) {
	module.hot.accept(/*! !../../node_modules/css-loader/dist/cjs.js!./appStyle.css */ "./node_modules/css-loader/dist/cjs.js!./src/lib/appStyle.css", function() {
		var newContent = __webpack_require__(/*! !../../node_modules/css-loader/dist/cjs.js!./appStyle.css */ "./node_modules/css-loader/dist/cjs.js!./src/lib/appStyle.css");

		if(typeof newContent === 'string') newContent = [[module.i, newContent, '']];

		var locals = (function(a, b) {
			var key, idx = 0;

			for(key in a) {
				if(!b || a[key] !== b[key]) return false;
				idx++;
			}

			for(key in b) idx--;

			return idx === 0;
		}(content.locals, newContent.locals));

		if(!locals) throw new Error('Aborting CSS HMR due to changed css-modules locals.');

		update(newContent);
	});

	module.hot.dispose(function() { update(); });
}

/***/ }),

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
/* harmony import */ var _appStyle_css__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../appStyle.css */ "./src/lib/appStyle.css");
/* harmony import */ var _appStyle_css__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_appStyle_css__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _CustomPdfActions__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../CustomPdfActions */ "./src/lib/CustomPdfActions.js");
/* harmony import */ var _annotationExample__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../annotationExample */ "./src/lib/annotationExample.js");
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







/**
 * PDF componetn using the Adobe Embed API. Takes file url location and json annotations.
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
      includePDFAnnotations: false // If true, annotations are saved to PDF buffer

    });

    _defineProperty(_assertThisInitialized(_this), "setAnnotationManager", function (annotManager) {
      _this.setState({
        annotationManager: annotManager
      });
    });

    _defineProperty(_assertThisInitialized(_this), "loadPdf", function () {
      ////// load the embed API script
      // const url = "https://documentcloud.adobe.com/view-sdk/main.js";
      // const script = document.createElement("script");
      // script.src = url;
      // script.async = true;
      // document.body.appendChild(script);
      var viewSDKClient = new _ViewSDKClient__WEBPACK_IMPORTED_MODULE_1__["default"]();
      viewSDKClient.ready().then(function () {
        /* Invoke the file preview and get the Promise object */
        _this.state.previewFilePromise = viewSDKClient.previewFile(_this.props.id, _this.viewerConfig, _this.props.apiKey, _this.props.fileUrl, _this.props.fileName, _this.props.fileId);
        /* Use the annotation manager interface to invoke the commenting APIs */

        _this.state.previewFilePromise.then(function (adobeViewer) {
          adobeViewer.getAnnotationManager().then(function (annotManager) {
            _this.setAnnotationManager(annotManager);

            if (_this.state.highlightsArr.length != 0) {
              annotManager.addAnnotations(_this.state.highlightsArr) // annotManager.addAnnotationsInPDF(this.state.highlightsArr)            
              .then(function (result) {
                console.log("Success!!! Annotations added", result);
              })["catch"](function (error) {
                console.log(error);
              });
            }
            /* Set UI configurations */


            var customFlags = {
              // showToolbar: false,   /* Default value is true */
              // dockPageControls: false, /* Default value is true */
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
    });

    _this.state = {
      annotationManager: undefined,
      fileUrl: "",
      highlightsArr: undefined
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
          fileUrl = _this$props.fileUrl,
          fileName = _this$props.fileName,
          fileId = _this$props.fileId,
          highlightsArr = _this$props.highlightsArr;
      this.state.fileUrl = fileUrl;
      this.state.highlightsArr = highlightsArr;
      return (
        /*#__PURE__*/
        // <Provider theme={defaultTheme} colorScheme="light">
        react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
          className: "pdf-view-container"
        }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
          id: id,
          className: "pdf-view full-window-div"
        }), this.state.annotationManager && /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_CustomPdfActions__WEBPACK_IMPORTED_MODULE_4__["default"], {
          annotationManager: this.state.annotationManager
        })) // </Provider>

      );
    } // render() {
    //     const {id, label, setProps, value} = this.props;
    //     return (
    //         <div id={id}>
    //             <div id="pdf-div" className="full-window-div">HI!</div> 
    //             <h1>HI!</h1>
    //             ExampleComponent: {label}&nbsp;
    //             <input
    //                 value={value}
    //                 onChange={
    //                     /*
    //                      * Send the new value to the parent component.
    //                      * setProps is a prop that is automatically supplied
    //                      * by dash's front-end ("dash-renderer").
    //                      * In a Dash app, this will update the component's
    //                      * props and send the data back to the Python Dash
    //                      * app server if a callback uses the modified prop as
    //                      * Input or State.
    //                      */
    //                     e => setProps({ value: e.target.value })
    //                 }
    //             />
    //         </div>
    //     );
    // }

  }]);

  return DashPdfComponents;
}(react__WEBPACK_IMPORTED_MODULE_0__["Component"]);


DashPdfComponents.defaultProps = {};
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
  fileUrl: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * file name
   */
  fileName: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
  * unique file id
  */
  fileId: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.string,

  /**
   * Annotations that will appear as highlights
   */
  highlightsArr: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.array,

  /**
   * Dash-assigned callback that should be called to report property changes
   * to Dash, to make them available for callbacks.
   */
  setProps: prop_types__WEBPACK_IMPORTED_MODULE_2___default.a.func
};

/***/ }),

/***/ "./src/lib/style.css":
false

})
//# sourceMappingURL=1f937fa-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiIxZjkzN2ZhLW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==