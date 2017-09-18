/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import {Link} from 'react-router-dom';
import {Nav, NavItem} from 'reactstrap';
import PropTypes from 'prop-types';
import React, {Component} from 'react';

class MainNav extends Component {
  renderAllItems() {
    return this.props.items.map((item, index) => {
      return (
        <div key={index}>
          <MainNavSection key={index} offsetClass="ml-1" text={item.name}/>
          {
            item.subcategories.map((subcategoryItem, subcategoryIndex) => {
              return (
                  <div key={subcategoryIndex}>
                    <MainNavSection offsetClass="ml-2" text={subcategoryItem.name}/>
                    {subcategoryItem.items.map((itemPair, index) => {
                      return <MainNavItem key={index} target={`/${itemPair[1]}`} text={itemPair[0]}/>
                    })}
                  </div>
              );
            })
          }
        </div>
      );
    });
  }

  render() {
    return (
      <Nav vertical>
        {this.renderAllItems()}
      </Nav>
    );
  }
}

MainNav.propTypes = {
  items: PropTypes.array.isRequired
};

export const MainNavSection = (props) => {
  return <NavItem className={props.offsetClass}>{props.text}</NavItem>;
};

MainNavSection.propTypes = {
  offsetClass: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired
};

export const MainNavItem = (props) => {
  return <NavItem className="ml-3"><Link to={props.target}>{props.text}</Link></NavItem>;
};

MainNavItem.propTypes = {
  target: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired
};

export default MainNav;
