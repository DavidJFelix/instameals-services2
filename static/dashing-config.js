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