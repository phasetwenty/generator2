/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import {Link} from 'react-router-dom';
import {Nav, NavItem} from 'reactstrap';
import PropTypes from 'prop-types';
import React from 'react';

const MainNav = (props) => {
  return (
    <Nav vertical>
      {
        props.items.map((item, index) => {
          return (
            <div key={index}>
              {renderItem(item, index, 1)}
              {item.subcategories.map((item, index) => renderItem(item, index, 2))}
            </div>
          );
        })
      }
    </Nav>
  );
};

MainNav.propTypes = {
  items: PropTypes.array.isRequired
};

function renderItem(item, key, depth) {
  const offsetClass = `ml-${depth}`;
  const itemOffsetClass = `ml-${depth + 1}`;
  return (
    <div key={key}>
      <MainNavSection key={key} offsetClass={offsetClass} text={item.name}/>
      {
        item.objects.map((pair, index) => {
          return <MainNavItem key={index} offsetClass={itemOffsetClass} target={`/${pair[1]}`} text={pair[0]}/>;
        })
      }
    </div>
  );
}


const MainNavSection = (props) => {
  return <NavItem className={props.offsetClass}>{props.text}</NavItem>;
};

MainNavSection.propTypes = {
  offsetClass: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired
};

const MainNavItem = (props) => {
  const {offsetClass, target, text} = props;
  return <NavItem className={offsetClass}><Link to={target}>{text}</Link></NavItem>;
};

MainNavItem.propTypes = {
  offsetClass: PropTypes.string.isRequired,
  target: PropTypes.string.isRequired,
  text: PropTypes.string.isRequired
};

export default MainNav;
