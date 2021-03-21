import React from "react";
import { AiFillCalendar, AiFillClockCircle } from "react-icons/ai";
import { HiLocationMarker } from "react-icons/hi";

import "./EventInfo.css";

export const EventInfo = ({ name, imgurl, url, date, time, location }) => (
    <div className="event-info">
        <a href={url}>
            <div className="event-info-img-container">
                <img src={imgurl} alt={name} />
            </div>
        </a>
        <div style={{marginLeft: "15px"}}>
            <a href={url}>
                <h3>{name}</h3>
            </a>
            <p><AiFillCalendar /><b>Date:</b> {date}</p>
            <p><AiFillClockCircle /><b>Time:</b> {time}</p>
            <p><HiLocationMarker /><b>Location:</b> {location}</p>
        </div>
    </div>
);
