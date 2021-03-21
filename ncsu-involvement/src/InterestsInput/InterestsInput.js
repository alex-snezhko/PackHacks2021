import React, { useState } from "react";
import Autosuggest from 'react-autosuggest';

const INTERESTS = [
    "Politics/Advocacy", "Leadership", "Student Government", "Greek Life", "Religion",
    "Sports & Recreation", "Technology", "Gaming", "Arts"
].sort();

const getSuggestions = value => {
    const inputValue = value.trim().toLowerCase();
    const inputLength = inputValue.length;

    return inputLength === 0 ? [] : INTERESTS.filter(int =>
        int.toLowerCase().slice(0, inputLength) === inputValue
    );
};

const getSuggestionValue = suggestion => suggestion;

const renderSuggestion = suggestion => suggestion;
// (
//     <div>
//         {suggestion}
//     </div>
// );

export class InterestsInput extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            // value: '',
            suggestions: []
            // suggestions: INTERESTS
        };
    }

    // onChange = (event, { newValue }) => {
    //     this.setState({
    //         value: newValue
    //     });
    // };

    onSuggestionsFetchRequested = ({ value }) => {
        this.setState({
            suggestions: getSuggestions(value)
        });
    };

    onSuggestionsClearRequested = () => {
        // this.setState({ suggestions: INTERESTS });
        this.setState({ suggestions: [] });
    };

    render() {
        const { suggestions } = this.state;

        const inputProps = {
            placeholder: 'Type something you are interested in',
            value: this.props.value,
            onChange: this.props.onChange,
            size: "30"
        };

        return (
            <Autosuggest
                suggestions={suggestions}
                onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
                onSuggestionsClearRequested={this.onSuggestionsClearRequested}
                getSuggestionValue={getSuggestionValue}
                renderSuggestion={renderSuggestion}
                // shouldRenderSuggestions={() => true}
                alwaysRenderSuggestions={true}
                inputProps={inputProps}
            />
        );
    }
}
