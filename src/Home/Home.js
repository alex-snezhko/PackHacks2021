import React, { useState, useEffect } from "react";

import { OrgInfo } from "../OrgInfo/OrgInfo";
import { EventInfo } from "../EventInfo/EventInfo";

import "./Home.css"

export function Home({ userLoggedIn }) {
    const [recommendedOrgs, setRecommendedOrgs] = useState([]);
    const [recommendedEvents, setRecommendedEvents] = useState([]);

    useEffect(() => {
        fetch(`/recommendedOrganizations/${userLoggedIn}`,
        {
            headers: { "Access-Control-Allow-Origin": "http://localhost:3000" }
        })
            .then(res => res.json())
            .then(orgs => setRecommendedOrgs(orgs.data));

        fetch(`/recommendedOrganizations/${userLoggedIn}`)
            .then(res => res.json())
            .then(events => setRecommendedEvents(events.data));
    }, []);



    // const recommendedOrgs = await fetch("/recommended-orgs").then(res => res.json());
    return (
        <React.Fragment>
            <h2><span style={{color: "#c00"}}>Organizations</span> You May Be Interested In</h2>
            <hr />
            <div className="flex-area">
                {recommendedOrgs.map(org => <OrgInfo key={org.name} {...org} />)}
            </div>
            <h2><span style={{color: "#c00"}}>Upcoming Events</span> You May Be Interested In</h2>
            <hr />
            <div className="flex-area">
                {recommendedEvents.map(event => <EventInfo key={event.name} {...event} />)}
            </div>
        </React.Fragment>
    );
}
