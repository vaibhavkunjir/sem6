var registrationApp = angular.module("registrationApp", []);
registrationApp.controller("registrationController", function($scope, $http) {
   $scope.submitForm = function() {
      var data = {
         "firstName": $scope.firstName,
         "lastName": $scope.lastName,
         "username": $scope.username,
         "password": $scope.password
      };
      $http.post("/register", data).then(function(response) {
         alert("Registration Successful");
      }, function(error) {
         alert("Registration Failed");
      });
   };
});
