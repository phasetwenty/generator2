/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import MainNav from './MainNav';
import {Navbar, NavbarBrand} from 'reactstrap';
import OutputTable from './OutputTable';
import PropTypes from 'prop-types';
import React from 'react';

const App = (props) => {
  return (
    <div>
      <Navbar color="dark" className="text-light">
        <NavbarBrand>generator</NavbarBrand>
      </Navbar>
      <div className="container-fluid">
        <div className="row">
          <div className="col-3">
            <MainNav items={props.navItems}/>
          </div>
          <div className="col-4">
            <OutputTable/>
          </div>
        </div>
      </div>
    </div>
  );
};

App.propTypes = {
  navItems: PropTypes.array.isRequired
};

export default App;
