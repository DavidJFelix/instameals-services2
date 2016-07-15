var React = require('react');

var Footer = require('./Footer');
var Header = require('./Header');
var LocationSetter = require('./LocationSetter');
var MealList = require('./MealList');

var Home = React.createClass({
    render: function () {
        var meals = [
            {
                name: "Chicken Pot Pie",
                description: "Delicious"
            },
            {
                name: "Dumplings",
                description: "Delicious"
            },
            {
                name: "Brown Rice",
                description: "Delicious"
            },
            {
                name: "Meatloaf",
                description: "Delicious"

            }
        ];

        return (
            <div>
                <Header></Header>
                <LocationSetter></LocationSetter>
                <MealList meals={meals}></MealList>
                <Footer></Footer>
            </div>
        )
    }
});

module.exports = Home;