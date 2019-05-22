'use strict';
var app = angular.module('myApp.controllers');

app.controller('generalController', function($scope, $location) {
	
	$scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
});