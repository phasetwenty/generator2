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

    this.state = {fields: []};
  }

  componentWillMount() {
    fetch('http://localhost:8080/api/v1/test')
      .then((response) => {
        return response.json();
      }).then((json) => {
        this.setState({fields: json});
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
    const items = this.state.fields.map((pair, index) => { return this.renderSingleCell(index, ...pair); });
    return (<tbody>{items}</tbody>);
  }

  renderSingleCell(key, labelText, value) {
    return (<tr key={key}><th>{labelText}</th><td>{value}</td></tr>);
  }

  render() {
    return (
        <Table inverse>
          {this.state.fields.length === 0 ? this.renderEmpty() : this.renderWithData()}
        </Table>
    );
  }
}

OutputTable.propTypes = {};

export default OutputTable;
