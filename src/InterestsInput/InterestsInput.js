import React, { useState } from "react";
import Autosuggest from 'react-autosuggest';

const INTERESTS = [
    "Politics", "Leadership", "Student Government", "Greek Life", "Religion",
    "Sports", "Technology", "Gaming", "Arts", "Service"
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

export class InterestsInput extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            // suggestions: []
            suggestions: INTERESTS
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
        this.setState({ suggestions: INTERESTS });
        // this.setState({ suggestions: [] });
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
                // alwaysRenderSuggestions={true}
                inputProps={inputProps}
            />
        );
    }
}
