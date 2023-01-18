webpackHotUpdatedash_pdf_components("main",{

/***/ "./src/lib/SidebarTable.js":
/*!*********************************!*\
  !*** ./src/lib/SidebarTable.js ***!
  \*********************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-bootstrap-icons */ "./node_modules/react-bootstrap-icons/dist/index.js");
/* harmony import */ var _sidebar_styles_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./sidebar-styles.css */ "./src/lib/sidebar-styles.css");
/* harmony import */ var _sidebar_styles_css__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_sidebar_styles_css__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @adobe/react-spectrum */ "./node_modules/@adobe/react-spectrum/dist/module.js");
function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _iterableToArrayLimit(arr, i) { var _i = arr == null ? null : typeof Symbol !== "undefined" && arr[Symbol.iterator] || arr["@@iterator"]; if (_i == null) return; var _arr = []; var _n = true; var _d = false; var _s, _e; try { for (_i = _i.call(arr); !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }







function SidebarTable(_ref) {
  var documentTable = _ref.documentTable,
      updatePdfRendered = _ref.updatePdfRendered;

  var _useState = Object(react__WEBPACK_IMPORTED_MODULE_0__["useState"])(false),
      _useState2 = _slicedToArray(_useState, 2),
      isOpen = _useState2[0],
      setIsOpen = _useState2[1];

  var handleTrigger = function handleTrigger() {
    return setIsOpen(!isOpen);
  }; // console.log("in side bar");
  // console.log(documentTable[pdfRendered].highlightsArr[0].creator.isReviewed);


  return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
    className: "sidebar ".concat(isOpen ? "sidebar--open" : "")
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("div", {
    className: "trigger",
    onClick: handleTrigger
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_1__["ArrowsAngleExpand"], null)), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["TableView"], {
    colorScheme: "lightest",
    "aria-label": "Example table with static contents",
    selectionMode: "single",
    disallowEmptySelection: true,
    selectionStyle: "highlight" // onAction={(key) => console.log(`clicked item ${key}...`)}
    ,
    onAction: function onAction(key) {
      return updatePdfRendered(key);
    },
    isQuiet: true // density="compact"
    ,
    overflowMode: "wrap"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["TableHeader"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Column"], {
    minWidth: 120
  }, "Name"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Column"], {
    align: "end"
  }, "Impact"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Column"], {
    maxWidth: 120
  }, "Reviewed?"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Column"], {
    maxWidth: 80
  }, "TFC"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Column"], {
    align: "end"
  }, "Revenue")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["TableBody"], null, Object.entries(documentTable).map(function (_ref2) {
    var _ref3 = _slicedToArray(_ref2, 2),
        key = _ref3[0],
        value = _ref3[1];

    return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Row"], {
      key: key,
      className: "".concat(documentTable[key].highlightsArr[0].creator.isReviewed === true ? "review-true" : "review-false")
    }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Cell"], null, key), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Cell"], null, "".concat(value.impactFactor)), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Cell"], null, "".concat(value.highlightsArr[0].creator.isReviewed === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Cell"], null, "".concat(value.highlightsArr[0].creator.isCorrect === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_3__["Cell"], null, "".concat(value.revenue)));
  })))) // end side bar div
  ;
}

/* harmony default export */ __webpack_exports__["default"] = (SidebarTable);

/***/ })

})
//# sourceMappingURL=38bb4f4-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiIzOGJiNGY0LW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==