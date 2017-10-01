/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import MutableInstance from './MutableInstance';
import PropTypes from 'prop-types';
import React, {Component} from 'react';
import {Table} from 'reactstrap';

class OutputTable extends Component {
  constructor(props) {
    super(props);

    this.state = {properties: {}};
  }

  componentWillMount() {
    this._update(this.props.fetchPromise, this.props.match.params.slug);
  }

  componentWillReceiveProps(nextProps) {
    this._update(nextProps.fetchPromise, nextProps.match.params.slug);
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
    const items = Object.keys(this.state.properties).map((key, index) => {
      return this.renderSingleCell(index, key, this.state.properties[key])
    });
    return (<tbody>{items}</tbody>);
  }

  renderSingleCell(key, labelText, value) {
    return (<tr key={key}><th>{labelText}</th><td><MutableInstance label={value}/></td></tr>);
  }

  render() {
    const itemCount = Object.keys(this.state.properties).length;
    return (
        <Table inverse>
          {itemCount === 0 ? this.renderEmpty() : this.renderWithData()}
        </Table>
    );
  }

  _update(fetchPromise, slug) {
    fetchPromise(slug).then((json) => {
        this.setState({properties: json.objects[0]});
    });
  }
}

OutputTable.propTypes = {
  fetchPromise: PropTypes.func.isRequired
};

export default OutputTable;
