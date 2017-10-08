/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import {Dropdown, DropdownItem, DropdownMenu, DropdownToggle} from 'reactstrap';
import PropTypes from 'prop-types';
import React, {Component} from 'react';

/*
 * May not be the best name.
 */
export default class MutableInstance extends Component {
  static propTypes = {
    items: PropTypes.array.isRequired,
    onSelect: PropTypes.func.isRequired,
    selectId: PropTypes.string.isRequired
  };

  constructor(props) {
    super(props);

    this.state = {open: false};
  }

  _select = (e) => {
    this.props.onSelect(this.props.selectId, e.target.textContent);
    this.toggleOpen();
  };

  toggleOpen = () => {
    this.setState({open: !this.state.open});
  };

  render() {
    const {items} = this.props;
    return (
      <Dropdown isOpen={this.state.open} tag='span' toggle={this.toggleOpen}>
        <DropdownToggle tag="span" caret>
          {this.props.label}
        </DropdownToggle>
        <DropdownMenu>
          {items.map((item, index) => <DropdownItem key={index} onClick={this._select}>{item}</DropdownItem>)}
        </DropdownMenu>
      </Dropdown>
    );
  }
}