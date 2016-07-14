var React = require('react');

var Footer = require('./Footer');
var Header = require('./Header');
var LocationSetter = require('./LocationSetter');
var MealList = require('./MealList');

var Home = React.createClass({
    render: function () {
        var meals = ["stuff", "duh", "pretty", "dope"];

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