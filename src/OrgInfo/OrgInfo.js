import React from "react";
import { AiFillTags } from "react-icons/ai";
import { BsFillInboxesFill } from "react-icons/bs";

// import "./OrgInfo.css";
import "../EventInfo/EventInfo.css";

export const OrgInfo = ({ name, img, orgurl }) => (
    <div className="event-info">
        <a href={orgurl}>
            <div className="event-info-img-container">
                <img src={img} alt={name} />
            </div>
        </a>
        <div style={{marginLeft: "15px"}}>
            <a href={orgurl}>
                <h3>{name}</h3>
            </a>
            {/* <p><AiFillTags /><b>Category:</b> {category}</p> */}
            {/* <p><BsFillInboxesFill /><b>Tags:</b> {tags.join(", ")}</p> */}
        </div>
        
    </div>
);