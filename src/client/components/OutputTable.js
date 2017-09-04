/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import React, {Component, PropTypes} from 'react';
import {Table} from 'reactstrap';
import 'whatwg-fetch';

class OutputTable extends Component {
  constructor(props) {
    super(props);

    this.state = {};
  }

  componentWillMount() {
    fetch('http://localhost:8080/api/v1/random-object')
      .then((response) => {
        return response.json();
      }).then((json) => {
        this.setState(json);
      });
  }

  renderEmpty() {
    return (
        <tbody>
          <tr>
            <th>Name</th>
            <td/>
          </tr>
          <tr>
            <th>Sex</th>
            <td/>
          </tr>
          <tr>
            <th>Race</th>
            <td/>
          </tr>
          <tr>
            <th>Class</th>
            <td/>
          </tr>
          <tr>
            <th>Description</th>
            <td/>
          </tr>
          <tr>
            <th>Extra</th>
            <td/>
          </tr>
        </tbody>
    );
  }

  renderWithData() {
    const items = Object.keys(this.state).map((key, index) => {
      return this.renderSingleCell(index, key, this.state[key])
    });
    return (<tbody>{items}</tbody>);
  }

  renderSingleCell(key, labelText, value) {
    return (<tr key={key}><th>{labelText}</th><td>{value}</td></tr>);
  }

  render() {
    const itemCount = Object.keys(this.state).length;
    return (
        <Table inverse>
          {itemCount === 0 ? this.renderEmpty() : this.renderWithData()}
        </Table>
    );
  }
}

OutputTable.propTypes = {};

export default OutputTable;
