/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
/* global beforeEach, describe, expect, test */
import MainNav, {MainNavItem, MainNavSection} from '../../components/MainNav';
import React from 'react';
import {shallow} from 'enzyme';

describe('MainNav', () => {
  const items = [
    {
      "name": "Top-level",
      "subcategories": [{"name": "Second-level", "items": [["Thieves"], ["Nobles"]]}]
    }
  ];
  let componentUnderTest = null;

  beforeEach(() => {
    componentUnderTest = shallow(<MainNav items={items}/>);
  });

  test('renders the expected number of category sections.', () => {
    const categoryElements = componentUnderTest.find(MainNavSection);
    expect(categoryElements.length).toBe(2);
  });

  test('renders a category section.', () => {
    const categoryElement = componentUnderTest
      .find(MainNavSection)
      .findWhere(node => node.render().text() === 'Top-level');
    expect(categoryElement.length).toBe(1);
  });

  test('renders a subcategory section.', () => {
    const subcategoryElement = componentUnderTest
      .find(MainNavSection)
      .findWhere(node => node.render().text() === 'Second-level');
    expect(subcategoryElement.length).toBe(1);
  });

  test('renders the leaf nav items.', () => {
    const navItems = componentUnderTest.find(MainNavItem);

    const thievesItem = navItems.findWhere(node => node.render().text() === 'Thieves');
    expect(thievesItem.length).toBe(1);

    const noblesItem = navItems.findWhere(node => node.render().text() === 'Nobles');
    expect(noblesItem.length).toBe(1);
  });
});
