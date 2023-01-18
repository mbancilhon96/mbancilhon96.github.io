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
/* harmony import */ var react_bootstrap_Container__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-bootstrap/Container */ "./node_modules/react-bootstrap/esm/Container.js");
/* harmony import */ var react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-bootstrap/Row */ "./node_modules/react-bootstrap/esm/Row.js");
/* harmony import */ var react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-bootstrap/Col */ "./node_modules/react-bootstrap/esm/Col.js");
/* harmony import */ var react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-bootstrap-icons */ "./node_modules/react-bootstrap-icons/dist/index.js");
/* harmony import */ var react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react-bootstrap/Badge */ "./node_modules/react-bootstrap/esm/Badge.js");
/* harmony import */ var react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-bootstrap/Stack */ "./node_modules/react-bootstrap/esm/Stack.js");
/* harmony import */ var react_bootstrap_Dropdown__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! react-bootstrap/Dropdown */ "./node_modules/react-bootstrap/esm/Dropdown.js");
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










var ClauseItem = /*#__PURE__*/function (_Component) {
  _inherits(ClauseItem, _Component);

  var _super = _createSuper(ClauseItem);

  function ClauseItem() {
    var _this;

    _classCallCheck(this, ClauseItem);

    _this = _super.call(this);

    _defineProperty(_assertThisInitialized(_this), "editButtonOnClick", function (e) {
      e.stopPropagation();
      /* If in editMode */

      if (_this.state.inEditMode) {
        _this.editAnnotation(_this.props.annotation);
        /* toggle editMode */


        _this.setState({
          inEditMode: false
        });
      } else {
        /* Default input value */
        if (!_this.state.editInputValue) {
          _this.setState({
            editInputValue: _this.props.annotation.bodyValue
          });
        }
        /* toggle editMode */


        _this.setState({
          inEditMode: true
        });
      }
    });

    _defineProperty(_assertThisInitialized(_this), "deleteButtonOnClick", function (e) {
      e.stopPropagation();

      _this.deleteAnnotation(_this.props.annotation.id);
    });

    _defineProperty(_assertThisInitialized(_this), "clauseItemOnClick", function () {
      _this.props.annotationManager.selectAnnotation(_this.props.annotation.id).then(function () {})["catch"](function (error) {
        console.log(error);
      });
    });

    _defineProperty(_assertThisInitialized(_this), "editInputOnChange", function (e) {
      e.persist();

      _this.setState({
        editInputValue: e.target.value
      });
    });

    _defineProperty(_assertThisInitialized(_this), "editAnnotation", function (annotation) {
      annotation.bodyValue = _this.state.editInputValue;

      _this.props.annotationManager.updateAnnotation(annotation).then(function () {
        console.log("Annotation updated successfully.");
      })["catch"](function (error) {
        console.log(error);
      });
    });

    _defineProperty(_assertThisInitialized(_this), "deleteAnnotation", function (annotationId) {
      var filter = {
        annotationIds: [annotationId]
      };

      _this.props.annotationManager.deleteAnnotations(filter).then(function () {
        console.log("Annotation deleted successfully.");
      })["catch"](function (error) {
        console.log(error);
      });
    });

    _this.state = {
      inEditMode: false,
      editInputValue: undefined
    };
    return _this;
  }
  /* Bind editAnnotation to edit button. */


  _createClass(ClauseItem, [{
    key: "render",
    value: function render() {
      var inEditMode = this.state.inEditMode;
      var _this$props = this.props,
          annotation = _this$props.annotation,
          selectedAnnotationId = _this$props.selectedAnnotationId;
      var annot_name = annotation.creator.name.toLowerCase();

      if (annot_name == "opt_out" || annot_name == "Opt_out") {
        annot_name = "Opt-out";
      } else if (annot_name == "terminations" || annot_name == "termination") {
        annot_name = "Termination";
      } else if (annot_name == "payments" || annot_name == "payment") {
        annot_name = "Payment";
      }

      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("li", {
        id: annotation.id // className={ selectedAnnotationId === annotation.id ? "selected" : "unselected" }
        ,
        className: "".concat(selectedAnnotationId === annotation.id ? "selected" : "unselected", " ").concat(annot_name),
        onClick: this.clauseItemOnClick
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_7__["default"], {
        gap: 2
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Container__WEBPACK_IMPORTED_MODULE_2__["default"], {
        className: "stack-annotation-container"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__["default"], {
        className: "clause-label"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "clause-label ".concat(annot_name.toLowerCase())
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("small", null, annot_name))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("small", null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("button", {
        className: "edit",
        onClick: this.editButtonOnClick
      }, inEditMode ? "Save" : "Edit"))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("small", null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("button", {
        className: "delete",
        onClick: this.deleteButtonOnClick
      }, "Delete"))))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "clause-body"
      }, inEditMode ? /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("input", {
        type: "text",
        defaultValue: annotation.bodyValue,
        onChange: this.editInputOnChange
      }) : /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("label", null, annotation.bodyValue)), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "page-number"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("small", null, "Page ", parseInt(annotation.target.selector.node.index) + 1))));
    }
  }]);

  return ClauseItem;
}(react__WEBPACK_IMPORTED_MODULE_0__["Component"]);

