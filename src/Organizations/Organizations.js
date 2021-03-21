import React, { useEffect, useState } from "react";
import { OrgInfo } from "../OrgInfo/OrgInfo";

import "../Home/Home.css";

export function Organizations() {
    const [search, setSearch] = useState("");
    const [relevantOrgs, setRelevantOrgs] = useState([]);

    function getOrgs(search) {
        fetch(search === "" ? "/searchOrganizationsAll" : `/searchOrganizations/${search}`)
            .then(res => res.json())
            .then(events => setRelevantOrgs(events.data));
    }
    useEffect(() => {
        getOrgs("");
    }, []);

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