var React = require('react');

var MealListItem = require('./MealListItem');

var MealList = React.createClass({
    propTypes: {
        meals: React.PropTypes.array.isRequired
    },

    render: function () {
        return (
            <ul>{
                this.props.meals.map(
                    function (meal, index) {
                        return <MealListItem
                            key={index}
                            meal={meal}
                        />;
                    }
                )
            }</ul>
        )
    }
});

module.exports = MealList;
