define([
	"underscore",
	"backbone"
], function (_, Backbone) {
	var RouteModel;

	RouteModel = Backbone.Model.extend({
		idAttribute: "route_id",

	    initialize: function(){

        }
 	});

	return RouteModel;
})