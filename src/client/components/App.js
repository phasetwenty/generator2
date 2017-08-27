/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import {Nav, NavItem, NavLink, Navbar, NavbarBrand} from 'reactstrap';
import React, {Component} from 'react';

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <Navbar color="dark" className="text-light">
          <NavbarBrand>generator</NavbarBrand>
        </Navbar>
        <div className="container-fluid">
          <div className="row">
            <div className="col-3">
              <Nav vertical>
                <NavItem>
                  <NavLink href="#">NPC</NavLink>
                </NavItem>
              </Nav>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
