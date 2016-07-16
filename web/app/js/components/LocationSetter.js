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
            <div className="jumbotron jumbotron-fluid bg-primary">
                <div className="container">
                    <div className="row">
                        <div className="col-xl-3"></div>
                        <div className="input-group col-xl-6">
                            <input
                                className="form-control"
                                placeholder="Where are you looking for food?"
                                onChange={this.handleChange}
                                value={this.state.value}
                            />
                        </div>
                        <div className="col-xl-3"></div>
                    </div>
                </div>
            </div>
        )
    }
});

module.exports = LocationSetter;
