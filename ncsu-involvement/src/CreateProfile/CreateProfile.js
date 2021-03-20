import React from "react";
import { useState } from "react";

import { Interests } from "../Interests/Interests";

const DEFAULT_SELECT = "-- Select an option --";
const DEPARTMENTS = {
    "College of Agriculture and Life Sciences": [
        "Agricultural and Human Sciences",
        "Agricultural and Resource Economics",
        "Agricultural Institute",
        "Animal Science",
        "Applied Ecology",
        "Biological and Agricultural Engineering",
        "Crop and Soil Sciences",
        "Entomology and Plant Pathology",
        "Food, Bioprocessing, and Nutrition Sciences",
        "Horticultural Science",
        "Molecular and Structural Biochemistry",
        "Plant and Microbial Biology",
        "Prestage Department of Poultry Science"
    ],
    "College of Design": [
        "Architecture",
        "Art + Design",
        "Graphic Design",
        "Industrial Design",
        "Landscape Architecture and Environmental Planning"
    ],
    "College of Education": [
        "Educational Leadership, Policy, and Human Development",
        "Science, Technology, Engineering, & Mathematics Education",
        "Teacher Education and Learning Sciences"
    ],
    "College of Engineering": [
        "Biological and Agricultural Engineering",
        "Biomedical Engineering",
        "Chemical and Biomolecular Engineering",
        "Civil, Construction and Environmental Engineering",
        "Computer Science",
        "Edward P. Fitts Department of Industrial & Systems Engineering",
        "Electrical and Computer Engineering",
        "Materials Science and Engineering",
        "Mechanical and Aerospace Engineering",
        "Nuclear Engineering"
    ],
    "College of Humanities and Social Sciences": [
        "Communication",
        "English",
        "Foreign Languages and Literatures",
        "History",
        "Interdisciplinary Studies",
        "Philosophy and Religious Studies",
        "Political Science [in the School of Public and International Affairs]",
        "Psychology",
        "Public Administration [in the School of Public and International Affairs]",
        "Social Work",
        "Sociology and Anthropology"
    ],
    "College of Natural Resources": [
        "Forest Biomaterials",
        "Forestry and Environmental Resources",
        "Parks, Recreation and Tourism Management"
    ],
    "Poole College of Management": [
        "Accounting",
        "Business Management",
        "Economics",
        "Management, Innovation and Entrepreneurship"
    ],
    "College of Sciences": [
        "Biological Sciences",
        "Chemistry",
        "Marine, Earth, and Atmospheric Sciences",
        "Mathematics",
        "Physics",
        "Statistics"
    ],
    "Wilson College of Textiles": [
        "Textile and Apparel, Technology and Management",
        "Textile Engineering, Chemistry and Science"
    ],
    "College of Veterinary Medicine": [
        "Clinical Sciences",
        "Molecular Biomedical Sciences",
        "Population Health and Pathobiology"
    ]
};


export function CreateProfile(props) {
    const [college, setCollege] = useState(null);
    const [interests, setInterests] = useState(null);

    function handleFormSubmit(event) {

    }


    return (
        <form onSubmit={handleFormSubmit}>
            <h1>Edit Profile</h1>
            <div class="input-area">
                <label>
                    College:
                    <select name="college" value={college} onChange={e => setCollege(e.target.value)}>
                        <option value={null}>{DEFAULT_SELECT}</option>
                        {Object.keys(DEPARTMENTS).map(coll => <option value={coll} key={coll}>{coll}</option>)}
                    </select>
                </label>
            </div>

            <div class="input-area">
                {college && (
                    <label>
                        Department:
                        <select disabled={college === null} name="department">
                            <option value={null}>{DEFAULT_SELECT}</option>
                            {DEPARTMENTS[college].map(dep => <option value={dep} key={dep}>{dep}</option>)}
                        </select>
                    </label>
                )}
            </div>

            <div class="input-area">
                <label>
                    Interests:
                    <Interests />
                    {/* <input type="text" value={interests} onChange={e => setInterests(e.target.value)} /> */}
                </label>
            </div>
        </form>
    );
}
