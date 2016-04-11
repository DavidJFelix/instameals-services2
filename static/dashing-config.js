/* global Dashboard */

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

dashboard.addWidget('meal_widget', 'Number', {
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
    getData: function () {
        var self = this;
        Dashing.utils.get('order_widget', function(data) {
            $.extend(self.scope, data);
        });
    },
    interval: 5000
});