$("#image").click(function (e) {
  let x = e.pageX - this.offsetLeft;
  let y = e.pageY - this.offsetTop;

  alert("coordinates: " + x + ", " + y);
});
