# PDF viewer dash UI

## Install dependencies
```
pip install -r requirements.txt
```

## Run app

1. For now run the app navigate to `dash_pdf_components`
2. Run calling `usage.py`

```
cd dash_pdf_component
python usage.py
```

View on http://localhost:8050/. 

**It's Important to use localhost for authentication purposes with the [Adobe Embed API](https://developer.adobe.com/document-services/docs/overview/pdf-embed-api/).


## Annotation Scheme

To see an example of the annotation schema expected: `dash_pdf_components/src/annotationExample.js`. The "creator" part:

- Entity can be Parties or Amount
- Clause can be Opt-Out, Payment, or Termination
- id between annotations MUST be unique
- source MUST match the file ID. For now assign source as: `"source": "0d07d124-ac85-43b3-a867-36930f502ac6"`

Example:
- `"creator": {
    "category": "Clause",
    "type": "Person",
    "name": "Termination"
 }`
 
 - `"creator": {
    "category": "Entity",
    "type": "Person",
    "name": "Amount"
 }`

## TODO 

- [ ] Need to move code from usage to app.py and export the dash pdf components
- [ ] Expose other API function calls for annotation events
- [ ] in dash component library write function to match annotation "source" to "fileID" in props 
- [x] Test import json file with annotation list


## PDF Embed API
1. You need to set the client key [apiKey = <your_key>] when you use the DashPdfComponents.
2. fileUrl is the link to the PDF stored externally or locally. Local files are located in `assets/files/`. For external url, here's a sample: https://documentcloud.adobe.com/view-sdk-demo/PDFs/Bodea%20Brochure.pdf

This is what it looks like if it's working:

<img width="1792" alt="user interface screenshot of PDF reader on the left and insights panel on the right"  src="https://git.corp.adobe.com/storage/user/44556/files/3410404e-3324-42cb-a505-b396b574d652">


## Making Changes to the Dash Component
To use the Embed API, we create a custom Dash component in React. If you want to make changes, navigate to `dash_pdf_components`:

1. Install npm packages
    ```
    $ npm install
    ```
2. Create a virtual env and activate.
    ```
    $ virtualenv venv
    $ . venv/bin/activate
    ```
    _Note: venv\Scripts\activate for windows_

3. Install python packages required to build components.
    ```
    $ pip install -r requirements.txt
    ```
4. Install the python packages for testing (optional)
    ```
    $ pip install -r tests/requirements.txt
    ```

### Write your component code in `src/lib/components/DashPdfComponents.react.js`.

- The demo app is in `src/demo` and you will import your example component code into your demo app.
    1. Run the app
        ```
        $ npm start
        ```
    2. See your changes in: http://localhost:8030/

- Test your code in a Python environment with Dash:
    1. Build your code
        ```
        $ npm run build
        ```
    2. Run and modify the `usage.py` sample dash app:
        ```
        $ python usage.py
        ```
- Write tests for your component.
    - A sample test is available in `tests/test_usage.py`, it will load `usage.py` and you can then automate interactions with selenium.
    - Run the tests with `$ pytest tests`.
    - The Dash team uses these types of integration tests extensively. Browse the Dash component code on GitHub for more examples of testing (e.g. https://github.com/plotly/dash-core-components)
- Add custom styles to your component by putting your custom CSS files into your distribution folder (`dash_pdf_components`).
    - Make sure that they are referenced in `MANIFEST.in` so that they get properly included when you're ready to publish your component.
    - Make sure the stylesheets are added to the `_css_dist` dict in `dash_pdf_components/__init__.py` so dash will serve them automatically when the component suite is requested.

### Create a production build and publish:

1. Build your code:
    ```
    $ npm run build
    ```
2. Create a Python distribution
    ```
    $ python setup.py sdist bdist_wheel
    ```
    This will create source and wheel distribution in the generated the `dist/` folder.
    See [PyPA](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project)
    for more information.

3. Test your tarball by copying it into a new environment and installing it locally:
    ```
    $ pip install dash_pdf_components-0.0.1.tar.gz
    ```
