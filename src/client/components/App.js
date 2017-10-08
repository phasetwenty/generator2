/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import MainNav from './MainNav';
import {Navbar, NavbarBrand} from 'reactstrap';
import OutputTable from './OutputTable';
import PropTypes from 'prop-types';
import React, {Component} from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import 'whatwg-fetch';

export default class App extends Component {
  static DEFAULT_OBJECT = 'thieves';

  render() {
    return (
        <Router>
          <div>
            <Navbar color="dark" className="text-light">
              <NavbarBrand>generator</NavbarBrand>
            </Navbar>
            <div className="container-fluid">
              <div className="row">
                <div className="col-3">
                  <MainNav items={this.props.navItems}/>
                </div>
                <div className="col-4">
                  <Route path="/:slug?" render={this.outputTable}/>
                </div>
              </div>
            </div>
          </div>
        </Router>
    );
  }

  fetchObject = (slug) => {
    slug = slug || App.DEFAULT_OBJECT;
    return fetch(`http://localhost:8080/api/v1/${slug}`)
      .then((response) => {
        return response.json();
      });
  };

  outputTable = (props) => {
    return <OutputTable fetchPromise={this.fetchObject} {...props} />;
  };
}

App.propTypes = {
  navItems: PropTypes.array.isRequired
};
