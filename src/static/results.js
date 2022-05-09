
// location dictionary based on Findspots
const locations = {
    L7: ["Along the Wall of the Synagogue", "Block L7", "Blocks L7"],
    L8: ["Block L8", "Blocks L7", "Block L7 or L8"],
    "L7-L8": ["Blocks L7", "Block L7 or L8"],
    "T. 22": "Tower 22",
    "Wall along T. 3": "Tower 3",
    "N MG": "Northeast Tower of the Main Gate",
    "No location": ["Not available", "Unclear", "Unknown"],
    "E7 W13": ["Temple of Artemis Azzanathkona", "Temple of Azzanathkona"],
    "South MG": "Southwest",
    J9: "Temple of Bel",
    "T. 19": "Tower 19",
    "T. 2": "Tower 2",
    "Wall MG": "Wall Street near the Main Gate",
  };


window.onload = function() {

    let location = localStorage.getItem('location');
    console.log(location);

    let table = document.getElementById("resultsTable");
    table.insertRow(-1);
    for (i = 0; i < 16; i++) {
        let cell1 = row.insertCell(0);
        cell1.innerHTML = "hello";
    }
    

    // $('#tbody').append("<tr>").addClass("align-middle").html("hello");



    // fetch locations
    let form = new FormData();
    form.append("location", locations[location]);

    fetch("/display_results", { 
      method: "POST", 
      body: form,
    })
    .then(response => response.json())
    .then(data => { 
      data = data.data;

    //   for (let i = 0; i < data.length; i++) {
    //       let entry = data[i];
    //       for (value in entry) {
    //         $('#tbody').append(<tr>);
    //       }
    //   }


  });
  
  }

