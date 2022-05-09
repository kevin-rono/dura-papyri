$("#image").click(function (e) {
  alert(
    "No papyri found in this area of Dura-Europos; click a colored area to explore!"
  );
});

function storeLocation(location) {
  localStorage.setItem("location", location);
  localStorage.setItem("map", "yes");
  console.log(localStorage.getItem("location"));
}
