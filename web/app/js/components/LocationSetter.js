var React = require('react');

var LocationSetter = React.createClass({
    getInitialState: function () {
        return {value: ''};
    },
    handleChange: function (event) {
        this.setState({value: event.target.value});
    },

    render: function () {
        return (
            <div className="input-group">
                <input
                    className="form-control"
                    placeholder="Enter A City"
                    onChange={this.handleChange}
                    value={this.state.value}
                />
            </div>
        )
    }
});

module.exports = LocationSetter;
