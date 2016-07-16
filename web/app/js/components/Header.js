var React = require('react');

var Header = React.createClass({
    render: function() {
        return (
            <nav className="navbar">
                <a className="navbar-brand">Instameals</a>
            </nav>
        )
    }
});

module.exports = Header;
