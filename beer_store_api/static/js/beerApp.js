var beerApp = angular.module('beerApp', ['google-maps']).config(['$interpolateProvider', function ($interpolateProvider) { 
    $interpolateProvider.startSymbol('[['); 
    $interpolateProvider.endSymbol(']]'); 
}]); 

var controllers = {};


controllers.BeerMapController = function($scope, $http, $location) {

    $scope.locations = [];

    /*$http.jsonp('http://127.0.0.1:8000/stores?callback=JSON_CALLBACK').success(function(data) {
        $scope.locations = data;
    });*/

    $scope.filterCity = function() {
            $http.jsonp('http://127.0.0.1:8000/stores?city='+$scope.city+'&callback=JSON_CALLBACK').success(function(data) {
            $scope.locations = data;
        });
    };
};

controllers.BeerInventoryController = function($scope, $http, $location) {

    $scope.locations = [];
    $scope.products = [];

    $http.jsonp('http://127.0.0.1:8000/stores?callback=JSON_CALLBACK').success(function(data) {
        $scope.locations = data;
    });
    
    $scope.updateStore = function() {
            $http.jsonp('http://127.0.0.1:8000/stores/'+$scope.selectedStore.store_id+'/products?callback=JSON_CALLBACK').success(function(data) {
            $scope.products = data;
        });
    };
};

// register controllers
beerApp.controller(controllers);
