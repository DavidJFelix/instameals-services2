var React = require('react');
var ReactDom = require('react-dom');


var Main = React.creatClass({
  render: function() {
    return (
      <div>Hello World</div>
    )
  }
});

ReactDom.render(<Main />, document.getElementById('app'))

