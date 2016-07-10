var React = require('react');

var Footer = require('./Footer');
var Header = require('./Header');
var LocationSetter = require('./LocationSetter');
var MealList = require('./MealList');

var Home = React.createClass({
    render: function () {
        return (
            <div>
                <Header></Header>
                <LocationSetter></LocationSetter>
                <MealList></MealList>
                <Footer></Footer>
            </div>
        )
    }
});

module.exports = Home;