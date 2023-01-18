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
/* harmony import */ var _adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @adobe/react-spectrum */ "./node_modules/@adobe/react-spectrum/dist/module.js");
/* harmony import */ var react_modern_drawer__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-modern-drawer */ "./node_modules/react-modern-drawer/dist/index.modern.js");
/* harmony import */ var react_modern_drawer_dist_index_css__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-modern-drawer/dist/index.css */ "./node_modules/react-modern-drawer/dist/index.css");
/* harmony import */ var react_modern_drawer_dist_index_css__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react_modern_drawer_dist_index_css__WEBPACK_IMPORTED_MODULE_4__);
function _slicedToArray(arr, i) { return _arrayWithHoles(arr) || _iterableToArrayLimit(arr, i) || _unsupportedIterableToArray(arr, i) || _nonIterableRest(); }

function _nonIterableRest() { throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _iterableToArrayLimit(arr, i) { var _i = arr == null ? null : typeof Symbol !== "undefined" && arr[Symbol.iterator] || arr["@@iterator"]; if (_i == null) return; var _arr = []; var _n = true; var _d = false; var _s, _e; try { for (_i = _i.call(arr); !(_n = (_s = _i.next()).done); _n = true) { _arr.push(_s.value); if (i && _arr.length === i) break; } } catch (err) { _d = true; _e = err; } finally { try { if (!_n && _i["return"] != null) _i["return"](); } finally { if (_d) throw _e; } } return _arr; }

function _arrayWithHoles(arr) { if (Array.isArray(arr)) return arr; }


 // import "./sidebar-styles.css";






function SidebarTable(_ref) {
  var documentTable = _ref.documentTable,
      updatePdfRendered = _ref.updatePdfRendered,
      showImpact = _ref.showImpact;

  var _useState = Object(react__WEBPACK_IMPORTED_MODULE_0__["useState"])(false),
      _useState2 = _slicedToArray(_useState, 2),
      isOpen = _useState2[0],
      setIsOpen = _useState2[1];

  var handleTrigger = function handleTrigger() {
    return setIsOpen(!isOpen);
  };

  function GetTable() {
    if (showImpact) {
      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableView"], {
        colorScheme: "lightest",
        "aria-label": "Example table with static contents",
        selectionMode: "single",
        disallowEmptySelection: true,
        selectionStyle: "highlight",
        onAction: function onAction(key) {
          return updatePdfRendered(key);
        },
        isQuiet: true,
        overflowMode: "wrap"
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableHeader"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        minWidth: 120
      }, "Name"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        align: "end"
      }, "Impact"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], null, "Confidence"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        maxWidth: 120
      }, "Reviewed?"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        maxWidth: 80
      }, "TFC"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        align: "end"
      }, "Revenue")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableBody"], null, Object.entries(documentTable).map(function (_ref2) {
        var _ref3 = _slicedToArray(_ref2, 2),
            key = _ref3[0],
            value = _ref3[1];

        return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Row"], {
          key: key,
          className: "".concat(documentTable[key].highlightsArr[0].creator.isReviewed === true ? "review-true" : "review-false")
        }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, key), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.impactFactor)), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.tfcConfidence)), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.highlightsArr[0].creator.isReviewed === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.highlightsArr[0].creator.isCorrect === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.revenue)));
      })));
    } else {
      return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableView"], {
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
      }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableHeader"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        minWidth: 120
      }, "Name"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        maxWidth: 120
      }, "Reviewed?"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        maxWidth: 80
      }, "TFC"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
        align: "end"
      }, "Revenue")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableBody"], null, Object.entries(documentTable).map(function (_ref4) {
        var _ref5 = _slicedToArray(_ref4, 2),
            key = _ref5[0],
            value = _ref5[1];

        return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Row"], {
          key: key,
          className: "".concat(documentTable[key].highlightsArr[0].creator.isReviewed === true ? "review-true" : "review-false")
        }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, key), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.highlightsArr[0].creator.isReviewed === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.highlightsArr[0].creator.isCorrect === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.revenue)));
      })));
    }
  }

  return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react__WEBPACK_IMPORTED_MODULE_0___default.a.Fragment, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("button", {
    onClick: handleTrigger
  }, "Show Table"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_modern_drawer__WEBPACK_IMPORTED_MODULE_3__["default"], {
    open: isOpen,
    onClose: handleTrigger,
    direction: "top",
    className: "top-bar",
    enableOverlay: false
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableView"], {
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
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableHeader"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
    minWidth: 120
  }, "Name"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
    maxWidth: 120
  }, "Reviewed?"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
    maxWidth: 80
  }, "TFC"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Column"], {
    align: "end"
  }, "Revenue")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["TableBody"], null, Object.entries(documentTable).map(function (_ref6) {
    var _ref7 = _slicedToArray(_ref6, 2),
        key = _ref7[0],
        value = _ref7[1];

    return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Row"], {
      key: key,
      className: "".concat(documentTable[key].highlightsArr[0].creator.isReviewed === true ? "review-true" : "review-false")
    }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, key), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.highlightsArr[0].creator.isReviewed === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.highlightsArr[0].creator.isCorrect === true ? "yes" : "no")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(_adobe_react_spectrum__WEBPACK_IMPORTED_MODULE_2__["Cell"], null, "".concat(value.revenue)));
  })))));
}

/* harmony default export */ __webpack_exports__["default"] = (SidebarTable);

/***/ })

})
//# sourceMappingURL=59bc357-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiI1OWJjMzU3LW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==