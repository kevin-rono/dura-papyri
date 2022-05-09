
$("#image").click(function (e) {
  alert(
    "No papyri found in this area of Dura-Europos; click a colored area to explore!"
  );
});

<<<<<<< HEAD
// for each id in map
// create fetch, passing the the value of the id in locations
// example: L7 -> locations[L7]
// response -> data
// attach data to results.html

function populateResults(id) {
  // let test = $("<div>").html("test");
  // $("#test").append(test);

  $("#test").html("test");

  console.log(id);

  fetch("/display_results", {
    method: "GET",
  })
    .then((response) => response.json())
    .then((data) => {
      data = locations[id];
      console.log(data);
    });
}
=======
function storeLocation(location) {
  localStorage.setItem('location', location);
  console.log(localStorage.getItem('location'));

}


>>>>>>> 24e75e3779b568f5e6cb193cf339128e16b20e92
