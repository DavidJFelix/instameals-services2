var React = require('react');

var MealListItem = React.createClass({
    propTypes: {
        meal: React.PropTypes.object.isRequired
    },

    render: function() {
        return (
            <div>
                <img src=""/>
                <h4>{this.props.meal.name}</h4>
                <p>{this.props.meal.description}</p>
            </div>
        )
    }
});

module.exports = MealListItem;
