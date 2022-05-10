// Upload file
$(document).on("click", "#btnUploadFile", function () {
  if ($("#fileToUpload").get(0).files.length == 0) {
    alert("Please upload the file first.");
    return;
  }
  let fileUpload = $("#fileToUpload").get(0);
  let files = fileUpload.files;
  if (files[0].name.toLowerCase().lastIndexOf(".csv") == -1) {
    alert("Please upload only CSV files");
    return;
  }

  alert("Document uploaded successfully");

  data = files[0];
  console.log(data);

  let form = new FormData();
  form.append("data", data);

  fetch("/upload", {
    method: "POST",
    body: form,
  }).then((response) => {
    console.log("File upload response: ", response);
  });
});
