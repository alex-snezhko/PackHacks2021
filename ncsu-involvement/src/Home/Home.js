import React from "react";

import { OrgInfo } from "../OrgInfo/OrgInfo";
import { EventInfo } from "../EventInfo/EventInfo";

import "./Home.css"

export function Home(props) {
    const recommendedOrgs = [
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
        }
    ];

    const recommendedEvents = [
        {
            name: "8th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        }
    ];
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
