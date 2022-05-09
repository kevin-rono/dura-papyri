// location dictionary based on Findspots
const locations = {
  L7: "Block L7",
  L8: "Block L8",
  "L7-L8": "Blocks L7",
  "T. 22": "Tower 22",
  "Wall along T. 3": "Tower 3",
  "N MG": "Northeast Tower of the Main Gate",
  "No location": ["Not available", "Unclear", "Unknown"],
  "E7 W13": "Azzanathkona",
  "South MG": "Southwest",
  J9: "Temple of Bel",
  "T. 19": "Tower 19",
  "T. 2": "Tower 2",
  "Wall MG": "Wall Street near the Main Gate",
};

window.onload = function () {
  let location = localStorage.getItem("location");
  console.log(location);

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
      console.log(data);

      for (let i = 0; i < data.length; i++) {
        // declare first of the entries
        let entry = data[i];

        // store values of each category
        let id = entry["ID"];
        let publication = entry["Publication"];
        let relation = entry["Relation"];
        let language = entry["Language"];
        let date = entry["Date"];
        let provenance = entry["Provenance"];
        let findspot = entry["Findspot"];
        let season = entry["Season"];
        let wikidata = entry["Wikidata_ID"];
        let content = entry["content"];
        let name = entry["name"];
        let subject = entry["subject"];
        let start = entry["start"];
        let end = entry["end"];
        let material = entry["material"];
        let origin = entry["origin"];

<<<<<<< HEAD
          // add values into graph 
          let table = document.getElementById("resultsTable");
          let row = table.insertRow(-1);
=======
        let table = document.getElementById("resultsTable");
        let row = table.insertRow(-1);

        let cell_id = row.insertCell(-1);
        cell_id.innerHTML = id;
>>>>>>> d1e0a608678c336559159da5118db31118addd72

        let cell_publication = row.insertCell(-1);
        cell_publication.innerHTML = publication;

        let cell_relation = row.insertCell(-1);
        cell_relation.innerHTML = relation;

        let cell_language = row.insertCell(-1);
        cell_language.innerHTML = language;

        let cell_date = row.insertCell(-1);
        cell_date.innerHTML = date;

        let cell_provenance = row.insertCell(-1);
        cell_provenance.innerHTML = provenance;

        let cell_findspot = row.insertCell(-1);
        cell_findspot.innerHTML = findspot;

        let cell_season = row.insertCell(-1);
        cell_season.innerHTML = season;

        let cell_wikidata = row.insertCell(-1);
        cell_wikidata.innerHTML = wikidata;

        let cell_content = row.insertCell(-1);
        cell_content.innerHTML = content;

        let cell_name = row.insertCell(-1);
        cell_name.innerHTML = name;

        let cell_subject = row.insertCell(-1);
        cell_subject.innerHTML = subject;

        let cell_start = row.insertCell(-1);
        cell_start.innerHTML = start;

        let cell_end = row.insertCell(-1);
        cell_end.innerHTML = end;

<<<<<<< HEAD
      }

  });
  
  }

=======
        let cell_material = row.insertCell(-1);
        cell_material.innerHTML = material;

        let cell_origin = row.insertCell(-1);
        cell_origin.innerHTML = origin;
      }
    });
};
>>>>>>> d1e0a608678c336559159da5118db31118addd72
