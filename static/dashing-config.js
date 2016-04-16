/* global Dashboard */

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock', {
    color: 'orange'
});

dashboard.addWidget('meal_widget', 'Number', {
    color: 'orange',
    getData: function () {
        var self = this;
        Dashing.utils.get('meal_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 5000
});

dashboard.addWidget('user_widget', 'Number', {
    getData: function () {
        var self = this;
        Dashing.utils.get('user_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 5000
});

dashboard.addWidget('order_widget', 'Number', {
    color: 'steelblue',
    getData: function () {
        var self = this;
        Dashing.utils.get('order_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 5000
});

dashboard.addWidget('avg_meal_price_widget', 'Number', {
    getData: function () {
        var self = this;
        Dashing.utils.get('avg_meal_price_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 5000
});

