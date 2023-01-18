webpackHotUpdatedash_pdf_components("main",{

/***/ "./src/lib/AnnotationModal.js":
/*!************************************!*\
  !*** ./src/lib/AnnotationModal.js ***!
  \************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react-bootstrap/Row */ "./node_modules/react-bootstrap/esm/Row.js");
/* harmony import */ var react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react-bootstrap/Form */ "./node_modules/react-bootstrap/esm/Form.js");
/* harmony import */ var react_bootstrap_Modal__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react-bootstrap/Modal */ "./node_modules/react-bootstrap/esm/Modal.js");
/* harmony import */ var react_bootstrap_Button__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react-bootstrap/Button */ "./node_modules/react-bootstrap/esm/Button.js");
/* harmony import */ var react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react-bootstrap/ToggleButton */ "./node_modules/react-bootstrap/esm/ToggleButton.js");
/* harmony import */ var react_bootstrap_ToggleButtonGroup__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! react-bootstrap/ToggleButtonGroup */ "./node_modules/react-bootstrap/esm/ToggleButtonGroup.js");
/* harmony import */ var react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! react-bootstrap-icons */ "./node_modules/react-bootstrap-icons/dist/index.js");









var AnnotationModal = function AnnotationModal(_ref) {
  var show = _ref.show,
      onExited = _ref.onExited,
      categoryValue = _ref.categoryValue,
      toggleCategory = _ref.toggleCategory,
      nameValue = _ref.nameValue,
      toggleName = _ref.toggleName;
  return /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Modal__WEBPACK_IMPORTED_MODULE_3__["default"], {
    show: show,
    onExit: onExited
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Modal__WEBPACK_IMPORTED_MODULE_3__["default"].Header, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Modal__WEBPACK_IMPORTED_MODULE_3__["default"].Title, null, "Select annotation attributes")), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Modal__WEBPACK_IMPORTED_MODULE_3__["default"].Body, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__["default"].Group, {
    className: "mb-4",
    controlId: "form.Category"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__["default"].Label, null, "Is this annotation a key entity or clause?"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_1__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButtonGroup__WEBPACK_IMPORTED_MODULE_6__["default"], {
    type: "radio",
    name: "options",
    defaultValue: "Entity",
    value: categoryValue,
    onChange: toggleCategory
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__["default"], {
    id: "tbg-type-1",
    value: "Entity",
    variant: "outline-secondary"
  }, "Entity"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__["default"], {
    id: "tbg-type-2",
    value: "Clause",
    variant: "outline-secondary"
  }, "Clause")))), categoryValue == "Entity" && /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__["default"].Group, {
    className: "mb-4",
    controlId: "form.EntityType"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__["default"].Label, null, "What is the entity type?"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_1__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButtonGroup__WEBPACK_IMPORTED_MODULE_6__["default"], {
    type: "radio",
    name: "options",
    defaultValue: "Amount",
    value: nameValue,
    onChange: toggleName
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__["default"], {
    id: "tbg-entity-1",
    value: "Amount",
    variant: "outline-secondary"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span", {
    className: "entity-icon"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_7__["CurrencyDollar"], {
    className: "ml-4"
  })), "Amount"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__["default"], {
    id: "tbg-entity-2",
    value: "Parties",
    variant: "outline-secondary"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement("span", {
    className: "entity-icon"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_icons__WEBPACK_IMPORTED_MODULE_7__["PersonCircle"], {
    className: "ml-4"
  })), "Parties")))), categoryValue == "Clause" && /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__["default"].Group, {
    className: "mb-4",
    controlId: "form.ClauseType"
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Form__WEBPACK_IMPORTED_MODULE_2__["default"].Label, null, "What is the clause type?"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Row__WEBPACK_IMPORTED_MODULE_1__["default"], null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButtonGroup__WEBPACK_IMPORTED_MODULE_6__["default"], {
    type: "radio",
    name: "options",
    defaultValue: "Opt-out",
    value: nameValue,
    onChange: toggleName
  }, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__["default"], {
    "class": "btn-outline-opt-out",
    id: "tbg-clause-1",
    value: "Opt-out"
  }, "Opt-out"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__["default"], {
    id: "tbg-clause-2",
    value: "Termination",
    variant: "outline-secondary"
  }, "Termination"), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_ToggleButton__WEBPACK_IMPORTED_MODULE_5__["default"], {
    id: "tbg-clause-3",
    value: "Payment",
    variant: "outline-secondary"
  }, "Payment")))))), /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Modal__WEBPACK_IMPORTED_MODULE_3__["default"].Footer, null, /*#__PURE__*/react__WEBPACK_IMPORTED_MODULE_0___default.a.createElement(react_bootstrap_Button__WEBPACK_IMPORTED_MODULE_4__["default"], {
    variant: "primary",
    onClick: onExited
  }, "Done")));
}; // function AnnotationModal() {
// const [annotationModalVisible, toggleAnnotationModal] = useState(false);
// const [radioValue, setRadioValue] = useState('1');
// );


/* harmony default export */ __webpack_exports__["default"] = (AnnotationModal); // function AnnotationModal() {
//     const [show, setShow] = useState(false);
//     // const handleClose = () => setShow(false);
//     // const handleShow = () => setShow(true);
//     return (
//       <>
//         <Modal show={show}>
//         {/* <Modal> */}
//           <Modal.Header closeButton>
//             <Modal.Title>Modal heading</Modal.Title>
//           </Modal.Header>
//           <Modal.Body>
// <Form>
//   <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
//     <Form.Label>Email address</Form.Label>
//     <Form.Control
//       type="email"
//       placeholder="name@example.com"
//       autoFocus
//     />
//   </Form.Group>
//   <Form.Group
//     className="mb-3"
//     controlId="exampleForm.ControlTextarea1"
//   >
//     <Form.Label>Example textarea</Form.Label>
//     <Form.Control as="textarea" rows={3} />
//   </Form.Group>
// </Form>
//           </Modal.Body>
//           {/* <Modal.Footer>
//             <Button variant="secondary" onClick={handleClose}>
//               Close
//             </Button>
//             <Button variant="primary" onClick={handleClose}>
//               Save Changes
//             </Button>
//           </Modal.Footer> */}
//         </Modal>
//       </>
//     );
// }

/***/ })

})
//# sourceMappingURL=3bcbc63-main-wps-hmr.js.map
//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiIzYmNiYzYzLW1haW4td3BzLWhtci5qcyIsInNvdXJjZVJvb3QiOiIifQ==