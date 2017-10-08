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

    this.state = {
      properties: [],
      selections: {}
    };
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
    const items = this.state.properties.map((property, index) => this.renderSingleCell(index, property));
    return (<tbody>{items}</tbody>);
  }

  renderSingleCell(key, property) {
    const selectId = property.label;
    const selection = this.state.selections[selectId];
    return (
        <tr key={key}>
          <th>{property.label}</th>
          <td>
            <MutableInstance label={selection} items={property.instances} onSelect={this._onSelect} selectId={selectId}/>
          </td>
        </tr>
    );
  }

  render() {
    const itemCount = this.state.properties.length;
    return (
        <Table inverse>
          {itemCount === 0 ? this.renderEmpty() : this.renderWithData()}
        </Table>
    );
  }

  _onSelect = (propertyLabel, instanceValue) => {
    const newSelections = Object.assign({}, this.state.selections, {[propertyLabel]: instanceValue});
    this.setState({selections: newSelections});
  };

  _update(fetchPromise, slug) {
    fetchPromise(slug).then((json) => {
        const properties = json.objects[0].properties;
        const selections = {};
        properties.forEach((property) => {
          selections[property.label] = property.instances[0];
        });

        this.setState({properties, selections});
    });
  }
}

OutputTable.propTypes = {
  fetchPromise: PropTypes.func.isRequired
};

export default OutputTable;
