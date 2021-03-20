import React, { useState } from "react";
import Autosuggest from 'react-autosuggest';

const INTERESTS = [
    "Politics/Advocacy", "Leadership", "Student Government", "Greek Life", "Religion",
    "Sports & Recreation", "Technology", "Gaming", "Arts"
].sort();

const getSuggestions = value => {
    const inputValue = value.trim().toLowerCase();
    return INTERESTS.filter(int => int.toLowerCase().slice(0, inputValue.length) === inputValue);
}

export function Interests() {
    const [input, setInput] = useState("");
    const [suggestions, setSuggestions] = useState([]);

    return (
        <Autosuggest
            suggestions={suggestions}
            onSuggestionsFetchRequested={({ value }) => setSuggestions(getSuggestions(value))}
            onSuggestionsClearRequested={() => setSuggestions([])}
            getSuggestionValue={sugg => sugg}
            renderSuggestion={suggestion => <div>{suggestion}</div>}
            inputProps={{
                placeholder: "Type something you are interested in",
                value: input,
                onChange: setInput
            }}
        />
    )
}
