/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import {Nav, NavItem, NavLink} from 'reactstrap';
import React, {Component} from 'react';

export default class MainNav extends Component {
  render() {
    return (
      <Nav vertical>
        <NavItem>
          <NavLink href="#">NPC</NavLink>
        </NavItem>
      </Nav>
    );
  }
}
