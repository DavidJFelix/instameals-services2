module.exports = {
  entry: "./web/app/js/App.js",

  output: {
    filename: "./web/static/app.js"
  },

  module: {
    loaders: [
      {
        test: /\.jsx?$/,
        exclude: /(node_modules|bower_components)/,
        loader: 'babel',
        query: {
          presets: ['react', 'es2015',]
        }
      }
    ]
  }
};
