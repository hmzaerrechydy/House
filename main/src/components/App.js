import React, { useState, Component } from "react";
import { render } from "react-dom";
import Table from "./Table";


export default function App() {
    const items = require('../../../db.json');
    const [query, setQuery] = useState("");
    const keys = ["title", "url", "type", "topic", "author"];
    const search = (data) => {
      return data.filter((item) =>
        keys.some((key) => item[key].toLowerCase().includes(query))
      );
   };
    return (
        <div className="mx-auto w-50" id="content">
          <div className="text-justify">
            <h1 className="text-center">The House of Wisdom</h1>
            <p id="about">
            The House of Wisdom, also known as the Grand Library of Baghdad, was a major Abbasid public academy and intellectual center in Baghdad and one of the world's largest public libraries during the Islamic Golden Age. 
            <b><a href="https://en.wikipedia.org/wiki/House_of_Wisdom" target="_blank"> Learn more. </a></b>
             This website tries to imitate The House of Wisdom by curating the best content on the internet in one place. 
             Anyone can add content by clicking the <b>Add</b> button below.
            </p>

            <div class="input-group mx-auto">
              <input type="search" className="form-control rounded" placeholder="Search" aria-label="Search" aria-describedby="search-addon" onChange={(e) => setQuery(e.target.value.toLowerCase())}/>
              
              <a href="add/" id="add"><button type="button" className="btn btn-light">Add</button></a>
            </div>

          </div>
          <br></br>
          <div class="table-responsive">
            {<Table data={search(items)} />}
          </div>
        </div>
    );
}


const appDiv = document.getElementById("app");
render(<App />, appDiv);