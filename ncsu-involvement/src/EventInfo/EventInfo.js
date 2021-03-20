import React from "react";

import "./EventInfo.css";

export const EventInfo = ({ name, imgurl, url, date, time, location }) => (
    <div className="event-info">
        <a href={url}>
            <div className="event-info-img-container">
                <img src={imgurl} alt={name} />
            </div>
        </a>
        <a href={url}>
            <h3>{name}</h3>
        </a>
        <h4>Date: {date}</h4>
        <h4>Time: {time}</h4>
        <h4>Location: {location}</h4>
    </div>
);
