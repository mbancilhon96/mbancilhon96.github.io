/* eslint no-magic-numbers: 0 */
import React, {Component} from 'react';
import { DashPdfComponents } from '../lib';
// import { annotationExample } from '../lib/annotationExample';
import { annotationExample } from '../lib/annotationTFCExample';
import {defaultTheme, Provider} from '@adobe/react-spectrum';
import { docTableExample } from '../lib/docTableExample';

let file2 = "https://dl.dropboxusercontent.com/s/5ui4jwcvfitbscu/Control_Service-B_Electrical.pdf";
// let file2 = "https://documentcloud.adobe.com/view-sdk-demo/PDFs/Bodea Brochure.pdf";

class App extends Component {

    componentDidMount() {
        this.loadJS();
    }

    loadJS = () => {
        ////// load the embed API script
        const url = "https://documentcloud.adobe.com/view-sdk/viewer.js";
        // const url = "https://documentservices.adobe.com/view-sdk/viewer.js";
        const script = document.createElement("script");
        script.src = url;
        script.async = true;
        document.body.appendChild(script);
    }

    constructor() {
        super();
        this.state = {
            value: ''
        };
        this.setProps = this.setProps.bind(this);
    }

    setProps(newProps) {
        this.setState(newProps);
    }

    
    render() {

        // console.log(docTableExample[0].contractId)
        return (
            
            <Provider theme={defaultTheme} colorScheme="light">
            <div>
                <DashPdfComponents
                    setProps={this.setProps}
                    {...this.state}
                    id = 'pdf-view'
                    label = 'pdf-view-label'
                    apiKey = '899d52477b7d4b589f808242e8d36cc3'
                    documentTable = {docTableExample}
                    showImpact = {true}
                />
            </div>
            </Provider>

        )
    }
}

export default App;
