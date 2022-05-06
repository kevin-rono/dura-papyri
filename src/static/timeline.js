function showTimeline() {
  var start = document.getElementById("start").value;
  var end = document.getElementById("end").value;

  console.log(start);

  if (start > end) {
    alert("Start date must be before end date");
  }
}
