import React, { useState, useEffect } from "react";

import { EventInfo } from "../EventInfo/EventInfo";

import "../Home/Home.css";

export function Events() {
    const [search, setSearch] = useState("");
    const [relevantEvents, setRelevantEvents] = useState([]);

    function getEvents(search) {
        fetch(search === "" ? "/searchEventsAll" : `/searchEvents/${search}`)
            .then(res => res.json())
            .then(events => setRelevantEvents(events.data));
    }
    // get all of the events with search string "" when page gets here
    useEffect(() => {
        getEvents("");
    }, []);

    function handleSearch() {
        getEvents(search);
        setSearch("")
    }

    return (
        <React.Fragment>
            <input type="text" placeholder="Search by keyword(s)" value={search} onChange={e => setSearch(e.target.value)} />
            <button style={{marginLeft: "10px"}} onClick={handleSearch}>Search</button>
            
            <h2>{search.length === 0 ? "All Events" : "Relevant Events"}</h2>
            <div className="flex-area">
                {relevantEvents.length === 0 ?
                    "No events found matching criteria" :
                    relevantEvents.map(e => <EventInfo key={e.name} {...e} />)
                }
            </div>
        </React.Fragment>
    );
}