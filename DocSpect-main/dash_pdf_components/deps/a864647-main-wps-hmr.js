webpackHotUpdatedash_pdf_components("main",{

/***/ "./src/lib/CustomPdfActions.js":
/*!*************************************!*\
  !*** ./src/lib/CustomPdfActions.js ***!
  \*************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-bootstrap/Accordion */ "./node_modules/react-bootstrap/esm/Accordion.js");
/* harmony import */ var react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-bootstrap/Row */ "./node_modules/react-bootstrap/esm/Row.js");
/* harmony import */ var react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-bootstrap/Col */ "./node_modules/react-bootstrap/esm/Col.js");
/* harmony import */ var react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-bootstrap/Badge */ "./node_modules/react-bootstrap/esm/Badge.js");
/* harmony import */ var _ClauseAnnotationItem__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./ClauseAnnotationItem */ "./src/lib/ClauseAnnotationItem.js");
/* harmony import */ var _EntityAnnotationItem__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./EntityAnnotationItem */ "./src/lib/EntityAnnotationItem.js");
/* harmony import */ var _AnnotationItem__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./AnnotationItem */ "./src/lib/AnnotationItem.js");
/* harmony import */ var _AnnotationModal__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./AnnotationModal */ "./src/lib/AnnotationModal.js");
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && iter[Symbol.iterator] != null || iter["@@iterator"] != null) return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

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

// From code in Adobe Embed API samples:
// https://github.com/adobe/pdf-embed-api-samples










