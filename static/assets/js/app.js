angular.module("myApp.controllers", []);
angular.module("myApp.models", []);
var myApp = angular.module("myApp", [
  "ui.router",
  "myApp.controllers",
  "myApp.models"
]);

// configure our routes
myApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to /state1
  $urlRouterProvider.otherwise("/");
  //
  // Now set up the states
  $stateProvider
    .state("home", {
      url: "/",
      templateUrl: "partials/home.html"
    })

    .state("event", {
      url: "/event-tickets",
      templateUrl: "partials/event.html"
    })

    .state("singleEvent", {
      url: "/event",
      templateUrl: "partials/single-event.html"
    })

    .state("movies", {
      url: "/movies-tickets",
      templateUrl: "partials/movies.html"
    })

    .state("BuyAdeal", {
      url: "/buy-a-deal",
      templateUrl: "partials/buy-a-deal.html"
    })

    .state("BookAtalent", {
      url: "/book-a-talent",
      templateUrl: "partials/book-a-talent.html"
    })

    .state("CreateEvent", {
      url: "/create-event",
      templateUrl: "partials/create-event.html"
    })

    .state("error", {
      url: "/error",
      templateUrl: "404.html"
    });
});
