/* global initialProps */
import App from './components/App';
import React from 'react';
import ReactDOM from 'react-dom';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';

ReactDOM.render(<App navItems={initialProps.items}/>, document.getElementById('App'));
