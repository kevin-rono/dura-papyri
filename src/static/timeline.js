function showTimeline() {
  var start = document.getElementById("start").value;
  var end = document.getElementById("end").value;

  //   console.log(start);

  // error handling
  if (start > end) {
    alert("Start date must be before end date");
    return;
  }

  // fetch data
  $(document).on("click", "#timelineDisplay", () => {
    let form = new FormData();
    form.append("start", start);
    form.append("end", end);

    fetch("/show_timeline", {
      method: "POST",
      body: form,
    })
      .then((response) => response.json())
      .then((data) => {
        data = data.data;
        console.log(data);

        ids = [];

        for (let i = 0; i < data.length; i++) {
          papyrus = data[i];
          id = papyrus["ID"];
          ids.push(id);
          publication = papyrus["Publication"];
          start_date = papyrus["start"];
          end_date = papyrus["end"];

          if (i % 2 == 0) {
            // left
            let leftDiv = $(`<div id=papyrus${id}>`)
              .addClass("container left")
              .addClass("content");

            $(".timeline").append(leftDiv);

            if (start_date < 0) {
              $(`#papyrus${id}`)
                .append("<h4>" + publication + "</h4>")
                .append(
                  "<p>" + "Start Date: " + Math.abs(start_date) + " BCE </p>"
                );
              if (end_date < 0) {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + Math.abs(end_date) + " BCE </p>"
                );
              } else {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + end_date + " CE </p>"
                );
              }
            } else {
              $(`#papyrus${id}`)
                .append("<h4>" + publication + "</h4>")
                .append("<p>" + "Start Date: " + start_date + " CE </p>");
              if (end_date < 0) {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + Math.abs(end_date) + " BCE </p>"
                );
              } else {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + end_date + " CE </p>"
                );
              }
            }
          } else {
            // right
            let rightDiv = $(`<div id=papyrus${id}>`)
              .addClass("container right")
              .addClass("content");

            $(".timeline").append(rightDiv);

            if (start_date < 0) {
              $(`#papyrus${id}`)
                .append("<h4>" + publication + "</h4>")
                .append(
                  "<p>" + "Start Date: " + Math.abs(start_date) + " BCE </p>"
                );
              if (end_date < 0) {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + Math.abs(end_date) + " BCE </p>"
                );
              } else {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + end_date + " CE </p>"
                );
              }
            } else {
              $(`#papyrus${id}`)
                .append("<h4>" + publication + "</h4>")
                .append("<p>" + "Start Date: " + start_date + " CE </p>");
              if (end_date < 0) {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + Math.abs(end_date) + " BCE </p>"
                );
              } else {
                $(`#papyrus${id}`).append(
                  "<p>" + "End Date: " + end_date + " CE </p>"
                );
              }
            }
          }
        }

        for (let i = 0; i < ids.length; i++) {
          papyrus = document.getElementById(`papyrus${ids[i]}`);
          // console.log(papyrus);
          papyrus.addEventListener("click", () => {
            localStorage.setItem("ID", ids[i]);
            localStorage.setItem("map", "no");
            console.log(localStorage.getItem("ID"));
            window.open("../results", "_blank").focus();
          });
        }
      });
  });
}
