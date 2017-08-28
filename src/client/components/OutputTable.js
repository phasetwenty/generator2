/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import React, {Component, PropTypes} from 'react';
import {Table} from 'reactstrap';

class OutputTable extends Component {
  constructor(props) {
    super(props)
  }

  render() {
    return (
      <Table inverse>
        <tbody>
          <tr>
            <th>Name</th>
            <td>Horse</td>
          </tr>
          <tr>
            <th>Sex</th>
            <td>Male</td>
          </tr>
          <tr>
            <th>Race</th>
            <td>Human</td>
          </tr>
          <tr>
            <th>Class</th>
            <td>Horse</td>
          </tr>
          <tr>
            <th>Description</th>
            <td>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce faucibus nunc massa, et tempus tortor
              rhoncus eget. Aenean volutpat.
            </td>
          </tr>
          <tr>
            <th>Extra</th>
            <td>Lorem ipsum dolor sit amet, consectetur adipiscing metus.</td>
          </tr>
        </tbody>
      </Table>
    );
  }
}

OutputTable.propTypes = {};

export default OutputTable;
