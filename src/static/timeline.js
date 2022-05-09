
function showTimeline() {
  var start = document.getElementById("start").value;
  var end = document.getElementById("end").value;

  console.log(start);

  // error handling
  if (start > end) {
    alert("Start date must be before end date");
    return;
  }

  let startDiv = $("<div>").addClass("container left").addClass("content");
  //.on("click", function() {

  //   alert("clicked");

  // } );

$("#contentLeft").append(startDiv);

if (start < 0) {
  $( ".content" ).append("<h2>" + Math.abs(start) + " BCE </h2>").append("<p>" + start + "</p>");
}
else {
  $( ".content" ).append("<h2>" + start + " CE </h2>").append("<p>" + start + "</p>");
}

// end date
let endDiv = $("<div>").addClass("container right").addClass("content");
$("#contentLeft").append(endDiv);


if (end < 0) {
  $( ".content" ).append("<h2>" + Math.abs(end) + " BCE </h2>").append("<p>" + end + "</p>");
}
else {
  $( ".content" ).append("<h2>" + end + " CE </h2>").append("<p>" + end + "</p>");
}


  //$("#timeline").addClass("container left").addClass("content").html(start);


}
