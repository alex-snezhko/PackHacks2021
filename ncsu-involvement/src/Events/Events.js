import React, { useState } from "react";

import { EventInfo } from "../EventInfo/EventInfo";

import "../Home/Home.css";

export function Events() {
    const [search, setSearch] = useState("");
    const [relevantEvents_____, setRelevantEvents] = useState([]);

    function getEvents(search) {
        fetch(`/events/${search}`)
            .then(res => res.json())
            .then(events => setRelevantEvents(events));
    }
    // useEffect(() => {
    //     getEvents("");
    // });

    const relevantEvents = [
        {
            name: "8th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        },
        {
            name: "9th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        },
        {
            name: "10th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        },
        {
            name: "11th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        },
        {
            name: "12th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        },
        {
            name: "13th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        },
        {
            name: "14th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        },
        {
            name: "15th Latin American Research Symposium Submissions",
            url: "https://calendar.ncsu.edu/event/8th_latin_american_research_symposium-_submission_deadline_march_28_2021#.YFZSa0NKiV4",
            imgurl: "https://localist-images.azureedge.net/photos/36226378104779/big_square/53fec8400c6adc6cebb230ef9539e3924d1f9e63.jpg",
            date: "3/20/2021",
            time: "6:30 pm",
            location: "Virtual"
        }
    ];

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