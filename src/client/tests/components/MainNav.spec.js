/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
/* global beforeEach, describe, expect, test */
import MainNav, {MainNavItem, MainNavSection} from '../../components/MainNav';
import {MemoryRouter} from 'react-router-dom';
import React from 'react';
import renderer from 'react-test-renderer';

describe('MainNav', () => {
  const items = [
    {
      "name": "Top-level",
      "subcategories": [{"name": "Second-level", "objects": [["Thieves"], ["Nobles"]]}],
      "objects": []
    }
  ];

  test('matches snapshot', () => {
    const currentSnapshot = renderer.create(
        <MemoryRouter>
          <MainNav items={items}/>
        </MemoryRouter>
    ).toJSON();
    expect(currentSnapshot).toMatchSnapshot();
  });
});