var CustomPdfActions = /*#__PURE__*/function (_Component) {
  _inherits(CustomPdfActions, _Component);

  var _super = _createSuper(CustomPdfActions);

  function CustomPdfActions() {
    var _this;

    _classCallCheck(this, CustomPdfActions);

    for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    _this = _super.call.apply(_super, [this].concat(args));

    _defineProperty(_assertThisInitialized(_this), "state", {
      annotationListItems: [],
      selectedAnnotationId: undefined,
      annotationModalVisible: false,
      annotationCategory: "",
      annotationName: ""
    });

    _defineProperty(_assertThisInitialized(_this), "annotationEventListener", function (event) {
      if (event.type === "ANNOTATION_ADDED") {
        if (event.data.bodyValue) {
          _this.onAnnotationAdded(event.data);
        } else {
          _this.addAnnotationText(event.data);
        }
      }

      if (event.type === "ANNOTATION_DELETED") {
        _this.onAnnotationDeleted(event.data.id);
      }

      if (event.type === "ANNOTATION_SELECTED") {
        _this.toggleSelectedAnnotation(event.data.id);
      }

      if (event.type === "ANNOTATION_UNSELECTED") {
        _this.toggleSelectedAnnotation();
      }

      if (event.type === "ANNOTATION_UPDATED" && event.data.target.selector.subtype === "freetext") {
        _this.onTextAnnotationUpdated(event.data);
      }

      console.log(event);
    });

    _defineProperty(_assertThisInitialized(_this), "onAnnotationAdded", function (annotation) {
      _this.setState({
        annotationListItems: [].concat(_toConsumableArray(_this.state.annotationListItems), [annotation])
      });
    });

    _defineProperty(_assertThisInitialized(_this), "onAnnotationDeleted", function (id) {
      _this.setState({
        annotationListItems: _this.state.annotationListItems.filter(function (item) {
          return item.id !== id;
        })
      });
    });

    _defineProperty(_assertThisInitialized(_this), "toggleSelectedAnnotation", function (id) {
      _this.setState({
        selectedAnnotationId: id
      });
    });

    _defineProperty(_assertThisInitialized(_this), "onTextAnnotationUpdated", function (annotation) {
      console.log("onTextAnnotationUpdated");

      var index = _this.state.annotationListItems.findIndex(function (item) {
        return item.id === annotation.id;
      });

      _this.state.annotationListItems[index].bodyValue = annotation.bodyValue;

      _this.setState({
        annotationListItems: _this.state.annotationListItems
      });
    });

    _defineProperty(_assertThisInitialized(_this), "toggleAnnotationModal", function () {
      _this.setState(function (state) {
        return {
          annotationModalVisible: !state.annotationModalVisible
        };
      });
    });

    _defineProperty(_assertThisInitialized(_this), "onAnnotationModalExited", function () {
      console.log("EXIT onAnnotationModalExited");

      if (_this.state.annotationCategory != "") {
        _this.props.highlightsDict[_this.state.currentAnnotation.id] = {
          category: _this.state.annotationCategory
        };

        _this.updateAnnotationCategory("");
      }

      if (_this.state.annotationName != "") {
        _this.state.currentAnnotation.creator.name = _this.state.annotationName;
        _this.props.highlightsDict[_this.state.currentAnnotation.id].name = _this.state.annotationName;

        _this.updateAnnotationName("");
      }

      _this.props.annotationManager.updateAnnotation(_this.state.currentAnnotation).then(function () {
        console.log("Annotation updated successfully.");

        _this.onAnnotationAdded(_this.state.currentAnnotation);
      })["catch"](function (error) {
        console.log(error);
      });

      _this.toggleAnnotationModal();
    });

    _defineProperty(_assertThisInitialized(_this), "updateAnnotationCategory", function (value) {
      _this.setState(function (state) {
        return {
          annotationCategory: value
        };
      });
    });

    _defineProperty(_assertThisInitialized(_this), "updateAnnotationName", function (value) {
      _this.setState(function (state) {
        return {
          annotationName: value
        };
      });
    });

    _defineProperty(_assertThisInitialized(_this), "addAnnotationText", function (annotation) {
      console.log(" addAnnotationText");
      /* Get the annotation body value */

      annotation.bodyValue = _this.props.viewSDKClient.getSelectedText(); // console.log(annotation);

      _this.toggleAnnotationModal();

      _this.setState(function (state) {
        return {
          currentAnnotation: annotation
        };
      }); // const type = annotation.target.selector.subtype;
      // const comment = prompt("Enter the text associated with " + type, "Added a " + type) || "Added a " + type;
      // const comment = "Added a " + type;
      // annotation.bodyValue = comment;

    });

    return _this;
  }

  _createClass(CustomPdfActions, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      /* API to register events listener */
      this.props.annotationManager.registerEventListener(this.annotationEventListener);
    }
  }, {
    key: "render",
    value: function render() {
      var _this2 = this;

      // ”category": {clause} or {entity}
      // “name”: {clause type} or {entity type}
      var annotationEntityList = [];
      var annotationClasueList = [];
      var uncategorizedList = [];
      this.state.annotationListItems.forEach(function (element) {
        // console.log({ element });
        // console.log(this.props.highlightsDict[element.id].category)
        if (element.id in _this2.props.highlightsDict) {
          if (_this2.props.highlightsDict[element.id].category == "Clause") {
            annotationClasueList.push(element);
          } else if (_this2.props.highlightsDict[element.id].category == "Entity") {
            annotationEntityList.push(element);
          }
        } else {
          uncategorizedList.push(element);
        }
      });
      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "panel-container"
      }, this.state.annotationModalVisible && /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_AnnotationModal__WEBPACK_IMPORTED_MODULE_8__["default"], {
        show: this.state.annotationModalVisible,
        onExited: this.onAnnotationModalExited,
        categoryValue: this.state.annotationCategory,
        toggleCategory: this.updateAnnotationCategory,
        nameValue: this.state.annotationName,
        toggleName: this.updateAnnotationName
      }), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "panel-heading"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("h1", {
        className: "panel-heading"
      }, "Agreement Insights")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "panel-contents"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"], {
        defaultActiveKey: ['0'],
        alwaysOpen: true
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Item, {
        eventKey: "0"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Header, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("h2", {
        className: "accordion-header"
      }, "Key Entities")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Body, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("ul", {
        className: "annotations-container"
      }, // this.state.annotationListItems.map(listItem =>
      annotationEntityList.map(function (listItem) {
        return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_EntityAnnotationItem__WEBPACK_IMPORTED_MODULE_6__["default"], {
          key: listItem.id,
          annotation: listItem,
          selectedAnnotationId: _this2.state.selectedAnnotationId,
          annotationManager: _this2.props.annotationManager
        });
      }))))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"], {
        defaultActiveKey: ['1'],
        alwaysOpen: true
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Item, {
        eventKey: "1"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Header, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("h2", {
        className: "accordion-header"
      }, "Key Clauses")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Body, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_2__["default"], {
        className: "category-badge"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_4__["default"], {
        bg: "opt-out"
      }, "Opt-out"), ' '), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_4__["default"], {
        bg: "termination"
      }, "Termination"), ' '), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_4__["default"], {
        bg: "payment"
      }, "Payment"), ' ')), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("ul", {
        className: "annotations-container"
      }, // this.state.annotationListItems.map(listItem =>
      annotationClasueList.map(function (listItem) {
        return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_ClauseAnnotationItem__WEBPACK_IMPORTED_MODULE_5__["default"], {
          key: listItem.id,
          annotation: listItem,
          selectedAnnotationId: _this2.state.selectedAnnotationId,
          annotationManager: _this2.props.annotationManager
        });
      })))))));
    }
  }]);

  return CustomPdfActions;
}(react__WEBPACK_IMPORTED_MODULE_0__["Component"]);

/* harmony default export */ __webpack_exports__["default"] = (CustomPdfActions);

/***/ })

})
//# sourceMappingURL=a864647-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJhODY0NjQ3LW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==