var EntityItem = /*#__PURE__*/function (_Component2) {
  _inherits(EntityItem, _Component2);

  var _super2 = _createSuper(EntityItem);

  function EntityItem() {
    var _this2;

    _classCallCheck(this, EntityItem);

    _this2 = _super2.call(this);

    _defineProperty(_assertThisInitialized(_this2), "editButtonOnClick", function (e) {
      e.stopPropagation();
      /* If in editMode */

      if (_this2.state.inEditMode) {
        _this2.editAnnotation(_this2.props.annotation);
        /* toggle editMode */


        _this2.setState({
          inEditMode: false
        });
      } else {
        /* Default input value */
        if (!_this2.state.editInputValue) {
          _this2.setState({
            editInputValue: _this2.props.annotation.bodyValue
          });
        }
        /* toggle editMode */


        _this2.setState({
          inEditMode: true
        });
      }
    });

    _defineProperty(_assertThisInitialized(_this2), "deleteButtonOnClick", function (e) {
      e.stopPropagation();

      _this2.deleteAnnotation(_this2.props.annotation.id);
    });

    _defineProperty(_assertThisInitialized(_this2), "entityItemOnClick", function () {
      _this2.props.annotationManager.selectAnnotation(_this2.props.annotation.id).then(function () {})["catch"](function (error) {
        console.log(error);
      });
    });

    _defineProperty(_assertThisInitialized(_this2), "editInputOnChange", function (e) {
      e.persist();

      _this2.setState({
        editInputValue: e.target.value
      });
    });

    _defineProperty(_assertThisInitialized(_this2), "editAnnotation", function (annotation) {
      annotation.bodyValue = _this2.state.editInputValue;

      _this2.props.annotationManager.updateAnnotation(annotation).then(function () {
        console.log("Annotation updated successfully.");
      })["catch"](function (error) {
        console.log(error);
      });
    });

    _defineProperty(_assertThisInitialized(_this2), "deleteAnnotation", function (annotationId) {
      var filter = {
        annotationIds: [annotationId]
      };

      _this2.props.annotationManager.deleteAnnotations(filter).then(function () {
        console.log("Annotation deleted successfully.");
      })["catch"](function (error) {
        console.log(error);
      });
    });

    _this2.state = {
      inEditMode: false,
      editInputValue: undefined
    };
    return _this2;
  }
  /* Bind editAnnotation to edit button. */


  _createClass(EntityItem, [{
    key: "render",
    value: function render() {
      var inEditMode = this.state.inEditMode;
      var _this$props2 = this.props,
          annotation = _this$props2.annotation,
          selectedAnnotationId = _this$props2.selectedAnnotationId;
      var icon;

      if (annotation.creator.name == "Parties") {
        icon = /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span", {
          className: "entity-icon"
        }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_5__["PersonCircle"], {
          className: "ml-4"
        }));
        console.log("it's parties");
      } else if (annotation.creator.name == "Amount") {
        icon = /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span", {
          className: "entity-icon"
        }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_5__["CurrencyDollar"], {
          className: "ml-4"
        }));
      }

      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("li", {
        id: annotation.id // className={ selectedAnnotationId === annotation.id ? "selected" : "unselected" }
        ,
        className: "".concat(selectedAnnotationId === annotation.id ? "selected" : "unselected", " ").concat(annotation.creator.name.toLowerCase()),
        onClick: this.entityItemOnClick
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Stack__WEBPACK_IMPORTED_MODULE_7__["default"], {
        gap: 2
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Container__WEBPACK_IMPORTED_MODULE_2__["default"], {
        className: "stack-annotation-container"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_3__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__["default"], {
        className: "entity-label"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "entity-label ".concat(annotation.creator.name.toLowerCase())
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("p", {
        className: "entity-text"
      }, icon, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span", null, annotation.creator.name, ": ", annotation.bodyValue)))))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "page-number"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("small", null, "Page ", parseInt(annotation.target.selector.node.index) + 1))));
    }
  }]);

  return EntityItem;
}(react__WEBPACK_IMPORTED_MODULE_0__["Component"]);

var CustomPdfActions = /*#__PURE__*/function (_Component3) {
  _inherits(CustomPdfActions, _Component3);

  var _super3 = _createSuper(CustomPdfActions);

  function CustomPdfActions() {
    var _this3;

    _classCallCheck(this, CustomPdfActions);

    for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {
      args[_key] = arguments[_key];
    }

    _this3 = _super3.call.apply(_super3, [this].concat(args));

    _defineProperty(_assertThisInitialized(_this3), "state", {
      annotationListItems: [],
      selectedAnnotationId: undefined
    });

    _defineProperty(_assertThisInitialized(_this3), "annotationEventListener", function (event) {
      if (event.type === "ANNOTATION_ADDED") {
        if (event.data.bodyValue) {
          _this3.onAnnotationAdded(event.data);
        } else {
          _this3.addCommentText(event.data);
        }
      }

      if (event.type === "ANNOTATION_DELETED") {
        _this3.onAnnotationDeleted(event.data.id);
      }

      if (event.type === "ANNOTATION_SELECTED") {
        _this3.toggleSelectedAnnotation(event.data.id);
      }

      if (event.type === "ANNOTATION_UNSELECTED") {
        _this3.toggleSelectedAnnotation();
      }

      if (event.type === "ANNOTATION_UPDATED" && event.data.target.selector.subtype === "freetext") {
        _this3.onTextAnnotationUpdated(event.data);
      }

      console.log(event);
    });

    _defineProperty(_assertThisInitialized(_this3), "onAnnotationAdded", function (annotation) {
      _this3.setState({
        annotationListItems: [].concat(_toConsumableArray(_this3.state.annotationListItems), [annotation])
      });
    });

    _defineProperty(_assertThisInitialized(_this3), "onAnnotationDeleted", function (id) {
      _this3.setState({
        annotationListItems: _this3.state.annotationListItems.filter(function (item) {
          return item.id !== id;
        })
      });
    });

    _defineProperty(_assertThisInitialized(_this3), "toggleSelectedAnnotation", function (id) {
      _this3.setState({
        selectedAnnotationId: id
      });
    });

    _defineProperty(_assertThisInitialized(_this3), "onTextAnnotationUpdated", function (annotation) {
      var index = _this3.state.annotationListItems.findIndex(function (item) {
        return item.id === annotation.id;
      });

      _this3.state.annotationListItems[index].bodyValue = annotation.bodyValue;

      _this3.setState({
        annotationListItems: _this3.state.annotationListItems
      });
    });

    _defineProperty(_assertThisInitialized(_this3), "addCommentText", function (annotation) {
      var type = annotation.target.selector.subtype; // const comment = prompt("Enter the text associated with " + type, "Added a " + type) || "Added a " + type;

      var comment = "Added a " + type;
      annotation.bodyValue = comment;

      _this3.props.annotationManager.updateAnnotation(annotation).then(function () {
        console.log("Annotation updated successfully.");

        _this3.onAnnotationAdded(annotation);
      })["catch"](function (error) {
        console.log(error);
      });
    });

    return _this3;
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
      var _this4 = this;

      // ”category": {clause} or {entity}
      // “name”: {clause type} or {entity type}
      var annotationEntityList = [];
      var annotationClasueList = [];
      this.state.annotationListItems.forEach(function (element) {
        // console.log({ element });
        // console.log(this.props.highlightsDict[element.id].category)
        if (_this4.props.highlightsDict[element.id].category == "Clause") {
          annotationClasueList.push(element);
        } else if (_this4.props.highlightsDict[element.id].category == "Entity") {
          annotationEntityList.push(element);
        }
      });
      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
        className: "panel-container"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
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
        return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(EntityItem, {
          key: listItem.id,
          annotation: listItem,
          selectedAnnotationId: _this4.state.selectedAnnotationId,
          annotationManager: _this4.props.annotationManager
        });
      }))))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"], {
        defaultActiveKey: ['1'],
        alwaysOpen: true
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Item, {
        eventKey: "1"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Header, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("h2", {
        className: "accordion-header"
      }, "Key Clauses")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Accordion__WEBPACK_IMPORTED_MODULE_1__["default"].Body, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_3__["default"], {
        className: "category-badge"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_6__["default"], {
        bg: "opt-out"
      }, "Opt-out"), ' '), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_6__["default"], {
        bg: "termination"
      }, "Termination"), ' '), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Col__WEBPACK_IMPORTED_MODULE_4__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Badge__WEBPACK_IMPORTED_MODULE_6__["default"], {
        bg: "payment"
      }, "Payment"), ' ')), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("ul", {
        className: "annotations-container"
      }, // this.state.annotationListItems.map(listItem =>
      annotationClasueList.map(function (listItem) {
        return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(ClauseItem, {
          key: listItem.id,
          annotation: listItem,
          selectedAnnotationId: _this4.state.selectedAnnotationId,
          annotationManager: _this4.props.annotationManager
        });
      })))))));
    }
  }]);

  return CustomPdfActions;
}(react__WEBPACK_IMPORTED_MODULE_0__["Component"]);

/* harmony default export */ __webpack_exports__["default"] = (CustomPdfActions);

/***/ })

})
//# sourceMappingURL=3b99635-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiIzYjk5NjM1LW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==