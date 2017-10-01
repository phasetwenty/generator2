/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import {Dropdown, DropdownItem, DropdownMenu, DropdownToggle} from 'reactstrap';
import React, {Component} from 'react';

/*
 * May not be the best name.
 */
export default class MutableInstance extends Component {
  constructor(props) {
    super(props);

    this.state = {open: false};
  }

  toggle = () => {
    this.setState({open: !this.state.open});
  };

  render() {
    return (
      <Dropdown isOpen={this.state.open} tag='span' toggle={this.toggle}>
        <DropdownToggle tag="span" caret>
          {this.props.label}
        </DropdownToggle>
        <DropdownMenu>
          <DropdownItem onClick={this.toggle}>Item1</DropdownItem>
          <DropdownItem onClick={this.toggle}>Item2</DropdownItem>
          <DropdownItem onClick={this.toggle}>Item3</DropdownItem>
        </DropdownMenu>
      </Dropdown>
    );
  }
}