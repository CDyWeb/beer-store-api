var beerApp = angular.module('beerApp', ['google-maps']).config(['$interpolateProvider', function ($interpolateProvider) { 
    $interpolateProvider.startSymbol('[['); 
    $interpolateProvider.endSymbol(']]'); 
}]); 

var controllers = {};


controllers.BeerMapController = function($scope, $http, $location) {

    $scope.locations = [];

    $scope.filterCity = function() {
            $http.jsonp('http://ontariobeerapi.ca/stores?city='+$scope.city+'&format=jsonp&callback=JSON_CALLBACK').success(function(data) {
            $scope.locations = data;
        });
    };
};

controllers.BeerInventoryController = function($scope, $http, $location) {

    $scope.locations = [];
    $scope.products = [];

    $http.jsonp('http://ontariobeerapi.ca/stores?format=jsonp&callback=JSON_CALLBACK').success(function(data) {
        $scope.locations = data;
    });
    
    $scope.updateStore = function() {
            $http.jsonp('http://ontariobeerapi.ca/stores/'+$scope.selectedStore.store_id+'/products?callback=JSON_CALLBACK').success(function(data) {
            $scope.products = data;
        });
    };
};

// register controllers
beerApp.controller(controllers);
