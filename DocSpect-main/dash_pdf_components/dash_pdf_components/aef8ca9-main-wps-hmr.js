webpackHotUpdatedash_pdf_components("main",{

/***/ "./src/lib/ClauseTFCAnnotationItem.js":
/*!********************************************!*\
  !*** ./src/lib/ClauseTFCAnnotationItem.js ***!
  \********************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_bootstrap_Container__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-bootstrap/Container */ "./node_modules/react-bootstrap/esm/Container.js");
/* harmony import */ var react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-bootstrap/Row */ "./node_modules/react-bootstrap/esm/Row.js");
/* harmony import */ var react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-bootstrap/Col */ "./node_modules/react-bootstrap/esm/Col.js");
/* harmony import */ var react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-bootstrap/Stack */ "./node_modules/react-bootstrap/esm/Stack.js");
/* harmony import */ var _AnnotationItem__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./AnnotationItem */ "./src/lib/AnnotationItem.js");
/* harmony import */ var _spectrum_icons_workflow_CheckmarkCircle__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @spectrum-icons/workflow/CheckmarkCircle */ "./node_modules/@spectrum-icons/workflow/CheckmarkCircle.js");
/* harmony import */ var _spectrum_icons_workflow_CheckmarkCircle__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_spectrum_icons_workflow_CheckmarkCircle__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _spectrum_icons_workflow_CloseCircle__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @spectrum-icons/workflow/CloseCircle */ "./node_modules/@spectrum-icons/workflow/CloseCircle.js");
/* harmony import */ var _spectrum_icons_workflow_CloseCircle__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_spectrum_icons_workflow_CloseCircle__WEBPACK_IMPORTED_MODULE_7__);
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










var ClauseTFCAnnotationItem = /*#__PURE__*/function (_AnnotationItem) {
  _inherits(ClauseTFCAnnotationItem, _AnnotationItem);

  var _super = _createSuper(ClauseTFCAnnotationItem);

  function ClauseTFCAnnotationItem() {
    var _this;

    _classCallCheck(this, ClauseTFCAnnotationItem);

    _this = _super.call(this);

    _defineProperty(_assertThisInitialized(_this), "acceptButtonOnClick", function (e) {
      e.stopPropagation();

      _this.updateAnnotationReview(_this.props.annotation.id, true);
    });

    _defineProperty(_assertThisInitialized(_this), "deleteButtonOnClick", function (e) {
      e.stopPropagation();

      _this.updateAnnotationReview(_this.props.annotation.id, false);
    });

    _defineProperty(_assertThisInitialized(_this), "updateAnnotationReview", function (annotationId, status) {
      _this.setState({
        isReviewed: status
      });

      _this.props.annotation.creator.review = status;

      _this.props.updateAnnotationReview(annotationId, status);
    });

    _this.state = {
      isReviewed: false
    };
    return _this;
  }
  /* Bind deleteAnnotation to delete button. */


  _createClass(ClauseTFCAnnotationItem, [{
    key: "render",
    value: function render() {
      var _this$state = this.state,
          inEditMode = _this$state.inEditMode,
          isReviewed = _this$state.isReviewed;
      var _this$props = this.props,
          annotation = _this$props.annotation,
          selectedAnnotationId = _this$props.selectedAnnotationId;
      var annot_name = annotation.creator.name;
      var annot_review = annotation.creator.isReviewed;
      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("li", {
        id: annotation.id,
        className: "".concat(selectedAnnotationId === annotation.id ? "selected" : "unselected", " ").concat(annot_name, " ").concat(annot_review),
        onClick: this.itemOnClick
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_4__["default"], {
        gap: 2
      }, !this.state.isReviewed && /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Container__WEBPACK_IMPORTED_MODULE_1__["default"], {
        className: "stack-review-container"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_2__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("button", {
        className: "accept",
        onClick: this.acceptButtonOnClick
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span", null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_spectrum_icons_workflow_CheckmarkCircle__WEBPACK_IMPORTED_MODULE_6___default.a, {
        "aria-label": "Positive Checkmark",
        color: "positive"
      })))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("button", {
        className: "cancel",
        onClick: this.deleteButtonOnClick
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span", null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_spectrum_icons_workflow_CloseCircle__WEBPACK_IMPORTED_MODULE_7___default.a, {
        "aria-label": "Negative Close",
        color: "negative"
      })))))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "clause-body"
      }, inEditMode ? /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("input", {
        type: "text",
        defaultValue: annotation.bodyValue,
        onChange: this.editInputOnChange
      }) : /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("label", null, annotation.bodyValue)), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_2__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "page-number"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("small", null, "Page ", parseInt(annotation.target.selector.node.index) + 1))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("small", null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("button", {
        className: "edit",
        onClick: this.editButtonOnClick
      }, inEditMode ? "Save" : "Edit"))))));
    }
  }]);

  return ClauseTFCAnnotationItem;
}(_AnnotationItem__WEBPACK_IMPORTED_MODULE_5__["default"]);

/* harmony default export */ __webpack_exports__["default"] = (ClauseTFCAnnotationItem);

/***/ })

})
//# sourceMappingURL=aef8ca9-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJhZWY4Y2E5LW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==