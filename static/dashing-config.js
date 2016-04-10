/* global Dashboard */

var dashboard = new Dashboard();

dashboard.addWidget('clock_widget', 'Clock');

dashboard.addWidget('meal_widget', 'Number', {
    getData: function () {
        var self = this;
        $.get('widgets/meal_widget/', function(data) {
            $.extend(self.data, data);
        });
    },
    interval: 5000
});