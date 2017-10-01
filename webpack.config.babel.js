/**
 * Copyright 2017 Christopher Haverman
 * All Rights Reserved
 **/
import fs from 'fs';
import path from 'path';
import {ProvidePlugin} from 'webpack';
import HtmlWebpackPlugin from 'html-webpack-plugin';

function readInitialProps() {
  return fs.readFileSync('initialprops.json', 'utf8').trim();
}

export default {
  //the base directory (absolute path) for resolving the entry option
  context: __dirname,
  //the entry point we created earlier. Note that './' means
  //your current directory. You don't have to specify the extension  now,
  //because you will specify extensions later in the `resolve` section
  entry: './src/client/index',

  devtool: 'inline-source-map',
  devServer: {contentBase: './bundle'},

  output: {
    //where you want your compiled bundle to be stored
    path: path.resolve('./bundle/'),
    //naming convention webpack should use for your files
    filename: '[name]-[hash].js',
  },

  plugins: [
    new HtmlWebpackPlugin({
      initialProps: readInitialProps(),
      title: 'horse',
      template: 'src/server/generator2/templates/home.html.ejs'
    }),
    new ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery',
      Popper: ['popper.js', 'default']
    }),
  ],

  module: {
    loaders: [
      //a regexp that tells webpack use the following loaders on all
      //.js and .jsx files
      {
        test: /\.jsx?$/,
        //we definitely don't want babel to transpile all the files in
        //node_modules. That would take a long time.
        exclude: /node_modules/,
        //use the babel loader
        loader: 'babel-loader',
        query: {
          //specify that we will be dealing with React code
          presets: ['react']
        }
      },
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },

  resolve: {
    //tells webpack where to look for modules
    modules: ['node_modules'],
    //extensions that should be used to resolve modules
    extensions: ['.js', '.jsx']
  }
};
