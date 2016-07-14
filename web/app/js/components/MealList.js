var React = require('react');

var MealListItem = require('./MealListItem');

var MealList = React.createClass({
    render: function() {
        return (
            <ul>
                {this.props.meals.map(function(meal) {
                    return <MealListItem key={meal} data={meal}/>;
                })}
            </ul>
        )
    }
});

module.exports = MealList;
