import React from "react";

import "./OrgInfo.css";

export const OrgInfo = ({ name, imgurl, orgurl, category, tags }) => (
    <div className="org-info">
        <a href={orgurl}>
            <div className="org-info-img-container">
                <img src={imgurl} alt={name} />
            </div>
        </a>
        <a href={orgurl}>
            <h3>{name}</h3>
        </a>
        <h4>Category: {category}</h4>
        <h4>Tags: {tags}</h4>
    </div>
);