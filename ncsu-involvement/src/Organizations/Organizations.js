import React, { useEffect, useState } from "react";
import { OrgInfo } from "../OrgInfo/OrgInfo";

import "../Home/Home.css";

export function Organizations() {
    const [search, setSearch] = useState("");
    const [relevantOrgs___, setRelevantOrgs] = useState([]);

    function getOrgs(search) {
        fetch(`/organizations/${search}`)
            .then(res => res.json())
            .then(events => setRelevantOrgs(events));
    }
    // useEffect(() => {
    //     getEvents("");
    // });

    const relevantOrgs = [
        {
            name: "Aerial Robotics Club at NC State",
            orgurl: "https://getinvolved.ncsu.edu/organization/arc",
            imgurl: "https://se-infra-imageserver2.azureedge.net/clink/images/e9d963ae-9adf-439d-bf3a-bb9c6d3edd724e013b38-fb59-4487-8cfa-070cd04c89a1.jpg?preset=med-sq",
            category: "Academic & Pre-Professional",
            tags: ["Technology", "Aerospace"]
        },
        {
            name: "Accounting Society at NC State",
            orgurl: "https://getinvolved.ncsu.edu/organization/accsocietyncsu",
            imgurl: "https://se-infra-imageserver2.azureedge.net/clink/images/c3681c47-c495-40d9-bea5-b82396c59ce9721344f5-6f95-47fa-ac07-c8bdefba4a86.png?preset=med-sq",
            category: "Academic & Pre-Professional",
            tags: ["Accounting", "Business"]
        },
        {
            name: "Aerial Robotics Club at NC State2",
            orgurl: "https://getinvolved.ncsu.edu/organization/arc",
            imgurl: "https://se-infra-imageserver2.azureedge.net/clink/images/e9d963ae-9adf-439d-bf3a-bb9c6d3edd724e013b38-fb59-4487-8cfa-070cd04c89a1.jpg?preset=med-sq",
            category: "Academic & Pre-Professional",
            tags: ["Technology", "Aerospace"]
        },
        {
            name: "Accounting Society at NC State2",
            orgurl: "https://getinvolved.ncsu.edu/organization/accsocietyncsu",
            imgurl: "https://se-infra-imageserver2.azureedge.net/clink/images/c3681c47-c495-40d9-bea5-b82396c59ce9721344f5-6f95-47fa-ac07-c8bdefba4a86.png?preset=med-sq",
            category: "Academic & Pre-Professional",
            tags: ["Accounting", "Business"]
        },
        {
            name: "Aerial Robotics Club at NC State3",
            orgurl: "https://getinvolved.ncsu.edu/organization/arc",
            imgurl: "https://se-infra-imageserver2.azureedge.net/clink/images/e9d963ae-9adf-439d-bf3a-bb9c6d3edd724e013b38-fb59-4487-8cfa-070cd04c89a1.jpg?preset=med-sq",
            category: "Academic & Pre-Professional",
            tags: ["Technology", "Aerospace"]
        },
        {
            name: "Accounting Society at NC State3",
            orgurl: "https://getinvolved.ncsu.edu/organization/accsocietyncsu",
            imgurl: "https://se-infra-imageserver2.azureedge.net/clink/images/c3681c47-c495-40d9-bea5-b82396c59ce9721344f5-6f95-47fa-ac07-c8bdefba4a86.png?preset=med-sq",
            category: "Academic & Pre-Professional",
            tags: ["Accounting", "Business"]
        }
    ];

    function handleSearch() {
        getOrgs(search);
        setSearch("")
    }

    return (
        <React.Fragment>
            <input type="text" placeholder="Search by keyword(s)" value={search} onChange={e => setSearch(e.target.value)} />
            <button style={{marginLeft: "10px"}} onClick={handleSearch}>Search</button>
            
            <h2>{search.length === 0 ? "All Events" : "Relevant Events"}</h2>
            <div className="flex-area">
                {relevantOrgs.length === 0 ?
                    "No organizations found matching criteria" :
                    relevantOrgs.map(org => <OrgInfo key={org.name} {...org} />)
                }
            </div>
        </React.Fragment>
    );
}